

def count_up(num):
    num10 = num + 10
    str1 = ""
    for i in range(num+1,num10+1):
        str1 += str(i) + " then "
    print str1[:-5]
        
        
        # print str(num10)

count_up(60)