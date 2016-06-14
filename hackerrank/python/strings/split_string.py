def split_join(S):
    S = S.split()
    return "-".join(S)
    

print split_join("this is a string")