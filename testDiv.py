import unittest
from calculator import Calculator


class TestStringMethods(unittest.TestCase):

    def test_sum(self):
        x = Calculator()

        self.assertEqual(x.div(5.5, 5.5), 11)


if __name__ == '__main__':
    unittest.main()