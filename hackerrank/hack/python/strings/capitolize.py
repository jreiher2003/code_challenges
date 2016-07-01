def caps_word(S):
    return " ".join([x.title() for x in S.split()])


print caps_word("yo this is a sentace 1")