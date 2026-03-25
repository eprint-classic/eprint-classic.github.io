from urllib.parse import urlencode
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET
import time

BASE_URL = "https://eprint.iacr.org/oai"

NS = {
    "oai": "http://www.openarchives.org/OAI/2.0/",
    "oai_dc": "http://www.openarchives.org/OAI/2.0/oai_dc/",
    "dc": "http://purl.org/dc/elements/1.1/",
}

PREFIX = "https://eprint.iacr.org/"


def fetch_xml(params, retries=4, sleep_seconds=2):
    query = urlencode(params)
    url = f"{BASE_URL}?{query}"

    last_err = None
    for attempt in range(retries):
        try:
            req = Request(
                url,
                headers={
                    "Accept": "text/xml, application/xml;q=0.9, */*;q=0.1",
                    "Content-Length": "0",
                    "User-Agent": "eprint-classic/1.0 (+https://github.com/eprint-classic/eprint-classic.github.io)",
                    "Connection": "close",
                },
                method="GET",
            )
            with urlopen(req, timeout=60) as resp:
                return ET.fromstring(resp.read())
        except Exception as err:
            last_err = err
            if attempt + 1 < retries:
                time.sleep(sleep_seconds * (attempt + 1))
            else:
                raise last_err


papers = []
params = {"verb": "ListRecords", "metadataPrefix": "oai_dc"}

while True:
    root = fetch_xml(params)

    for record in root.findall(".//oai:record", NS):
        header = record.find("./oai:header", NS)
        if header is not None and header.get("status") == "deleted":
            continue

        title_el = record.find(".//dc:title", NS)
        id_el = record.find(".//dc:identifier", NS)
        author_els = record.findall(".//dc:creator", NS)

        if title_el is None or id_el is None or not id_el.text:
            continue

        ident = id_el.text.strip()
        if not ident.startswith(PREFIX):
            continue

        tail = ident[len(PREFIX):]
        parts = tail.split("/", 1)
        if len(parts) != 2:
            continue

        p_year, paper_id = parts
        title = (title_el.text or "").strip()
        authors = ", ".join(
            a.text.strip() for a in author_els if a is not None and a.text
        )

        papers.append((p_year, paper_id, title, authors))

    token_el = root.find(".//oai:resumptionToken", NS)
    token = token_el.text.strip() if token_el is not None and token_el.text else ""
    if not token:
        break

    params = {"verb": "ListRecords", "resumptionToken": token}

papers.sort(key=lambda x: 10000 * int(x[0]) + int(x[1]), reverse=True)

for paper in papers:
    print("\
	<li>\
		<a href=\""+"http://eprint.iacr.org/"+paper[0] + "/" + paper[1]+"\">"+paper[0] + "/" + paper[1]+"</a>\
		(<a href=\""+"http://eprint.iacr.org/"+paper[0] + "/" + paper[1]+".pdf\">PDF</a>)\
	<dd><b>", paper[2],"</b><dd><em>", paper[3],"</em></li>")
