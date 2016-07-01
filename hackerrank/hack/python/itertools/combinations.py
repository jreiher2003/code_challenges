from itertools import combinations 
# print list(combinations('12345', 2))

# print list(combinations([1,1,3,3,3],4))

def comb(s,k):
    lst = sorted([letter for letter in s])
    for n in range(1,k+1):
        comby = list(combinations(lst, n))
        for i in comby:
            print "".join(i)

print comb("HACK",2)