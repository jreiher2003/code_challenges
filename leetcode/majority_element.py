def majority_elem(nums):
    nums = [(x,nums.count(x)) for x in nums]
    print nums
    return max(nums, key=lambda x: x[1])

# nums = [0,0,0,11]
# nums = [1,1,1,11]
# nums = [0,0,3,3,3,4,4,4,4]
# print majority_elem(nums)

def majorityElem(nums):
    for num in set(nums):
        print num,set(nums)
        # if nums.count(num) > len(nums)/2:
        #     return num
nums = [45,2,43,700,2]
print majorityElem(nums)

def M_E(nums):
    d = {x:nums.count(x) for x in nums}
    return max(d.iteritems(), key=lambda x: x[1])[0]

# nums = [1,1,1,1,1,1,0,34,45,796]
# print M_E(nums)