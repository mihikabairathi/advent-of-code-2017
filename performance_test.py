#!/usr/bin/env python3
import time
import sys
import importlib

def time_function(func, *args, **kwargs):
    """Time a function call and return the result and execution time."""
    start_time = time.time()
    try:
        result = func(*args, **kwargs)
        end_time = time.time()
        return result, end_time - start_time
    except Exception as e:
        end_time = time.time()
        return f"Error: {e}", end_time - start_time

def test_performance():
    """Test performance of various day solutions."""
    print("Testing performance of Advent of Code solutions...")
    print("=" * 60)

    # Test Day 15 - Generator matching (known to be slow)
    try:
        import day15
        print("Testing Day 15 - Generator matching...")
        result, exec_time = time_function(day15.count_matches, 65, 8921)
        print(f"Day 15: Result = {result}, Time = {exec_time:.3f}s")
        if exec_time > 5:
            print("⚠️  Day 15 is SLOW - needs optimization!")
    except Exception as e:
        print(f"Day 15 test failed: {e}")

    # Test Day 17 - Spinlock (potentially slow)
    try:
        import day17
        print("\nTesting Day 17 - Spinlock...")
        result, exec_time = time_function(day17.short_circuit, 3, 2017)
        print(f"Day 17 (small): Result = {result}, Time = {exec_time:.3f}s")

        # Test with larger input
        result, exec_time = time_function(day17.short_circuit, 3, 50000)
        print(f"Day 17 (large): Result = {result}, Time = {exec_time:.3f}s")
        if exec_time > 2:
            print("⚠️  Day 17 is SLOW - needs optimization!")
    except Exception as e:
        print(f"Day 17 test failed: {e}")

    # Test Day 22 - Virus simulation (potentially slow)
    try:
        import day22
        print("\nTesting Day 22 - Virus simulation...")
        # Create a small test file
        with open('test_day22.txt', 'w') as f:
            f.write("..#\n#..\n...")

        result, exec_time = time_function(day22.simulate_bursts, 10000, 'test_day22.txt')
        print(f"Day 22 (10k): Result = {result}, Time = {exec_time:.3f}s")

        result, exec_time = time_function(day22.simulate_bursts_evolved, 100000, 'test_day22.txt')
        print(f"Day 22 (100k evolved): Result = {result}, Time = {exec_time:.3f}s")
        if exec_time > 3:
            print("⚠️  Day 22 is SLOW - needs optimization!")
    except Exception as e:
        print(f"Day 22 test failed: {e}")

    # Test Day 14 - Grid operations
    try:
        import day14
        print("\nTesting Day 14 - Grid operations...")
        result, exec_time = time_function(day14.count_used, "flqrgnkx")
        print(f"Day 14 (count): Result = {result}, Time = {exec_time:.3f}s")

        result, exec_time = time_function(day14.count_groups, "flqrgnkx")
        print(f"Day 14 (groups): Result = {result}, Time = {exec_time:.3f}s")
        if exec_time > 2:
            print("⚠️  Day 14 is SLOW - needs optimization!")
    except Exception as e:
        print(f"Day 14 test failed: {e}")

if __name__ == "__main__":
    test_performance()
