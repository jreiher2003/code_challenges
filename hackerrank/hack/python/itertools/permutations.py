from itertools import permutations 
import textwrap

print list(permutations(["1", "2", "3"]))
print list(permutations([1, 2, 3]))


def perm(s, k):
    lst = []
    for letter in s:
        lst.append(letter)
    permy = sorted(list(permutations(lst, k)))
    for p in permy:
        print "".join(p)
    # print textwrap.fill("".join(["".join(p) for p in sorted(list(permutations(lst, k)))]),2)
print perm("HACK", 2)