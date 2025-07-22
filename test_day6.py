
import unittest
from day6 import redistribute, num_redistributions

class TestDay6(unittest.TestCase):
    def test_redistribute(self):
        self.assertEqual(redistribute([0, 2, 7, 0]), [2, 4, 1, 2])
        self.assertEqual(redistribute([2, 4, 1, 2]), [3, 1, 2, 3])
        self.assertEqual(redistribute([3, 1, 2, 3]), [0, 2, 3, 4])

    def test_num_redistributions(self):
        # Test with small input
        cycle_length, iterations = num_redistributions([0, 2, 7, 0])
        self.assertEqual(cycle_length, 4)
        self.assertEqual(iterations, 5)

        # Test with larger input
        cycle_length, iterations = num_redistributions([4, 1, 15, 12, 0, 9, 9, 5, 5, 8, 7, 3, 14, 5, 12, 3])
        self.assertGreater(cycle_length, 0)
        self.assertGreater(iterations, 0)

if __name__ == '__main__':
    unittest.main()
