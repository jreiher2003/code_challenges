
def maximizing(k, m):
    max_lst = []
    for lst in range(len(k)):
        max_lst.append(max(k[lst]))
    return sum([(x)**2%m for x in max_lst])

big_list = [[2,5,4],[3,7,8,9],[5,5,7,8,9,10]]
print maximizing(big_list,1000) 

