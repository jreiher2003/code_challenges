#!/bin/python

import sys
import re

lst = []
N = int(raw_input().strip())
for a0 in xrange(N):
    
    firstName,emailID = raw_input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]
    domain = re.search("[\w.]+@gmail.com", emailID)
    if domain != None:
        lst.append(firstName) 

b = sorted(lst)
for i in b:
    print i