from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if data.strip():
            lines = str(data).split("\n")
            print(">>> ", "Multi" if len(lines) > 1 else "Single", "-line Comment", sep="")
            print(*lines, sep="\n")

    def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)

html = ""
for i in range(N):
    html += raw_input().strip()
    html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()




parser = MyHTMLParser()
parser.feed("<div> Welcome to HackerRank</div>")

