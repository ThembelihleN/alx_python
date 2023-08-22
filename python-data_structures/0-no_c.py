#string = "Holberton School"
#print(string.translate({ord('c'): None}))
#print(string.replace('c', ''))
def no_c(my_string):
    new_string = print(my_string.translate({ord('c'): None}))
    return new_string
  
no_c("Holberton School")
#print("Chicago")
#print("C is fun!")