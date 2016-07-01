# Create a random list of numbers
from itertools import groupby

def group_by_iter(s):
    s1 = [list(g) for k, g in groupby(s)]
    for i in s1:
        print (len(i),int(i[0])),


print group_by_iter("1222311")


