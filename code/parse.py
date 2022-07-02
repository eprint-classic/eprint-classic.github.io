import sys, bs4, requests

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

year = int(sys.argv[1])
r = requests.get("https://eprint.iacr.org/byyear")
bs = bs4.BeautifulSoup(r.text, 'html.parser')
years = bs.find_all("li")
papers = 0
for i in years:
	if "papers" in i.text:
		if str(year)+" (" in i.text:
			papers = int(i.text.split("(")[1].split("papers")[0])
			break
if papers == 0:
	print("ERROR!")
	exit()
print_header(year)
# get number of pages
pages = int((papers+19)/20)
for i in range(0, pages):
	r = requests.get("https://eprint.iacr.org/"+str(year)+"/?offset="+str(20*i))
	bs = bs4.BeautifulSoup(r.text, 'html.parser')
	titles = bs.find_all("div",class_="papertitle")
	urls = bs.find_all("div",class_="flex-grow-1")
	authors = bs.find_all("div",class_="summaryauthors")

	for i,j,k in zip(titles, authors, urls):
		print("\
	<dt>\
		<a href=\""+"http://eprint.iacr.org/"+k.a['href']+"\">"+k.a['href'][1:]+"</a>\
		(<a href=\""+"http://eprint.iacr.org/"+k.a['href']+".pdf\">PDF</a>)\
	<dd><b>", i.text,"</b><dd><em>", j.text,"</em>")

print_footer()
