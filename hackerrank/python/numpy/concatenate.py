import numpy

array_1 = numpy.array([1,2,3])
array_2 = numpy.array([4,5,6])
array_3 = numpy.array([7,8,9])

print numpy.concatenate((array_1, array_2, array_3))    

import numpy

array_1 = numpy.array([[1,2,3],[0,0,1]])
array_2 = numpy.array([[0,0,0],[7,8,9]])

# row = 0 col = 1
print numpy.concatenate((array_1, array_2), axis = 0) 