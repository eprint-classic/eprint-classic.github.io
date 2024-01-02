from sickle import Sickle

papers = []

s = Sickle('https://eprint.iacr.org/oai')
rs = s.ListRecords(metadataPrefix='oai_dc', ignore_deleted=True)
for record in rs:
    data = record.metadata

    p_year = data["identifier"][0][len("https://eprint.iacr.org/"):].split("/")[0]
    id = data["identifier"][0][len("https://eprint.iacr.org/"):].split("/")[1]
    title = data["title"][0]
    authors = data["creator"]
    for i in range(len(authors)):
        if authors[i].startswith("and "):
            authors[i] = authors[i][3:]

    papers.append((p_year, id, title, ", ".join(authors)))

papers.sort(key=lambda x: 10000*int(x[0])+int(x[1]), reverse=True)

for paper in papers:
    print("\
	<li>\
		<a href=\""+"http://eprint.iacr.org/"+paper[0] + "/" + paper[1]+"\">"+paper[0] + "/" + paper[1]+"</a>\
		(<a href=\""+"http://eprint.iacr.org/"+paper[0] + "/" + paper[1]+".pdf\">PDF</a>)\
	<dd><b>", paper[2],"</b><dd><em>", paper[3],"</em></li>")