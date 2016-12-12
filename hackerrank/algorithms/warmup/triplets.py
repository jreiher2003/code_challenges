

def compare_lists(lst1,lst2):
    alice = 0
    bob = 0 
    for i, x in zip(lst1,lst2):
        if i > x: alice += 1
        if x > i: bob += 1
        if x == i: continue
    print alice,bob

print compare_lists([5,6,7], [3,6,10])
