#N = sticks
#len of stick is +int
# cut len of all sticks BY the len of shortest  

# def cut_sticks(lst):
#     cut = lst 
#     while len(cut) > 0:
#         cut = list(filter(lambda x: x!=0, [(x-min(lst)) for x in lst]))
#         new_cut = list(filter(lambda x: x!=0, [(x-min(cut)) for x in cut]))
#         new_cut1 = list(filter(lambda x: x!=0, [(x-min(new_cut)) for x in new_cut]))
#         print new_cut1
#         break
def cut_sticks(lst):
    while lst:
        print len(lst)
        minItem = min(lst)
        lst = [(x-minItem) for x in lst if (x-minItem) >0]
        




sticks = [1,2,3,4,3,3,2,1]
sticks1 = [5,4,4,2,2,8]
print cut_sticks(sticks)
print cut_sticks(sticks1)