f = open("test.csv","rU")
d = {}
for line in f:
    print line.split(",")
f.close()
