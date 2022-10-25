import sys
from oaipmh.client import Client
from oaipmh.metadata import MetadataRegistry, oai_dc_reader

def yeartostr(year):
	if year > 1000:
		return str(year)
	if year == -1:
		return "all"
	if year == 199:
		return "1990s"	
	if year == 200:
		return "2000s"	
	if year == 201:
		return "2010s"	
	if year == 202:
		return "2020s"	
def print_header(year):
	print("""
<html><head><meta charset=\"utf-8\"></head> 
<body> 
    <h1>Cryptology ePrint Archive: Listing for  """+yeartostr(year)+""" </h1> 
    <p/> 
    <hr/> 
    <p/> 
<script> 
function myFunction() {
  // Declare variables
  var input, filter, ul, li, a, i, txtValue;
  input = document.getElementById('myInput');
  filter = input.value.toUpperCase();
  ul = document.getElementById("myul");
  li = ul.getElementsByTagName('li');

  // Loop through all list items, and hide those who don't match the search query
  for (i = 0; i < li.length; i++) {
    title = li[i].getElementsByTagName("b")[0];
    author = li[i].getElementsByTagName("em")[0];
    txtValue = title.textContent + author.textContent;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      li[i].style.display = "";
    } else {
      li[i].style.display = "none";
    }
  }
}
</script>
<input type="text" style="width: 450px;" id="myInput" onkeyup="myFunction()" placeholder="Search for title or author...">
<ul id="myul" style="list-style: none;padding-left: 0;"> 
""")

def print_footer():
	print("\
    </ul>\
    <p/>\
    <hr/>\
    [ <a href=\"http://ia.cr/\">Cryptology ePrint archive</a>]\
</body>\
</html>\
")

year = int(sys.argv[1])
papers = []

f = open(sys.argv[2], 'r')

for line in f.readlines():
    i_year = int(line.split("/")[3])
    if year > 1000:
        if i_year < year:
            break
        if i_year == year:
            papers.append(line)
    elif year in [199,200,201,202]:
        if i_year < year*10:
            break
        if i_year < (year+1)*10:
            papers.append(line)
    elif year == -1:
        papers.append(line)
f.close()

print_header(year)
for paper in papers:
    print(paper)
print_footer()
