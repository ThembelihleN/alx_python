def no_c(my_string):
    new_string = my_string.translate({ord('c'):None})
    return my_string


print("Holberton School")
print("Chicago")
print("C is fun!")