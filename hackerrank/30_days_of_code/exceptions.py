def string_to_int(s):
    try:
        return int(s)
    except ValueError:
        print "Bad String"


print string_to_int("3")
print string_to_int(0)
print string_to_int("ab")