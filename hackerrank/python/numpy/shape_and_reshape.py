import numpy

my_1D_array = numpy.array([1, 2, 3, 4, 5])
print my_1D_array.shape     #(5,) -> 5 rows and 0 columns

my_2D_array = numpy.array([[1, 2],[3, 4],[6,5]])
print my_2D_array.shape     #(3, 2) -> 3 rows and 2 columns


#shape an array alters current array
change_array = numpy.array([1,2,3,4,5,6])
change_array.shape = (3, 2)
print change_array      

# reshape an array creates new array without altering current.
my_array = numpy.array([1,2,3,4,5,6])
print numpy.reshape(my_array,(3,2))