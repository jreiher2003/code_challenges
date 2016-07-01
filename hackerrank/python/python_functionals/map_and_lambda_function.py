fibo = lambda n: 1 if n <= 2 else fibo(n-1) + fibo(n-2)

print fibo(4)

# fib = lambda n: reduce(lambda x: x+[x[-1]+x[-2]], range(n-2), [0, 1])
# print fib(4)


result = [0,1]
fib = lambda n: map(lambda _: result.append(result[-1] + result[-2]), xrange(n-2))
print fib(0)
print [x**3 for x in result]


result = [0,1]
fib = lambda n: map(lambda _: result.append(result[-1] + result[-2]), xrange(n-2))
n = int(raw_input())
if n == 1:
    print [0]
if n == 0:
    print []
else:
    fib(n)
    print [x**3 for x in result]