#m=dollars both sunny and jonny have
#N=number of flavors to choose from
#M=the sum of two flavors indices
from itertools import combinations
N = 5
# strlst = "".join(str(x) for x in lst)
# print strlst
# l = []
# new_lst = combinations(lst,2)
# for i in new_lst:
#     if sum(i) <= M:
#         if lst.index(i[0]) == lst.index(i[1]):
#             print lst.index(i[0]), lst[::-1].index(i[1])
M = 4
# lst = [1,4,5,3,2]
lst = [2,2,4,3]
dit = {}        
for i,v in enumerate(lst,start=0):
    dit[i] = v
print dit
maxlst = []
newlst = combinations(lst,2)
for x in newlst:
    if sum(x) <= M:
        maxlst.append((x, sum(x)))
t = max(maxlst,key=lambda item: item[1])
dict_values = t[0]

print [(k+1) for k,v in dit.iteritems() if v==dict_values[0]][0],[(k+1) for k,v in dit.iteritems() if v==dict_values[1]][0]
 









