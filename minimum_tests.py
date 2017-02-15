import unittest
from minimum_effort import minimum_effort


class TestMinimumEffort(unittest.TestCase):

    def test_basic(self):
        """Testing example given in excercise"""
        self.assertEqual(minimum_effort("basic"), '14\n21')

    def test_more_complex(self):
        """Little more complex examples"""
        self.assertEqual(minimum_effort("complex"), '366\n91\n135')

if __name__ == '__main__':
    unittest.main()
