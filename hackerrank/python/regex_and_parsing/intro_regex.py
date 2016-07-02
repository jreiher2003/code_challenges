import re 
print bool(re.search(r"ly","similarly"))
print re.search(r"ly","similarly")

print bool(re.match(r"ly","similarly"))
print bool(re.match(r"ly","ly should be in the beginning"))

print bool(re.search(r"\d+\.\d+", '13.3'))

import re
m = re.search(r'([a-zA-Z0-9])\1', '..12345678910111213141516171820212223')
if m != None:
    print m.group(1)
else:
    print "-1"