import sys

f = "../poems/" + sys.argv[1]
index = "../index.html"

href = "<p><a href=\"/tseke/poems/[filename]\">[title]</a></p>"

html = "<html lang=\"en\">\n \
	<head>\n \
		<title>Ilepaas's poems</title>\n\
		<meta charset=\"UTF-8\">\n\
		<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n\
		<link rel=\"stylesheet\" href=\"https://tilde.club/style.css\">\n\
	</head>\n \
	<body>\n\
		<h1>~~~[title]~~~~</h1>\n\
[content]\
	</body>\n\
</html>"

contents = []

with(open(f,"r") as fil):
    for line in fil:
        line = line.strip()
        contents.append("\t\t\t<p>" + line + "</p>\n")

content = ""
titled = html.replace("[title]", sys.argv[2])
content = titled.replace("[content]", content.join(contents))

f += ".html"
with(open(f,"w") as fil):
    fil.write(content)

filename = f.replace("../poems/", "")
print(filename)
new_href = href.replace("[filename]", filename)
new_href = new_href.replace("[title]", sys.argv[2])
new_href = "\t\t" + new_href

tempInd = []
with open(index, "r+")as ind:
    lines = ind.readlines()
    for i, line in enumerate(lines):
        if line.startswith("\t\t<!--hrefs-->"):
            lines[i+1] = "\n" + lines[i+1].strip()+ new_href + "\n"
    ind.seek(0)
    for line in lines:
        ind.write(line)
