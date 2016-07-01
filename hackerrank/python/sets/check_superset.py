A = set(map(int, raw_input().strip().split())) 
N = int(raw_input()) 
lst = []
for i in range(N):
    lst.append(A.issuperset(set(map(int, raw_input().strip().split()))))

if False in lst:
    print False 
else:
    print True