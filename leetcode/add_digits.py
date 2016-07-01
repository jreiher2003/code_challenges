def add_digits(num):
    while len(str(num)) > 1:
        num = sum([int(x) for x in list(str(num))])
    return num
   
 
print add_digits(3882)


