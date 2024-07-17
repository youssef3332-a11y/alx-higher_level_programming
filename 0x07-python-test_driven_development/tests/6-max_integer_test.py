#!/usr/bin/python3
"""
testing module
.
"""
import unittest
max_integer = __import__('6-max_integer').max_integer
class TestMaxInteger(unittest.TestCase):
    """
    this is a class
    test
    for my method
    """
    def test_max_integer(self):
        self.assertIsNone(max_integer([]))
    def test_isCorret(self):
        self.assertEqual(max_integer([32,56,4,3.5]), 56)
        self.assertEqual(max_integer([32]), 32)
    def test_max_where(self):
        self.assertEqual(max_integer([32, 4, 56, 3, 6]), 56)
        self.assertEqual(max_integer([56, 4, 5, 3, 6]), 56)
        self.assertEqual(max_integer([32, 4, 5, 3, 56]), 56)
    def test_max_negatif(self):
        self.assertEqual(max_integer([-32, -4, -56, -3, -6]), -3)
        self.assertEqual(max_integer([32, -4, 56, 3, 6]), 56)
    