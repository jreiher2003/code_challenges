from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print tag
        for at in attrs:
            print "->",at[0], ">", at[1]

    def handle_startendtag(self, tag, attrs):
        print tag
        for at in attrs:
            print "->",at[0], ">", at[1]

parser = MyHTMLParser()
parser.feed("""<head>
<title>HTML</title>
</head>
<object type="application/x-flash" 
  data="your-file.swf" 
  width="0" height="0">
  <!-- <param name="movie" value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>""")
