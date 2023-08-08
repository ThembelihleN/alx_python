#Write a function that divides 2 integers and prints the result

def safe_print_division(a, b):
    if a and b == 0:
        return None
    elif a or b == 0:
        return None
    else:
        return result
try:
    a = 12
    b = 2

except:
    print("Inside result: None")

finally:
    result = safe_print_division(a, b)
    print("Inside result: {} / {} = {}".format(a, b, result))