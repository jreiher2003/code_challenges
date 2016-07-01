

def move_zeros(nums):
    len_zero_list = len([x for x in nums if x == 0])
    nums[:] = [x for x in nums if x != 0]
    nums[:] += [0] * len_zero_list
    return nums


nums = [0,1,0,3,12]
print move_zeros(nums)