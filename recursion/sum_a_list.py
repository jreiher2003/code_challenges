def sum_even(n):
 total = 0
 for i in range(2, n+1,2):
     total = total + i
 return total

print sum_even(10)

def sum_even1(n):
    if n == 0:
        return 0
    elif n % 2 != 0:
        return sum_even1(n-1)
    return n + sum_even1(n-2)
    

print sum_even1(11)