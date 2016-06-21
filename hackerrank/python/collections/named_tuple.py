from collections import namedtuple 

Point = namedtuple('Point', 'x, y')

pt1 = Point(1,2)
pt2 = Point(3,4)

dop_product = ( pt1.x * pt2.x ) + ( pt1.y * pt2.y )
print dop_product

avg = namedtuple('Avg', 'ID, MARKS, NAME, CLASS')
raymond = avg(1,97,"Raymond",7)
print raymond.MARKS

from collections import namedtuple 
N = int(raw_input()) 
avg = 0
Student = namedtuple('Student', raw_input().strip().split())
for i in range(N): 
    x = Student._make(raw_input().strip().split())
    avg += int(x.MARKS) 
avg1 = float(avg)/N 
print "{0:.2f}".format(avg1)