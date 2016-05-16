def moveZeros(nums):
    c = 0
    for num in nums:
        if num != 0:
            nums[c] = num
            c += 1
    nums[c:] = [0]*(len(nums)-c)
    return nums

nums = [0,1,0,2,12]
print moveZeros(nums)