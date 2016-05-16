def tile_to_number(excel_num):
    lst = map(chr, xrange(ord('A'), ord('Z')+1))
    new_list = []
    k = True
    while k:
        for e,i in enumerate(lst, start=1):
        #     lst += [i + x for x in lst if i == 'A']
            for x in lst:
                for i in lst:
                    new_list.append((i+x))
        lst += new_list    
        return lst[excel_num -1]
    return False

# print tile_to_number(17500)

# def title(s):
def convertToTitle(n):
    """
    :type n: int
    :rtype: str
    """
    res = ''
    base = ord('A')
    while n > 0:
        n, r = divmod(n - 1, 26)
        print n,r
        print base + r,chr(base+r), res
        res = '{}{}'.format(chr(base + r), res)
    return res

# print convertToTitle(17500)

def convert_2_tile(n):
    A_Z = map(chr, range(ord('A'), ord('Z')+1))
    print A_Z
    new_list = []
    while n:
        a = (n-1)%26
        new_list.append(A_Z[a])
        n =(n-1)/26
    return "".join(new_list[::-1])

print convert_2_tile(100000)
print divmod(16,2)


