f = open("test.csv","rU")
d = {}
for line in f:
    keyval = line.split(",")
    d[keyval[0]] = keyval[1]
print d
f.close()
