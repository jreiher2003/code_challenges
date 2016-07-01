#The poly tool returns the coefficients of a polynomial with the given sequence of roots.
print numpy.poly([-1, 1, 1, 10])        #Output : [  1 -11   9  11 -10]

#The roots tool returns the roots of a polynomial with the given coefficients.
print numpy.roots([1, 0, -1])           #Output : [-1.  1.]