
def closest_nums(t):
    # absolute_diff = []
    # for i in lst:
    #     for j in lst:
    #         if i < j:
    #             absolute_diff.append(abs(j-i))
    # minabsdiff = sorted(absolute_diff)[0]
    minabsdiff = sorted([abs(j-i) for i,j in zip(t, t[1:])])[0]
    tup = []
    # for i in t:
    #     for j in t:
    #         if (i + minabsdiff) == j:
    x = [tup.append((i,j)) for i, j in zip(t,t[1:]) if (i+ minabsdiff == j)]
    print tup,x
    # tup = sorted(tup)
    # for i in tup:
    #     print i[0],i[1]

closest_nums([4,-2,-1,3])

def new(t):
    print sorted([abs(j-i) for i,j in zip(t, t[1:])])[0]

# new([4,2,1,3])