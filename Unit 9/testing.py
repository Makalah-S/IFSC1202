a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for i in range(len(a)): ##which list you're in, starts with 0 (x)
    for j in range(len(a[i])): ##which item within that list you're at, starts with 0 (y)
        print(a[i][j], end=' ')
    print()

print(a[0][3])
print(a[1][0])

##i = row
##j = coloum