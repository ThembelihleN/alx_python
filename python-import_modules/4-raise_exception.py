def raise_exception():
    print("")
try:
    raise_exception()
except TypeError as te:
    print("Exception raised")