def sub_arr(lst):
    max_ending_here = max_so_far = lst[0]
    for x in lst[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far 

# def sub_arr(A):
#     max_ending_here = max_so_far = 0
#     for x in A:
#         max_ending_here = max(0, max_ending_here + x)
#         max_so_far = max(max_so_far, max_ending_here)
#     return max_so_far

def max_sub_arr(lst):
    if len(lst) == 1:
        return lst[0]
    elif all(item < 0 for item in lst):
        return max(lst)
    else:    
        return sum([x for x in lst if x > 0])


sub = [1]
sub2 = [-1,-2,-3,-4,-5,-6]
sub3 = [1,-2]
sub4 = [1,2,3]
sub5 = [-10]
sub6 = [1,-1,-1,-1,-1,5]

print sub_arr(sub), max_sub_arr(sub)
print sub_arr(sub2), max_sub_arr(sub2)
print sub_arr(sub3), max_sub_arr(sub3)
print sub_arr(sub4), max_sub_arr(sub4)
print sub_arr(sub5), max_sub_arr(sub5)
print sub_arr(sub6), max_sub_arr(sub6)

# print all(sub2) < 0
# for x in sub2:
#     print x
# print sub2
# # print 0  all(sub2)
print all(item < 0 for item in sub4) 