from collections import Counter

# word = "aabbbccde" 
word = "abc"
string = sorted(Counter(word).items(), key= lambda x: (-x[1],x[0]))[:3]
print("\n".join(x[0]+" "+str(x[1]) for x in string))
# for i, k in c:
#     print i,k

