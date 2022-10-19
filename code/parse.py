import sys
from oaipmh.client import Client
from oaipmh.metadata import MetadataRegistry, oai_dc_reader

def print_header(year):
	print("\
<html><head><meta charset=\"utf-8\"></head> \
<body> \
    <h1>Cryptology ePrint Archive: Listing for  "+str(year)+" </h1> \
    <p/> \
    <hr/> \
    <p/> \
    <dl> \
")

def print_footer():
	print("\
    </dl>\
    <p/>\
    <hr/>\
    [ <a href=\"http://ia.cr/\">Cryptology ePrint archive</a>]\
</body>\
</html>\
")

URL = 'https://eprint.iacr.org/oai'
registry = MetadataRegistry()
registry.registerReader('oai_dc', oai_dc_reader)
client = Client(URL, registry)
year = int(sys.argv[1])
papers = []

for record in client.listRecords(metadataPrefix='oai_dc'):
    if record[1] is not None:
        data = record[1].getMap()

        p_year = data["identifier"][0][len("https://eprint.iacr.org/"):].split("/")[0]
        id = data["identifier"][0][len("https://eprint.iacr.org/"):].split("/")[1]
        title = data["title"][0]
        authors = data["creator"]
        for i in range(len(authors)):
            if authors[i].startswith("and "):
                authors[i] = authors[i][3:]

        papers.append((p_year, id, title, ", ".join(authors)))
        if int(p_year) < year:
            break

papers.sort(key=lambda x: int(x[1]), reverse=True)

print_header(year)
for paper in papers:
    print("\
	<dt>\
		<a href=\""+"http://eprint.iacr.org/"+paper[0] + "/" + paper[1]+"\">"+paper[0] + "/" + paper[1]+"</a>\
		(<a href=\""+"http://eprint.iacr.org/"+paper[0] + "/" + paper[1]+".pdf\">PDF</a>)\
	<dd><b>", paper[2],"</b><dd><em>", paper[3],"</em>")
print_footer()