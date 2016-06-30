# Transpose
# We can generate the transposition of an array using the tool numpy.transpose. It will not affect the original array, but it will create a new array.  It flips rows, cols ie (2,3) to a (3,2)  
import numpy

my_array = numpy.array([[1,2,3],
                        [4,5,6]])
print numpy.transpose(my_array)

#Flatten
#The tool flatten creates a copy of the input array flattened to one dimension.  
my_array = numpy.array([[1,2,3],
                        [4,5,6]])
print my_array.flatten()
print my_array