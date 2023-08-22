def no_c(my_string):
    new_string = "".join(c for c in my_string if c.isalpha())
    print(new_string)


print("Holberton School")
print("Chicago")
print("C is fun!")