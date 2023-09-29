"""
module documentation
"""
from base import Base

class Rectangle(Base):
    """
    class documentation
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
      """
      getter documentation
      """
      return self.__width
    
    @width.setter
    def width(self, value):
       """"
       setter documentation
       """
       self.__width = value

    @property
    def height(self):
        """
        getter documentation
        """
        return self.__height

    @height.setter
    def height(self, value):
        """"
        setter documentation
        """
        self.__height = value

    @property
    def x(self):
      """
      getter documentation
      """
      return self.__x
    
    @width.setter
    def x(self, value):
       """"
       setter documentation
       """
       self.__x = value

    @property
    def y(self):
      """
      getter documentation
      """
      return self.__y
    
    @width.setter
    def y(self, value):
       """"
       setter documentation
       """
       self.__y = value