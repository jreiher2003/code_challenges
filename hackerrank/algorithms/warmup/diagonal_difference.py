#!/bin/python

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)
    L_R = [ a[i][i] for i in range(len(a)) ]
    R_L = [ row[-i-1] for i ,row in enumerate(a) ]
  
print abs(sum(L_R) - sum(R_L))



import numpy as np  

lst = [[11,2,4], [4,5,6], [10,8,-12]]
arr = np.array(lst)
arr1 = np.array(lst[::-1])
lr = np.trace(arr, offset=0,)
rl = np.trace(arr1)
print abs(lr-rl)