#n = range(0,100)

for x in range(100):
    if x == 99:
        print("{:02d},".format(x), end="\n")
    else:
        print("{:02d},".format(x), end=", ")

