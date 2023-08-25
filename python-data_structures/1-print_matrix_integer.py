#my_list = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]
my_list = [[i for i in range(3)] for _ in range(3)]
def print_matrix_integer(matrix=[[]]):
    matrix = ", ".join(str(x) for x in my_list)
    print("{:d}{:d}{:d}$".format((matrix)))


#my_list = [1, 2, 3]
#my_string = ", ".join(str(x) for x in my_list)
#print("My list contains: {}".format(my_string))
#print_matrix_integer(matrix)