#all possible different combinations of two digits
'''
for i in range(0,90):
    for x in range(0,90):
        if x < 10:
            print("0{},".format(x), end=" ")
        elif x == 89:
            print("{}".format(x))
        else:
            print("{},".format(x), end=" ")
'''

for i in range(10):
    for j in range(i +1, 10):
        if i == 8 and j == 9:
            print("{}{}".format(i, j), end="\n")
        else:
            print("{}{}".format(i, j), end=", ")