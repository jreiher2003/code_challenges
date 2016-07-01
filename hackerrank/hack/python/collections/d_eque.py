from collections import deque 

d = deque()

d.append(1)
d.append(2)
d.append(3)
d.appendleft(4)
d.pop()
d.popleft()

print d