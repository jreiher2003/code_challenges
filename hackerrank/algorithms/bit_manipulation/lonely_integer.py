from collections import Counter 

lst = [0,0,1,2,1]
c = Counter(lst)
# for k,v in c.iteritems():
#     if v == 1:
#         print k
#     else:
#         print "0"


print [k for k,v in c.iteritems() if v == 1][0]
