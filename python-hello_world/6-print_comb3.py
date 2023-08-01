#all possible different combinations of two digits
for i in range(0,90):
    for x in range(0,90):
        if x < 10:
            print("0{},".format(x), end=" ")
        elif x == 89:
            print("{}".format(x))
        else:
            print("{},".format(x), end=" ")