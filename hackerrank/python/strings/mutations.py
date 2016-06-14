def mutations(s, idx, new):
    s = list(s)
    s[idx] = new
    print "".join(s)


print mutations("abracadabra", 4, "d")