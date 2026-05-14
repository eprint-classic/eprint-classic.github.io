from oaipmh_scythe import Scythe
import sys, time

BASE_URL = "https://eprint.iacr.org/oai"

NS = {
    "oai_dc": "http://www.openarchives.org/OAI/2.0/oai_dc/",
    "dc": "http://purl.org/dc/elements/1.1/",
}

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:128.0) Gecko/20100101 Firefox/128.0"

for attempt in range(3):
    papers = []
    try:
        with Scythe(BASE_URL, max_retries=3, retry_status_codes=[503, 403]) as scythe:
            scythe.client.headers["user-agent"] = UA
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

if papers:
    top = papers[0]
    print(f"harvested {len(papers)} papers; newest={top[0]}/{top[1]}", file=sys.stderr)
else:
    print("harvested 0 papers", file=sys.stderr)

for p_year, paper_id, title, authors in papers:
    print(
        f'<li><a href="https://eprint.iacr.org/{p_year}/{paper_id}">{p_year}/{paper_id}</a> '
        f'(<a href="https://eprint.iacr.org/{p_year}/{paper_id}.pdf">PDF</a>) '
        f'<dd><b>{title}</b><dd><em>{authors}</em></li>'
    )
