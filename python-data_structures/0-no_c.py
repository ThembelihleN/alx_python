#string = "Holberton School"
#print(string.translate({ord('c'): None}))
#print(string.replace('c', ''))
def no_c(my_string):
    new_string = print(my_string.translate({ord(i):None for i in 'Cc'}))
    return new_string
  
no_c("Holberton School")
no_c("Chicago")
no_c("C is fun!")