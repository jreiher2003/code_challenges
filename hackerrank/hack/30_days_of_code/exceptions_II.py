class Calculator(object):

	def power(self,n,p):
		
		if n < 0 or p < 0:
			raise Exception("n and p should be non-negative.")
		else:
			return n**p
	

mycalc = Calculator()
print mycalc.power(3,4)
print mycalc.power(1, 4)