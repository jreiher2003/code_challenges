def plus_minus(nums):
    plus = 0.
    zero = 0.
    minus = 0.
    for n in nums:
        if n == 0:
            zero += 1
        if n > 0:
            plus += 1
        elif n < 0:
            minus += 1
    # print plus,minus,zero
    print plus/len(nums)
    print minus/len(nums)
    print zero/len(nums)

lst = [-4,3,-9,0,4,1]
plus_minus(lst)