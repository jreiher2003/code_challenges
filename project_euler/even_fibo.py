


def even_fib(n):
    count = 0
    a,b = 1,1
    for i in range(n-1):
        a,b = b, a+b
        if b % 2 == 0:
            print b
            count += b
    return a, count

print even_fib(33)