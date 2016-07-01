def power_of_fo(num):
    # if n == 0:
    #   return 0
    # if n == 1:
    #   return 1
    
            
    if num <= 0:
        return False
    while num % 4 == 0:
        num = num/4
        
    
    return True if num ==1 else False

print power_of_fo(16)
print power_of_fo(5)