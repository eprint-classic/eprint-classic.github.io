from oaipmh_scythe import Scythe
import time

BASE_URL = "https://eprint.iacr.org/oai"

NS = {
    "oai_dc": "http://www.openarchives.org/OAI/2.0/oai_dc/",
    "dc": "http://purl.org/dc/elements/1.1/",
}

papers = []

# If oaipmh-scythe supports custom headers/session args in your installed version,
# set a real User-Agent there. Otherwise wrap this in retry logic.
for attempt in range(3):
    try:
        with Scythe(BASE_URL) as scythe:
            records = scythe.list_records(metadata_prefix="oai_dc")
            for record in records:
                if record.deleted:
                    continue

                title_el = record.xml.find(".//dc:title", namespaces=NS)
                id_el = record.xml.find(".//dc:identifier", namespaces=NS)
                author_els = record.xml.findall(".//dc:creator", namespaces=NS)

                if title_el is None or id_el is None or id_el.text is None:
                    continue

                iden = id_el.text
                if not iden.startswith("https://eprint.iacr.org/"):
                    continue

                parts = iden[len("https://eprint.iacr.org/"):].split("/")
                if len(parts) < 2:
                    continue

                p_year, paper_id = parts[0], parts[1]
                authors = ", ".join(a.text for a in author_els if a.text)

                papers.append((p_year, paper_id, title_el.text or "", authors))
        break
    except Exception:
        if attempt == 2:
            raise
        time.sleep(15)

papers.sort(key=lambda x: 10000 * int(x[0]) + int(x[1]), reverse=True)

for p_year, paper_id, title, authors in papers:
    print(
        f'<li><a href="https://eprint.iacr.org/{p_year}/{paper_id}">{p_year}/{paper_id}</a> '
        f'(<a href="https://eprint.iacr.org/{p_year}/{paper_id}.pdf">PDF</a>) '
        f'<dd><b>{title}</b><dd><em>{authors}</em></li>'
    )
