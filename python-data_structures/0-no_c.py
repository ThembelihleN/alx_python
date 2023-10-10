#string = "Holberton School"
#print(string.translate({ord('c'): None}))
#print(string.replace('c', ''))
"""
def no_c(my_string):
    new_string = print(my_string.translate({ord(i):None for i in 'Cc'}))
    return new_string


no_c("Holberton School")"""

def no_c(my_string):
    # create a cariable that hold the new string
    new_string = ""
    # use a for loop to iterate over my_string
    for char in my_string:
        #check if each iteration is a c or C by checking the lower case form
        if char.lower() != "c":
            # if char.lower is not c add the iteration char to the new string variable
            new_string += char
    # return the new string
    return new_string