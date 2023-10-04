#Write a function that divides 2 integers and prints the resuts.
#a = 12
#b = 2

def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
    """if a and b == 0:
        return None
    elif a or b == 0:
        return None
    else:
        return result
    
    
try:
    result = a/b
    print("Inside result: {}.".format(result))

except:
     print("Error: Denominator cannot be 0.")

finally:
    result = safe_print_division(a, b)
    print("{} / {} = {}".format(a, b, result))

"""