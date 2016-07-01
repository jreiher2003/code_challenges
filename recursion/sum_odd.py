# sum_odd(n): number -> number
# sum_odd(n) is the sum of odd numbers from 1 to N
def sum_odd1(n):
    total = 0
    for i in range(1,n,2):
        total = total + i
    return total

print sum_odd1(12)

def sum_odd2(n):
    # if n == 0:
    #     return 0
    if n < 2:
        return 1
    elif n % 2 == 0:
        return sum_odd2(n-1)
    else:
        return n + sum_odd2(n-2)

print sum_odd2(12)