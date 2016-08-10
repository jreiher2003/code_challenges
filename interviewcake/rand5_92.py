import random 

def rand7():
    return random.randint(1,7)

# print rand7()

def rand5():
    if rand7() == 7:
        return random.randint(1,5)
    if rand7() == 6:
        return random.randint(1,5)
    else:
        return random.randint(1,5)


# from collections import Counter
# import random
# n = 100
# c = Counter(rand5()) 
# for i in range(1,11):
#     print '%2s  %02.10f%%' % (i, c[i] * 100.0 / n)
for i in range(1,5):
    print rand5()