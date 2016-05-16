

def removeElement(nums, val):
    return [x for x in nums if x != val]

nums = [3,2,2,3]
val = 3
print removeElement(nums, val)