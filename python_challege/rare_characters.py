import urllib2 
import re

def get_page(url):
	return urllib2.urlopen(url).read()



if __name__ == "__main__":
	page = get_page("http://www.pythonchallenge.com/pc/def/ocr.html")
	text = (re.findall(r'<!--(.*?)-->', page, re.DOTALL))[1]
	s = ''
	for i in text:
	    if text.count(i) < 10:
	        s += i
	print(s)