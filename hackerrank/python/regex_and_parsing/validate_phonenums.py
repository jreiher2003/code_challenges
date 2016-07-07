import re 
pat = "^[7-9]\d{9}$"
if re.search(pat, "85234789651"):
    print "YES"
else:
    print "NO"