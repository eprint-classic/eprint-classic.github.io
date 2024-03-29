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
 <!DOCTYPE html>
<html><head><meta charset=\"utf-8\"></head> 
<body> 
    <h1>Cryptology ePrint Archive: Listing for  """+yeartostr(year)+""" </h1> 
    <hr/> 
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
<ul id="headerul">

	<li>		<a href="https://eprint-classic.github.io/all.html">[ePrint 1996 - now ]</a> (~5MB!)	</li>
	<li><a href="https://eprint-classic.github.io/2020s.html">[ePrint 2020 - now ]</a>
			&nbsp;&nbsp;&nbsp;<a href="https://eprint-classic.github.io/2024.html">[ePrint 2024]</a>
			&nbsp;&nbsp;&nbsp;<a href="https://eprint-classic.github.io/2023.html">[ePrint 2023]</a>
			&nbsp;&nbsp;&nbsp;<a href="https://eprint-classic.github.io/2022.html">[ePrint 2022]</a>
			&nbsp;&nbsp;&nbsp;<a href="https://eprint-classic.github.io/2021.html">[ePrint 2021]</a>
			&nbsp;&nbsp;&nbsp;<a href="https://eprint-classic.github.io/2020.html">[ePrint 2020]</a>
	<li>		<a href="https://eprint-classic.github.io/2010s.html">[ePrint 2010 - 2019]</a>
			&nbsp;&nbsp;&nbsp;<a href="https://eprint-classic.github.io/2019.html">[ePrint 2019]</a>
			&nbsp;&nbsp;&nbsp;<a href="https://eprint-classic.github.io/2018.html">[ePrint 2018]</a>
			&nbsp;&nbsp;&nbsp;<a href="https://eprint-classic.github.io/2017.html">[ePrint 2017]</a>
			&nbsp;&nbsp;&nbsp;<a href="https://eprint-classic.github.io/2016.html">[ePrint 2016]</a>
			&nbsp;&nbsp;&nbsp;<a href="https://eprint-classic.github.io/2015.html">[ePrint 2015]</a>
			&nbsp;&nbsp;&nbsp;<a href="https://eprint-classic.github.io/2014.html">[ePrint 2014]</a>
			&nbsp;&nbsp;&nbsp;<a href="https://eprint-classic.github.io/2013.html">[ePrint 2013]</a>
			&nbsp;&nbsp;&nbsp;<a href="https://eprint-classic.github.io/2012.html">[ePrint 2012]</a>
			&nbsp;&nbsp;&nbsp;<a href="https://eprint-classic.github.io/2011.html">[ePrint 2011]</a>
			&nbsp;&nbsp;&nbsp;<a href="https://eprint-classic.github.io/2010.html">[ePrint 2010]</a>	</li>
	<li>		<a href="https://eprint-classic.github.io/2000s.html">[ePrint 2000 - 2009]</a>
			&nbsp;&nbsp;&nbsp;<a href="https://eprint-classic.github.io/2009.html">[ePrint 2009]</a>
			&nbsp;&nbsp;&nbsp;<a href="https://eprint-classic.github.io/2008.html">[ePrint 2008]</a>
			&nbsp;&nbsp;&nbsp;<a href="https://eprint-classic.github.io/2007.html">[ePrint 2007]</a>
			&nbsp;&nbsp;&nbsp;<a href="https://eprint-classic.github.io/2006.html">[ePrint 2006]</a>
			&nbsp;&nbsp;&nbsp;<a href="https://eprint-classic.github.io/2005.html">[ePrint 2005]</a>
			&nbsp;&nbsp;&nbsp;<a href="https://eprint-classic.github.io/2004.html">[ePrint 2004]</a>
			&nbsp;&nbsp;&nbsp;<a href="https://eprint-classic.github.io/2003.html">[ePrint 2003]</a>
			&nbsp;&nbsp;&nbsp;<a href="https://eprint-classic.github.io/2002.html">[ePrint 2002]</a>
			&nbsp;&nbsp;&nbsp;<a href="https://eprint-classic.github.io/2001.html">[ePrint 2001]</a>
			&nbsp;&nbsp;&nbsp;<a href="https://eprint-classic.github.io/2000.html">[ePrint 2000]</a>	</li>
	<li>		<a href="https://eprint-classic.github.io/1990s.html">[ePrint 1996 - 1999]</a>
			&nbsp;&nbsp;&nbsp;<a href="https://eprint-classic.github.io/1999.html">[ePrint 1999]</a>
			&nbsp;&nbsp;&nbsp;<a href="https://eprint-classic.github.io/1998.html">[ePrint 1998]</a>
			&nbsp;&nbsp;&nbsp;<a href="https://eprint-classic.github.io/1997.html">[ePrint 1997]</a>
			&nbsp;&nbsp;&nbsp;<a href="https://eprint-classic.github.io/1996.html">[ePrint 1996]</a>	</li>


    </ul>
<input type="text" style="width: 450px;" id="myInput" onkeyup="myFunction()" placeholder="Search for title or author...">
<ul id="myul" style="list-style: none;padding-left: 0;"> 
""")

def print_footer():
	print("\
    </ul>\
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
