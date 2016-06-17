from itertools import *
a = 4
b = sorted(["a","a","c","d"])
c = 2
d = set(combinations(xrange(a),c))

e = {x for x in d if b[x[0]] == 'a'}

print 1.*len(e)/len(d)