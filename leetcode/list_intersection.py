


def intersection(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    return set(nums1).intersection(set(nums2))

def intersection2(nums1, nums2):
    count = []
    for num in nums1:
        if num in nums2:
            nums2.remove(num)
            count.append(num)
    return count


a = [1,2,2,1]
b = [2,2]
c = [2]
print intersection(a,b)
print intersection2(a,b)
print intersection2(a,c)