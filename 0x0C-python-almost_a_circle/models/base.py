#!/usr/bin/python3
"""
This is 'base' module.
Functions and Classes:
    class Base()
"""


class Base():
    """
    Base class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        ret the JSON string representation of list_dictionaries
        """
        import json

        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """
        input the JSON string representation of list_objs to a file
        """
        filename = cls.__name__ + ".json"
        my_list = []

        if list_objs:
            for item in list_objs:
                if isinstance(item, Base):
                    d = item.to_dictionary()
                    my_list.append(d)

        json_s = Base.to_json_string(my_list)
        with open(filename, "w", encoding="UTF-8") as f:
            f.write(json_s)

    @staticmethod
    def from_json_string(json_string):
        """
        ret list of JSON string rep of json_string
        """
        import json

        if json_string:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """
        ret insta of all atrrtiii
        """
        from models.square import Square

        if dictionary:

            # initialize a dummy instance
            if cls is Base:
                tmp = cls()
            elif cls is Square:
                tmp = cls(1)
            else:
                tmp = cls(1, 1)  # Rectangle

            if isinstance(tmp, Base):
                tmp.update(**dictionary)
            return tmp

    @classmethod
    def load_from_file(cls):
        """
        ret list of insta
        """
        my_list = []

        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r", encoding="UTF-8") as f:
                content = f.read()
        except FileNotFoundError:
            return my_list

        json_list = Base.from_json_string(content)
        if json_list:
            for d in json_list:
                my_list.append(cls.create(**d))

        return my_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        input csv listobjs to file
        """
        import csv

        filename = cls.__name__ + ".csv"
        my_list = []
        for item in list_objs:
            if isinstance(item, Base):
                d = item.to_dictionary()
                my_list.append(d)

        with open(filename, "w", encoding="UTF-8", newline="") as f:
            f_csv = csv.writer(f)

            for d in my_list:
                if "size" in d.keys():
                    f_csv.writerow([d['id'], d['size'], d['x'], d['y']])
                else:
                    f_csv.writerow([d['id'], d['width'],
                                   d['height'], d['x'], d['y']])

    @classmethod
    def load_from_file_csv(cls):
        """
        ret tabla of instagram
        """
        import csv

        filename = cls.__name__ + ".csv"
        keys = ["id", "x", "y"]
        if filename == "Rectangle.csv":
            keys.insert(1, "width")
            keys.insert(2, "height")
        else:
            keys.insert(1, "size")

        my_list = []
        dicts = []
        try:
            with open(filename, "r", encoding="UTF-8", newline="") as f:
                f_csv = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

                for row in f_csv:
                    d = {}
                    index = 0
                    for attribute in keys:
                        d[attribute] = int(row[index])
                        index += 1
                    dicts.append(d)
        except FileNotFoundError:
            return my_list

        for d in dicts:
            my_list.append(cls.create(**d))

        return my_list
