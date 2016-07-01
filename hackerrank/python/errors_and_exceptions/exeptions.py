a = '1'
b = '0'
# print int(a)/int(b)

def ex(a,b):
	try:
		print int(a)/int(b)
	except (ZeroDivisionError,ValueError) as e:
		print "Error Code:",e
	

print ex(1,0)
print ex(2,'$')
print ex(3,1)