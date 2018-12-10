fname = input("Enter a file name:")
word = input("Enter the string to be removed:")

lt = []
f = open(fname, 'r')

for l in f.readlines():
    l = l.replace(word, "")
    lt.append(l)

f.close()

f = open(fname, 'w')

for l in lt:
    f.write(l)

f.close()
