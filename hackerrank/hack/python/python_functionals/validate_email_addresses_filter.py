l = list(range(10))
print l
lx = list(map(lambda x: x*x, l))
print lx
lxf = list(filter(lambda x: x>10 and x<80, lx))
print lxf


import re
lista=[]
for i in xrange(int(input())):
    str_test=str(raw_input())
    lista.append(str_test)
pat=r'^[A-z0-9_-]+@[a-zA-Z0-9]+\.[A-z0-9]{0,3}$'
print sorted(filter(lambda x: re.findall(pat,x),lista))