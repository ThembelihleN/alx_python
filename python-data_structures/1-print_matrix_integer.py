#my_list = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]
#my_list = [[i for i in range(3)] for _ in range(3)]
#def print_matrix_integer(matrix=[[]]):
   # matrix = ", ".join(x for x in my_list)
   # print("{:d}{:d}{:d}$".format((matrix)))

def print_matrix_integer(matrix=[[]]):
    # if matrix is empty, just print an empty line and return 
    if not matrix:
        print()
        return
    # iterate over each row in the matrix
    for row in matrix:
        # if row is empty print a new line and skip to next row 
        if not row:
            print()
            continue
        # iterate over each element in row using enumerate
        for i, num in enumerate(row):
            # if it is the last element in row print element folowed by a new line 
            if i == len(row) -1:
                print("{:d}".format(num))
            # else if it is not the last print element followed by a space
            else:
                print("{:d}".format(num), end=" ")