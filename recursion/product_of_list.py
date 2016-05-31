def prod(L):
	product, i = 1, 0
	while i < len(L):
		product = product * L[i]
		i = i + 1
	return product
L = [1,2,3,4]
print prod(L)

def prd(L):
	if L == []:
		return 1
	return L[0] * prd(L[1:])

print prd(L)