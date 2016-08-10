
def test_lst(l):
    lst = []
    for i in range(len(l)):
        if sum(l[:i]) == sum(l[(i+1):]):
            lst.append("YES")
        else:
            lst.append("NO")
    if "YES" in lst:
        return "YES"
    else:
        return "NO"
       


l_t = [1]
print test_lst(l_t)