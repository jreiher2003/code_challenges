import re
S=input().strip() 
print(bool(re.search(r'^[1-9]\d{5}$',S) and len(re.findall(r'(?=(\d)\d\1)', S)) <2))


postalcode = r'.*(\d{5}(\-\d{4})?)$'