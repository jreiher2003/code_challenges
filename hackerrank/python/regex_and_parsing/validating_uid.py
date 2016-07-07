import re

m1 = re.match(r'.*([A-Za-z].*){2}', st)
m2 = re.match(r'.*([0-9].*){3}', st)
m3 = re.match(r'([A-Za-z\d]){10}$', st)
m4 = re.match(r'.*(.).*\1', st)
if m1 and m2 and m3 and not m4:
    print "Valid"
else:
    print "Invalid"
