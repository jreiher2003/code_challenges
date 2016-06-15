def minion(s, k_ss, s_ss):
    st = 0
    k = 0
    
    for i in range(len(s)):
        for word in k_ss:
            if s[i:i+len(word)] == word:
                k += 1
    for i in range(len(s)):
        for w in s_ss:
            if s[i:i+len(w)] == w:
                st += 1
    
    if st > k:
        print "Stuart", st 
    else:
        print "Kevin", k


word = "BANANA"
kevin_words = ["A", "AN", "ANA", "ANAN", "ANANA"]
stu_words = ["B","N","BA","NA","BAN","NAN","BANA","NANA","BANAN","BANANA"]
print minion(word, kevin_words, stu_words)