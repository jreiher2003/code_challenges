def reverse_vowels(str_):
    """
    Given a string, returns a string with the order of the vowels reversed but all other chars 
    unchanged
    """
    tmp = list(str_)
    positions_and_vowels = [(index, char) for index, char in enumerate(tmp) if char in 'aeiouyAEIOUY']
    positions, vowels = [x[0] for x in positions_and_vowels], [x[1] for x in positions_and_vowels]
    vowels.reverse()
    for index, char in zip(positions, vowels):
        tmp[index] = char
    return "".join(tmp)
    # return tmp

print reverse_vowels("ilovepussY")
