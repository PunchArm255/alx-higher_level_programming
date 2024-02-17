#!/usr/bin/python3
"""
This is 'square' module.
Functions and Classes:
    class Square(Rectangle)
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    rep morba3
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        update instance's attributes
        """
        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.size = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]
        elif kwargs:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """
        ret dic instance
        """
        my_dict = {}
        for attr in dir(self):
            condition_1 = not attr.startswith("_")
            condition_2 = not callable(getattr(self, attr))
            condition_3 = (attr != "width") and (attr != "height")
            if condition_1 and condition_2 and condition_3:
                my_dict[attr] = getattr(self, attr)

        return my_dict

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)
