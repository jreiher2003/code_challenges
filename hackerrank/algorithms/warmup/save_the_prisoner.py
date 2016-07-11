from itertools import cycle 
T = int(raw_input())

def last_person(N,M,S):
    ans = (S + (M % N) -1) % N
    if ans == 0:
        print N
    else:
        print ans

i = 0 
while i <= T:
    N,M,S = map(int, raw_input().strip().split())
    last_person(N,M,S)
    i += 1