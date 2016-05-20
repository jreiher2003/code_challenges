

def iter_palidrome(s):
	for i in range(len(s)/2):
		if s[i] != s[-(i+1)]:
			return False
	return True

print iter_palidrome('abba')
print iter_palidrome('jeeefeeej')
print iter_palidrome("")
print iter_palidrome("jeff")