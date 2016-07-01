lst = [[10,2,5],[7,1,0],[9,9,9],[1,23,12],[6,5,9]]
y = 1
sort_lst = sorted(lst,key=lambda x: x[y])
# for elm in sort_lst:
#     print " ".join(str(x) for x in elm)


import textwrap 
print " ".join([str(x) for elm in sort_lst for x in elm])