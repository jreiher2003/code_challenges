

E = 100 
num_c = 8
k = 2
clouds = [0,0,1,0,0,1,1,0]

ii = 0
xx = 0
for i in range(len(clouds)):
    if i % k == 0:
        print i, clouds[i]
        if clouds[i] == 0:
            ii += 1
        if clouds[i] == 1:
            xx += 3
E = E - (ii + xx)
print E