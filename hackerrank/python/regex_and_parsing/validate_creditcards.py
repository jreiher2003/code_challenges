import re 

pat = '(?=[4-6])[0-9]{4}(\-?[0-9]{4}){3}$'
repeat = '.*(\d)(\-*\1){3}'
string = '4123456789123456'
m1 = re.match(pat,string)
m2 = re.match(repeat, string)
if m1 and not m2:
    print "Valid"
else:
    print "Invalid"