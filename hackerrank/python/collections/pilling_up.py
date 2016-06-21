from collections import deque 

# d = deque([4,3,2,1,3,4])  
d = deque([1,3,2])
i = 0
d_len = (len(d)/2)-1
print i, d_len
while i <= d_len:
    if d[0] >= d[-1]:
        d.popleft()
        d.pop()
        i+=1
        if len(d) == 0:
            print "Yes" 
    else:
        print "No"
        break
        
    
# print d