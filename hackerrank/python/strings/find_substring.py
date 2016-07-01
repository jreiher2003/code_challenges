import string 

def find_string(s, sub):
    return string.find(s, sub)

print find_string("ABCDCDC", "CDC")

s = "ABCDCDC"
ss = "CDC"
results = 0 
for i in range(len(s)):
    if s[i:(i+len(ss))] == ss:
        results += 1
print results

results = sum([s[i:(i+len(ss))] == ss for i in range(len(s))])

print results