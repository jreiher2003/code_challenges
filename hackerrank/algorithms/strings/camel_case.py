def camelcase(s):
    nl = list(s)
    cnt = 1
    # for letter in nl:
    #     if letter.isupper():
    #         cnt += 1
    # return cnt
    return len([letter for letter in nl if letter.isupper()]) + 1



 
print camelcase("saveChangesInTheEditor")