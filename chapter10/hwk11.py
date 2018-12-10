def sumColumn(m, columnIndex):
    s = 0
    for i in range(3):
        s += m[i][columnIndex]
    # returning s
    return s


a = []
for i in range(3):
    print("Enter a 3-by-4 matrix row for row " + str(i) + ":", end="")
    a.append([])
    x = input()
    x = x.split(" ")
    for j in range(4):
        a[i].append(float(x[j]))
print(a)

for i in range(4):
    total = sumColumn(a, i)
    print("Sum of the elements for column", i, "is", total)
