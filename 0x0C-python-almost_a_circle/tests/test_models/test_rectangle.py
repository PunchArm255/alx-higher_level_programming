import unittest

from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_type(self):
        a = Rectangle(10, 20, 1, 3, 100)
        b = Rectangle(10, 20, 33, id=101)
        c = Rectangle(1, 1, id=102)

        l = [a, b, c]
        for i in l:
            self.assertIsInstance(i, Rectangle)

    def test_values(self):
        a = Rectangle(5, 7)
        self.assertEqual(a.width, 5)
        self.assertEqual(a.height, 7)
        self.assertEqual(a.x, 0)
        self.assertEqual(a.y, 0)
        self.assertIsNotNone(a.id)

    def test_exception(self):
        with self.assertRaises(TypeError):
            a = Rectangle()

        with self.assertRaises(TypeError):
            a = Rectangle(8)

    def test_validation(self):
        with self.assertRaises(TypeError):
            a = Rectangle("1", 2, 3, 4)
        with self.assertRaises(TypeError):
            a = Rectangle(1, [2], 3, 4)
        with self.assertRaises(TypeError):
            a = Rectangle(1, 2, 3.0, 4)
        with self.assertRaises(TypeError):
            a = Rectangle(1, 2, 3, {"4": 4})

        with self.assertRaises(ValueError):
            a = Rectangle(0, 2, 3, 4)
        with self.assertRaises(ValueError):
            a = Rectangle(1, 0, 3, 4)
        with self.assertRaises(ValueError):
            a = Rectangle(1, 1, -2, 4)
        with self.assertRaises(ValueError):
            a = Rectangle(3, 1, 2, -4)

    def test_area(self):
        a = Rectangle(10, 11)
        self.assertEqual(a.area(), 110)
        b = Rectangle(1, 1, id=100)
        self.assertEqual(b.area(), 1)
        c = Rectangle(3, 33, 55, 50, 1000)
        self.assertEqual(c.area(), 99)

    def test_update(self):
        a = Rectangle(11, 111)
        self.assertNotEqual(a.id, 10101)
        self.assertNotEqual(a.width, 1)
        self.assertNotEqual(a.height, 2)
        self.assertNotEqual(a.x, 88008)
        self.assertNotEqual(a.y, 123456789)
        a.update(10101)
        self.assertEqual(a.id, 10101)
        a.update(10101, 1)
        self.assertEqual(a.id, 10101)
        self.assertEqual(a.width, 1)
        a.update(10101, 1, 2)
        self.assertEqual(a.height, 2)
        a.update(10101, 1, 2, 88008, 123456789)
        self.assertEqual(a.x, 88008)
        self.assertEqual(a.y, 123456789)
        self.assertEqual(a.id, 10101)
        self.assertEqual(a.width, 1)
        self.assertEqual(a.height, 2)

    def test_update_2(self):
        a = Rectangle(100, 100, id=1000)
        a.update(id=1001)
        self.assertEqual(a.id, 1001)
        a.update(1000, id=1002)
        self.assertEqual(a.id, 1000)
        self.assertNotEqual(a.id, 1002)
        a.update(id=200, x=3, y=4, width=1, height=2)
        self.assertEqual(a.id, 200)
        self.assertEqual(a.width, 1)
        self.assertEqual(a.height, 2)
        self.assertEqual(a.x, 3)
        self.assertEqual(a.y, 4)

    def test_dict(self):
        a = Rectangle(1, 20, 300, 4000, 50000)
        d = a.to_dictionary()
        tmp = {'width': 1, 'height': 20, 'x': 300, 'y': 4000, 'id': 50000}
        self.assertEqual(d, tmp)
        a.update(x=33)
        d = a.to_dictionary()
        tmp['x'] = 33
        self.assertEqual(d, tmp)
        a.update(id=5)
        d = a.to_dictionary()
        self.assertNotEqual(d, tmp)

if __name__ == '__main__':
    unittest.main()
