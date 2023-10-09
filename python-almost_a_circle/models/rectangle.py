"""
Module documentation
"""
from base import Base

class Rectangle(Base):
    """
    class documentation
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize the Rectangle instance with specified attributes.
        """
        super().__init__(id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height
            

        """
        arguments documentation
        """
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

    def area(self):
        """Area method: returns width * height"""
        return self.__width * self.__height
    
    def display(self):
        """Display the rectangle using char #."""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)
    
    def __str__(self):
        """Returns a formatted output."""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height))
    
    def update(self, *args, **kwargs):
        """Update attributes using *args."""
        if args and len(args) > 0:
            self.id = args[0]
        if args and len(args) > 1:
            self.width = args[1]
        if args and len(args) > 2:
            self.height = args[2]
        if args and len(args) > 3:
            self.x = args[3]
        if args and len(args) > 4:
             self.y = args[4]
        
        """Another documentation"""
        for key, value in kwargs.items():
            if key == "id":
                self.id = value
            elif key == "width":
                self.width = value
            elif key == "height":
                self.height = value
            elif key == "x":
                self.x = value
            elif key == "y":
                self.y = value