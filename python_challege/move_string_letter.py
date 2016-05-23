from string import maketrans   # Required to call maketrans function.

intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)

str = "this is string example....wow!!!"
print str.translate(trantab)

def shift_letter(string, n):
    new_string = ""
    for letter in string: 
        if ord('a') <= ord(letter) <= ord('z'):
            new_string += chr(((ord(letter) - ord('a') + n) % 26) + ord('a'))
        elif letter == "." or letter == "(" or letter == ")" or letter == " ":
            new_string += letter 
        # else:
        #     new_string += " " 


    return new_string

print shift_letter("map.", 2)