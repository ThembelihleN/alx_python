"""
module description
"""

class BaseGeometry:
    """
    class description
    """
    def __dir__(self):
        attributes = super().__dir__()
        return [i for i in attributes if i != '__init_subclass__']
    
    def area(self):
        raise Exception('area() is not implemented')