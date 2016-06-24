l = list(range(10))
print l
lx = list(map(lambda x: x*x, l))
print lx
lxf = list(filter(lambda x: x>10 and x<80, lx))
print lxf