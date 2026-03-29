import sys

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
var paperIndex = [];
var searchTimer = null;

function escapeRegExp(string) {
return string.replace(/[.*+?^${}()|[\\]\\\\]/g, '\\\\$&');
}

function initSearchIndex() {
  var ul = document.getElementById("myul");
  var li, i, title, author, links, paperId, txtValue;

  if (!ul) return;

  li = ul.getElementsByTagName("li");
  paperIndex = [];

  for (i = 0; i < li.length; i++) {
    title = li[i].getElementsByTagName("b")[0];
    author = li[i].getElementsByTagName("em")[0];
    links = li[i].getElementsByTagName("a");
    paperId = links.length > 0 ? links[0].textContent : "";

    txtValue =
      paperId + " " +
      (title ? title.textContent : "") + " " +
      (author ? author.textContent : "");

    paperIndex.push({
      node: li[i],
      text: txtValue
    });
  }
}

function scheduleSearch() {
  if (searchTimer !== null) {
    clearTimeout(searchTimer);
  }
  searchTimer = setTimeout(myFunction, 120);
}

function myFunction() {
  var input = document.getElementById('myInput');
  var regexBox = document.getElementById('regexMode');
  var pattern, regex, i, matched, newDisplay;

  if (!input || !regexBox) return;

  pattern = input.value;

  if (pattern === "") {
    for (i = 0; i < paperIndex.length; i++) {
      if (paperIndex[i].node.style.display !== "") {
        paperIndex[i].node.style.display = "";
      }
    }
    input.setCustomValidity("");
    return;
  }

  if (!regexBox.checked) {
    pattern = escapeRegExp(pattern);
  }

  try {
    regex = new RegExp(pattern, "i");
    input.setCustomValidity("");
  } catch (err) {
    input.setCustomValidity("Invalid regular expression");
    input.reportValidity();
    return;
  }

  for (i = 0; i < paperIndex.length; i++) {
    matched = regex.test(paperIndex[i].text);
    newDisplay = matched ? "" : "none";

    if (paperIndex[i].node.style.display !== newDisplay) {
      paperIndex[i].node.style.display = newDisplay;
    }
  }
}

window.addEventListener("load", initSearchIndex);
</script>
<ul id="headerul">

	<li>		<a href="https://eprint-classic.github.io/all.html">[ePrint 1996 - now ]</a> (~5MB!)	</li>
	<li><a href="https://eprint-classic.github.io/2020s.html">[ePrint 2020 - now ]</a>
			&nbsp;&nbsp;&nbsp;<a href="https://eprint-classic.github.io/2026.html">[ePrint 2026]</a>
			&nbsp;&nbsp;&nbsp;<a href="https://eprint-classic.github.io/2025.html">[ePrint 2025]</a>
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
<input
  type="text"
  style="width: 450px;"
  id="myInput"
  oninput="scheduleSearch()"
  placeholder="Search for title, author, or paper number..."
>
<label style="margin-left: 10px;">
  <input type="checkbox" id="regexMode" onchange="myFunction()" checked>
  Regex
</label>

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
