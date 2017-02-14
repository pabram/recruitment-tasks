import unittest
from battle import battle


class TestBattle(unittest.TestCase):
    def setUp(self):
        pass

    def test_basic(self):
        self.assertEqual(battle([1, 2, 3, 4]), "tie")
        self.assertEqual(battle([1, 2, 3, 5]), "odds win")

    def test_negatives(self):
        self.assertEqual(battle([21, -3, 20]), "evens win")
        self.assertEqual(battle([7, -3, -14, 6]), "odds win")
        self.assertEqual(battle([23, -3, 32, -24]), "tie")

    def test_with_zeros(self):
        self.assertEqual(battle([1, 2, 3, 4, 0]), "tie")
        self.assertEqual(battle([0, 7, -3, -14, 6]), "odds win")

if __name__ == '__main__':
    unittest.main()
