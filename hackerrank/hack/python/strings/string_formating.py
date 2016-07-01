def print_numbers(n):
    for i in range(1,n+1):
        w = len(str(bin(i)).replace('0b',''))
        b = bin(int(i)).replace('0b','').rjust(w, ' ')
        o = oct(int(i)).replace('0','', 1).rjust(w, ' ')
        h = hex(int(i)).replace('0x','').upper().rjust(w, ' ')
        j = str(i).rjust(w, ' ')
        print j, o, h, b

print print_numbers(17)