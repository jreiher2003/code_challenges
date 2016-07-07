import re 

pat = r'(?:(.)?)(#[0-9A-f]{3,6})(?:[;,.)]{1})'
string = "#FFF"
m = re.findall(pat,string)
for i in m:
    print i
else:
    print 'no good'