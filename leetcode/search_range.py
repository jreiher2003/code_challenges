def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    lst = []
    for i, n in enumerate(nums):
        print i,n
        if n == target:
            lst.append(i)
    if not lst:
        return [-1,-1]
    else:
        if len(lst) == 1:
            lst.append(lst[0])
            return lst 
        elif len(lst) > 2:
            return [lst[0], lst[-1]]
    return lst

nums = [1]
target = 0
print searchRange(nums, target)