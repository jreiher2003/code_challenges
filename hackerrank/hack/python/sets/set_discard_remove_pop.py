s = set([7, 2, 3, 4, 5, 6, 1, 8, 9])
s.remove(5)
print s
#set([1, 2, 3, 4, 6, 7, 8, 9])
print s.remove(4)
#None
print s
#set([1, 2, 3, 6, 7, 8, 9])
#s.remove(0)
#KeyError: 0
s.pop()
print s
x = s.pop()
print x
print s.add(x)
print s
z = s.pop()
print z
print s