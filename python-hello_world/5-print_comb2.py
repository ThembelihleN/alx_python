#n = range(0,100)
for x in range(0,100):
    if x < 10:
        print("0{},".format(x))
    else:
        print("{},".format(x))
