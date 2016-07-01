import textwrap 

string = "This is a very very very very very very very long string."
print textwrap.wrap(string, 8)

print textwrap.fill(string, 8)

abc = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
print textwrap.fill(abc, 4)