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