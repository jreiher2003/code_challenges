
lst = ['abcdefg']

def reverse1(string):
    begin = 0 
    end = len(string) - 1
    strlst = [i for i in string]
    while(begin < end):
       begin, end = 0, len(string)-1
       begin +=1
       end -= 1
    return ''.join(strlst)

def reverse(string):
    return ''.join(string[i] for i in xrange(len(string) - 1, -1, -1))
# print reverse('abcdefg')

# print ''.join(letter for letter in reversed('practice makes perfect'.split(' ')))


def real_reverse(str1):
    splitted = str1.split()
    reverse = splitted[::-1]
    result = " ".join(reverse)
    return result

str2 = "practice makes perfect"
# print list(str2)
# print real_reverse(str2)


lst1 = 'practice makes purfect'
lst1 = lst1.split()
x = lst1[::-1]
# print " ".join(x)
# print "".join

lst2 = 'practice makes purfect'
lst2 = list(lst2)
# print lst2 
var1 = "".join(lst2)
var2 = var1.split()
var2 = " ".join(var2[::-1])
# var3 = " ".join(var2)

print var2