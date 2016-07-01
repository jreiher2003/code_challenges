def tri_q(n):
    for i in range(1, n+1):
        print sum(map(lambda x: i * 10**x, xrange(i)))

print tri_q(4)