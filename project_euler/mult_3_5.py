def multiple_3_5(n):
	x = 0
	for i in range(n):
		if i % 5 == 0 or i % 3 == 0:
			x += i
	return x
	
 
print multiple_3_5(10)
print multiple_3_5(1000)