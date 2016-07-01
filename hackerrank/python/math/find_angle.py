import math
a = 10
b = 10
c = math.sqrt(a**2 + b**2)/2
A = (b*b+a*a-c*c)/(2*a*b)

print math.acos(A)*(180/math.pi)

# angle = math.cos(c/10.0)
# angle_to_degrees = math.degrees(angle)
# print angle_to_degrees


AB = 10
BC = 10 
print str(int(round(math.degrees(math.atan2(AB,BC)))))+'°'