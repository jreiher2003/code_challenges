T= 1
rows = 5
matrix = [
["e","b","a","c","d"],
["f","g","h","i","j"],
["o","l","m","k","n"],
["t","r","p","q","s"],
["x","y","w","u","v"]
]
import numpy as np 
arr = np.array(matrix)

def grid_challenge(m):
    row_m = []
    col_m = []
    for row in m:
        row_m.append(sorted(row))
    for row in row_m:
        print row
    print "%%%%%%%%%%space"
    ci = zip(*m)
    for i in ci:
        col_m.append(sorted(i))
    for col in col_m:
        print col

print grid_challenge(matrix)