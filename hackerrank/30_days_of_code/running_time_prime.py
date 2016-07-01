from math import sqrt 

def prime_num(num):
    if num == 2:
        return "Prime"
    if num % 2 == 0 or num <= 1:
        return "Not prime"
    sqrt_num = int(sqrt(num)) + 1 
    for div in range(3, sqrt_num, 2):
        if num % div == 0:
            return "Not prime"
    return "Prime"


           
    
    

print prime_num(7)