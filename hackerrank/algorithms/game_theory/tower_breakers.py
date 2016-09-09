def moves(l):
    # tot = len([x for x in l if x != 1])
    # if tot % 2 == 0:
    #     return "2"
    # if tot % 2 == 1:
    #     return "1"
    return "2" if len([x for x in l if x != 1]) % 2 == 0 else "1"

lst = [2,2]
print moves(lst)