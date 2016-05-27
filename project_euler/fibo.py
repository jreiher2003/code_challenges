def fibo(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	else:
		return fibo(n-1) + fibo(n-2)

print fibo(15)


def fibo1(n):
	lst = [0,1]
	i = 2
	while i <= n:
		lst.append(lst[n-1] + lst[n-2])
		i+=1
	return lst(n)
print fibo1(15)

def fibonacci(n):
    a,b = 1,1 
    for i in range(n-1):
    	a,b = b, a+b 
    return a


print fibonacci(15)