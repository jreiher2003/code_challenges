def tri_quest(n):
    for i in range(1, n+1):
        print "".join(str(i) * i)
        print "".join(str(((10**i-1)/9)**2))


print tri_quest(5)