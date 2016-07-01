import re 
print bool(re.search(r"ly","similarly"))
print re.search(r"ly","similarly")

print bool(re.match(r"ly","similarly"))
print bool(re.match(r"ly","ly should be in the beginning"))

print bool(re.search(r"\d+\.\d+", '13.3'))