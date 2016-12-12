from collections import deque 

def zig_zag(lst):
    new_lst = []
    so = sorted(lst)
    so = deque(so)
    while len(so) > 0:
        new_lst.append(so.pop())
        if len(so) > 0:
            new_lst.append(so.popleft())
    for i in new_lst:
        print i
    # print " ".join([str(i) for i in new_lst])

zig_zag([5,2,7,8,-2,25,25])
