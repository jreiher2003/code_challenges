A = [89,90,78,93,80]
B = [90,91,85,88,86]
C = [91,92,83,89,90.5]

D = [A]+[B]+[C]
print D
col =  zip(*D)
for x in col:
	print sum(x)/len(x)
