from collections import Counter 

myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
# print Counter(myList)
# print Counter(myList).items()
# print Counter(myList).keys()
# print Counter(myList).values()

def count_shoes(lst, shoe_size):
    numShoes = len(lst) 
    shoes = Counter(lst) 
    custys = 6 
    price = 0 
    for i in range(custys):
        # size, prices = list([6,45])
        if shoes[shoe_size]:
            # price += prices
            shoes[shoe_size] -= 1
    return price,shoes


LST = [2,3,4,5,6,8,7,6,5,18]
print count_shoes(LST,6)
