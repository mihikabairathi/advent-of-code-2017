



import unittest
from day16 import perform_dance, simulate_dances

class TestDay16(unittest.TestCase):
    def test_perform_dance(self):
        # Test spin
        self.assertEqual(perform_dance(['a', 'b', 'c', 'd'], ['s1']), ['d', 'a', 'b', 'c'])
        # Test exchange
        self.assertEqual(perform_dance(['a', 'b', 'c', 'd'], ['x0/3']), ['d', 'b', 'c', 'a'])
        # Test partner
        self.assertEqual(perform_dance(['a', 'b', 'c', 'd'], ['pa/b']), ['b', 'a', 'c', 'd'])

    def test_simulate_dances(self):
        # Test with small input
        result = simulate_dances('test_day16_input_fixed.txt', times=2)
        self.assertEqual(len(result), 16)
        self.assertEqual(len(set(result)), 16)  # All unique characters

if __name__ == '__main__':
    unittest.main()



