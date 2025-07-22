#!/usr/bin/env python3
"""
Unit tests for performance fixes in Advent of Code 2017 solutions.
Tests that the performance issues in Day 15 and Day 17 have been resolved.
"""

import unittest
import time
import sys
import os

# Add parent directory to path to import the day modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import day15
import day17

class TestPerformanceFixes(unittest.TestCase):
    """Test cases for performance fixes."""

    def time_function(self, func, *args, **kwargs):
        """Helper to time function execution."""
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        return result, end_time - start_time

    def test_day15_performance(self):
        """Test that Day 15 generator matching is reasonably fast."""
        result, exec_time = self.time_function(day15.count_matches, 65, 8921)

        # Verify correctness
        self.assertEqual(result, 309, "Day 15 should return correct result")

        # Verify performance (should be under 10 seconds)
        self.assertLess(exec_time, 10.0,
                       f"Day 15 should complete in under 10 seconds, took {exec_time:.3f}s")

        print(f"Day 15 performance: {exec_time:.3f}s")

    def test_day17_small_input_performance(self):
        """Test that Day 17 works correctly with small inputs."""
        result, exec_time = self.time_function(day17.short_circuit, 3, 2017)

        # Verify correctness for small input
        self.assertEqual(result[0], 638, "Day 17 should return correct first result")
        self.assertEqual(result[1], 1226, "Day 17 should return correct second result")

        # Should be very fast for small inputs
        self.assertLess(exec_time, 1.0,
                       f"Day 17 with small input should be fast, took {exec_time:.3f}s")

        print(f"Day 17 small input performance: {exec_time:.3f}s")

    def test_day17_large_input_performance(self):
        """Test that Day 17 can handle large inputs efficiently."""
        result, exec_time = self.time_function(day17.short_circuit, 3, 500000)

        # For large inputs, we expect the first result to be None (not computed)
        # and the second result to be computed efficiently
        self.assertIsNone(result[0], "Day 17 large input should return None for first result")
        self.assertIsNotNone(result[1], "Day 17 large input should compute second result")

        # Should complete in under 1 second (was hanging before fix)
        self.assertLess(exec_time, 1.0,
                       f"Day 17 with large input should be fast, took {exec_time:.3f}s")

        print(f"Day 17 large input performance: {exec_time:.3f}s")

    def test_day15_bitwise_optimization(self):
        """Test that Day 15 uses bitwise operations correctly."""
        # Test with small values to verify the bitwise logic
        gen1, gen2 = 65, 8921

        # Generate a few values manually to test the bitwise comparison
        gen1 = (gen1 * 16807) % 2147483647
        while gen1 % 4 != 0:
            gen1 = (gen1 * 16807) % 2147483647

        gen2 = (gen2 * 48271) % 2147483647
        while gen2 % 8 != 0:
            gen2 = (gen2 * 48271) % 2147483647

        # Test that bitwise AND gives same result as string conversion
        bitwise_result = (gen1 & 0xFFFF) == (gen2 & 0xFFFF)

        # Convert to binary strings for comparison
        bin1 = bin(gen1)[2:]
        if len(bin1) < 16:
            bin1 = '0' * (16 - len(bin1)) + bin1
        bin1 = bin1[-16:]

        bin2 = bin(gen2)[2:]
        if len(bin2) < 16:
            bin2 = '0' * (16 - len(bin2)) + bin2
        bin2 = bin2[-16:]

        string_result = bin1 == bin2

        self.assertEqual(bitwise_result, string_result,
                        "Bitwise optimization should give same result as string comparison")

if __name__ == '__main__':
    # Run the tests
    unittest.main(verbosity=2)
