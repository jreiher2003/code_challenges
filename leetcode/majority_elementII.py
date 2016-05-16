def majorityElementII(nums):
    res = []
    for num in set(nums):
        if nums.count(num) > len(nums)/3:
            res.append(num)
        
    return res

print majorityElementII([2,2,2,3,3,1])