def alpha(n):
    abc = map(chr, range(ord('a'),ord('z')+1))
    for i in range(n - 1, 0, -1):
        row = ["-"] * (n * 2 - 1)
        for j in range(0, n - i):
            row[n - 1 - j] = abc[j + i]
            row[n - 1 + j] = abc[j + i]
        print("-".join(row))

    for i in range(0, n):
        row = ["-"] * (n * 2 - 1)
        for j in range(0, n - i):
            row[n - 1 - j] = abc[j + i]
            row[n - 1 + j] = abc[j + i]
        print("-".join(row))

print alpha(3)