"""
module description
"""

def is_same_class(obj, a_class):
    """
    function description
    """
    if obj.__class__.__name__ == a_class.__name__ or isinstance(obj, a_class):
        return True
    else:
        return False
    
#a = 1
#print(float.__name__)