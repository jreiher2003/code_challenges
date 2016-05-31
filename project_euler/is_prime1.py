

def is_prime(num):
    lst = []
    for num in xrange(2,num+1):
        prime = True
        for i in xrange(2,num):
            if num % i == 0:
                prime = False
        if prime:
            lst.append(num)
    return len(lst), max(lst)
                

print is_prime(100)
# print is_prime(600851475143)

def is_pprime(num):
    factor_list = []
    n = 9999
    for i in range(2, n+1):
        prime = True
        for j in range(2,i):
            if i % j == 0:
                prime = False
                break
        if prime == True:
            if num % i == 0:
                factor_list.append(i)
        factor_list.sort()
    print factor_list.pop()

print is_pprime(600851475143)
import math

def is_prime_p(num):
    prime = False
    if num > 1:
        prime = True
        k = 2 
        num = math.sqrt(num)
        while k <= num and prime == True:
            if num % k == 0:
                prime = False 
            k += 1
    return prime

print is_prime_p(600851475143)

