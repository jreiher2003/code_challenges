# print zip([1,2,3,4,5,6],"Hacker")
# print zip([1,2,3,4,5,6],[0,9,8,7,6,5,4,3,2,1])
# print zip([0,9,8,7,6,5,4,3,2,1], [1,2,3,4,5,6])
# print "\n"
A = [1,2,3]
B = [6,5,4]
C = [7,8,9]
X = [A] + [B] + [C]

# print X
# print "\n"
# print zip(*X)
sub1 = [89,90,78,93,80]
sub2 = [90,91,85,88,86]
sub3 = [91,92,83,89,90.5]
N = [sub1] + [sub2] + [sub3]
# print N
# S = zip(*N)
# for x in S:
#     print sum(x)/len(x)

# n,x = input().split(' ') 
mark_lists = list([int(i) for i in range(len(N))]) 
mark_list1 = map(tuple, N)
print mark_list1
# student_col = [list(zip(*mark_lists)) for i in range(len(student_col))]
student_col = zip(*N)
print(sum(student_col[i])/len(student_col[i]))


scores = []
n, x = map(int, input().split())
for i in range(x):
    scores.append(list(map(float, input().split())))
print(*[sum(student)/len(student) for student in zip(*scores)],sep='\n')

n,x = raw_input().split() 
n,x = map(int, n)[0], map(int, x)[0]
#print n,x
s = []
for i in range(x):
    s += [raw_input().split()]

    
int_list = []
for i in s:
    int_list += [map(float,i)]

print int_list
   
N = zip(*int_list)
print N
for i in N:
    print (sum(i)/len(i))



#### right anwser that passes
numsub, numstu = map(int, raw_input().split())
rows = [map(float, raw_input().split()) for row in range(numstu)]
for average in  map(lambda row: reduce(lambda x,y: x+y, row)/numstu, zip(*rows)):
    print average