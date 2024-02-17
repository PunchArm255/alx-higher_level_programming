import unittest

from models.square import Square

class TestSquare(unittest.TestCase):

    def test_type(self):
        a = Square(5)
        b = Square(20, 0, 2, 3033030)
        c = Square(id=77, size=90)

        l = [a, b, c]
        for i in l:
            self.assertIsInstance(i, Square)

    def test_assign(self):
        a = Square(1, id=900)
        a.id = 800
        a.size = 100
        self.assertEqual(a.id, 800)
        self.assertEqual(a.size, 100)

    def test_exception(self):
        with self.assertRaises(TypeError):
            a = Square("0")
        with self.assertRaises(TypeError):
            a = Square("-20")
        with self.assertRaises(ValueError):
            a = Square(0)
        with self.assertRaises(ValueError):
            a = Square(-7)
        with self.assertRaises(ValueError):
            a = Square(1, y=-6, x=-1)

    def test_update(self):
        a = Square(100)
        self.assertEqual(a.size, 100)
        self.assertEqual(a.height, 100)
        self.assertEqual(a.y, 0)
        a.update(3)
        self.assertEqual(a.id, 3)
        a.update(5, size=19)
        self.assertNotEqual(a.size, 19)
        a.update(y=4, size=4)
        self.assertEqual(a.y, 4)
        self.assertEqual(a.size, 4)

    def test_dict(self):
        a = Square(1, 300, 4000, 50000)
        d = a.to_dictionary()
        tmp = {'size': 1, 'x': 300, 'y': 4000, 'id': 50000}
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
