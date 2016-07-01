import re 

try:
	re.compile(raw_input())
	print True 
except re.error:
	print False