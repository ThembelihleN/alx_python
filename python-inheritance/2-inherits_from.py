"""
module description
"""

def is_same_class(obj, a_class):
    """
    function description
    """
    obj_class = type(obj)
    if issubclass(obj_class, a_class) and obj is not a_class:
        return True
    else:
        return False
    
#a = True
#print(is_same_class(a, bool))