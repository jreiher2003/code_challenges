import itertools


def smallest_substring(arr, string):
    subsets = ["".join(x) for x in itertools.permutations(arr, 3)]
    for i in range(len(string)):
        for subset in subsets:
            if string[i: (i+3)] == subset:
                return string[i:(i+3)]
        





print smallest_substring(['x','y','z'], "xyyzyzyx")
# >>> "zyx"
print smallest_substring(['a','b', 'c'], "ccbbacbb")