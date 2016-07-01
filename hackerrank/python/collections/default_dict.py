from collections import defaultdict

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
# print d
# for k, v in s:
#     print k,v
#     d[k].append(v)

# print d.items()

n = 5
m = 2
A = ["a","a","b","a","b"]
B = ["a","b"]

lsta = [str((i+1)) for i, x in enumerate(A) if x == B[0]]
lstb = [str((i+1)) for i, x in enumerate(A) if x == B[1]]
print " ".join(lsta)
print " ".join(lstb)


from collections import defaultdict
d = defaultdict(list)
list1=[]

n, m = map(int,raw_input().split())

for i in range(0,n):
    d[raw_input()].append(i+1) 

for i in range(0,m):
    list1=list1+[raw_input()]  

for i in list1: 
    if i in d:
        print " ".join( map(str,d[i]) )
    else:
        print -1