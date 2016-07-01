print any([1>0,1==0,1<0])
print any([1==2,2==3,4==3])

print all([1==1,2==2,3>1])

lst = ['a','b','c']
print 'x' in lst

def palidrome(n):
	n = str(n)
	if len(n) == 1:
		return True
	elif n[0] != n[-1]:
		return False
	else:
		return palidrome(n[1:-1]) 

print palidrome(5)
print palidrome(121)
print palidrome(23)

print palidrome(1) and all(n>0 for n in [81])
print all(n>0 for n in [81])

N,n = int(raw_input()),raw_input().split()
print all([int(i)>0 for i in n]) and any([j == j[::-1] for j in n])
