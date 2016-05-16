def reverse_vowels(string):
    string = list(string)
    new_string = []
    for i in string:
        if i.isupper():
            new_string.append((i,True))
        else:
            new_string.append((i,False))
    lst_v =[]
    for index, v in enumerate(new_string):
        if v[0] in "aeiouyAEIOUY":
            # lst_v.append((index,v))
            lst_v.append((index,v[0],v[1]))
    pos, vowel, case = [x[0] for x in lst_v], [x[1] for x in lst_v], [x[2] for x in lst_v]
    vowel.reverse()
    lst_v_r = zip(pos, vowel, case)
    for index, v, case in lst_v_r:
        if case == False:
            string[index] = v.lower()
        else:
            string[index] = v.upper()
   
    return "".join(string)


print reverse_vowels("aA")
# v = "J"
# print v.isupper()

def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """
    lst = list(s)
    vowels_str = "aeiouAEIOU"
    vowels_list = [item for item in lst if item in vowels_str]
    vowels_list.reverse()
    vowels_index = 0
    for index, item in enumerate(lst):
        if item in vowels_str:
            lst[index] = vowels_list[vowels_index]
            vowels_index += 1
    return ''.join(lst)

print reverseVowels("aA")
print reverseVowels("JEffryi")