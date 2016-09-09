

def kangaroo(x1,v1,x2,v2):
    x = x1
    xx = x2 
    if v2 >= v1:
        print "NO"
    while x1 < x2:
        x += v1
        xx += v2
        if x == xx:
            print "YES"
    print "NO"



# print kangaroo(0,3,4,2)
print kangaroo(0,2,5,3)


if (x1 > x2 and v1 > v2) or (x2 > x1 and v2 > v1) or (v1 == v2):
    print("NO")
else:
    print(["NO","YES"][abs(x1-x2)%abs(v1-v2) == 0])