import unittest
from main import Operator

class TestOperator(unittest.TestCase):
    example = Operator(4, 2)
    def test_one(self):
        self.assertEqual(self.example.adding(), 6)

    def test_two(self):
        self.assertEqual(self.example.subtracting(), 2)

