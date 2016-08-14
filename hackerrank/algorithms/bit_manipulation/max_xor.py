

def trythis(a,b):
    r = 0
    while (a | r) != (b | r):
        r = (r << 1) + 1
    return r 

print trythis(10,15)