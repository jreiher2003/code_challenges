def remove_dups(nums):
    """ uses set to remove dups from list"""
    nums[:] = sorted(list(set(nums)))
    return nums