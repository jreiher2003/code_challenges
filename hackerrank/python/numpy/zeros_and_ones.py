import numpy

print numpy.zeros((1,2))                    #Default type is float
#Output : [[ 0.  0.]] 

print numpy.zeros((1,2), dtype = numpy.int) #Type changes to int
#Output : [[0 0]]

import numpy

print numpy.ones((1,2))                    #Default type is float
#Output : [[ 1.  1.]] 

print numpy.ones((2,2,2), dtype = numpy.int) #Type changes to int
#Output : [[1 1]]   

print numpy.zeros((row,col,p),dtype=numpy.int)
print numpy.ones((row,col,p),dtype=numpy.int)

import numpy
N = tuple(map(int, raw_input().strip().split()))

print numpy.zeros(N, dtype=numpy.int)
print numpy.ones(N, dtype=numpy.int)