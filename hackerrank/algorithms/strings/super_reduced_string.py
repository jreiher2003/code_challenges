def super_reduced(s):
    # s = list(s)
    while True:
        for i in range(len(s)-1):
            if s[i] == s[(i+1)]:

                print s, s[:i], s[i+2:]
                s = s[:i] + s[i+2:]
                break
        else:
            break
                
        
    print s if s else "Empty String"
    

    

print super_reduced('aaabccddd')
print super_reduced("baab")
