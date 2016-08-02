

def game(stones):
    if stones % 7 > 1:
        return "First"
    else:
        return "Second"


# print game(1)
# print game(2)
# print game(3)
# print game(4)
# print game(5)
# print game(6)
# print game(7)
# print game(10)
# print game()
for i in range(1,101):
    print game(i)
