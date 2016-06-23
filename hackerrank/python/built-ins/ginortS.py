def sorting(s):
	"""All sorted lowercase ahead of uppercase
	uppercase letters ahead of digits 
	odd digits before even digits
	"""
	lower = "".join(sorted([x for x in s if x.islower()]))
	upper = "".join([x for x in s if x.isupper()])
	even = "".join([x for x in s if x.isdigit() and int(x) % 2 ==0])
	odd = "".join([x for x in s if x.isdigit() and int(x) % 2 ==1])
	print lower + upper + odd + even


print sorting("Sorting1234")
#>>> ginortS1324 

def sorting_filter(s):
	s = sorted(s)
	num = list(filter(lambda x: x.isdigit(),s))
	even = filter(lambda x: int(x) % 2 ==0, num)
	odd = filter(lambda x: int(x) % 2 ==1, num)
	lower = list(filter(lambda x: x.islower(),s))
	upper = list(filter(lambda x: x.isupper(),s))
	con = lower+upper+odd+even
	print reduce(lambda x,y: x+y, con)

print sorting_filter("1qaz2wsx3edc4rfv5tgb6yhn7ujm8ik9ol0pQWERTYUIOPASDFGHJKLZXCVBNM")