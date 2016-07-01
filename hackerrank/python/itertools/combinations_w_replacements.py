from itertools import combinations_with_replacement 

print list(combinations_with_replacement("12345",2))

def comb_w_r(s,k):
    lst = sorted([letter for letter in s])
    comby = list(combinations_with_replacement(lst,k))
    for i in comby:
        print "".join(i)

print comb_w_r("HACK",2)