from oaipmh_scythe import Scythe

BASE_URL = "https://eprint.iacr.org/oai"

NS = {
    "oai_dc": "http://www.openarchives.org/OAI/2.0/oai_dc/",
    "dc": "http://purl.org/dc/elements/1.1/"
}

papers = []


with Scythe(BASE_URL) as scythe:
    records = scythe.list_records(
    )

    for record in records:
        if record.deleted:
            continue

        title = record.xml.find(".//dc:title", namespaces=NS).text
        iden = record.xml.find(".//dc:identifier", namespaces=NS).text
        id = iden[len("https://eprint.iacr.org/"):].split("/")[1]
        p_year = iden[len("https://eprint.iacr.org/"):].split("/")[0]
        authors = record.xml.findall(".//dc:creator", namespaces=NS)
        authors2 = [i.text for i in authors]
        papers.append((p_year, id, title, ", ".join(authors2)))

papers.sort(key=lambda x: 10000*int(x[0])+int(x[1]), reverse=True)

for paper in papers:
    print("\
	<li>\
		<a href=\""+"http://eprint.iacr.org/"+paper[0] + "/" + paper[1]+"\">"+paper[0] + "/" + paper[1]+"</a>\
		(<a href=\""+"http://eprint.iacr.org/"+paper[0] + "/" + paper[1]+".pdf\">PDF</a>)\
	<dd><b>", paper[2],"</b><dd><em>", paper[3],"</em></li>")
