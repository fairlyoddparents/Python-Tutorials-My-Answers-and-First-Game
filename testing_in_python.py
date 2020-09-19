import unittest
from unittest import TestCase

"""Simple test, it will just tell me which was the first thing to fail"""
def test_sum():
    assert sum([1,2,3]) == 6, "Should be 6"

def test_sum_tuple():
    assert sum((1, 2, 2)) == 5, "Should be 5"


"""Unittest testing"""
class TestSum(TestCase):
    def test_sum(self):
        self.assertEqual(sum([1,2,3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)),  5, "Should be 5")



if __name__ == "__main__":
    unittest.main()
