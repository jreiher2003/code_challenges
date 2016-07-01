def is_prime(num):
	for num in range(2,num):
		prime = True
		for i in range(2,num):
			if num%i == 0:
				# print i 
				prime = False
		if prime:
			print num

# print is_prime(100)

def is_prime2(num):
	return [num for num in range(2,num) for i in range(2,num) if num %i!=0 ]

print is_prime2(100)