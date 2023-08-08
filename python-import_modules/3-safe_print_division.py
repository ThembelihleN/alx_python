#Write a function that divides 2 integers and prints the result
#if __name__ == "__main__":
#    from variable_load_2 import a

def safe_print_division(a, b):
    #print("{}".format())
    try:
        a = 12
        b = 2
        
    except:
        print("Error: Denominator cannot be 0.")

    finally:
        result = safe_print_division(a, b)
        print("Inside result: {:d} / {:d} = {}".format(a, b, result))