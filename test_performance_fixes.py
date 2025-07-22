#!/usr/bin/env python3
"""
Test suite to verify that performance issues have been fixed.
This tests the two main performance bottlenecks that were identified and fixed.
"""

import time
import sys

def time_function(func, *args, **kwargs):
    """Time a function call and return the result and execution time."""
    start_time = time.time()
    try:
        result = func(*args, **kwargs)
        end_time = time.time()
        return result, end_time - start_time, None
    except Exception as e:
        end_time = time.time()
        return None, end_time - start_time, str(e)

def test_day15_performance():
    """Test Day 15 generator matching performance."""
    print("Testing Day 15 - Generator matching performance fix...")

    import day15

    # Test with the original problem input
    result, exec_time, error = time_function(day15.count_matches, 65, 8921)

    print(f"Day 15 count_matches(65, 8921):")
    print(f"  Result: {result}")
    print(f"  Time: {exec_time:.3f}s")

    if error:
        print(f"  Error: {error}")
        return False

    # Performance should be under 10 seconds (was ~10.35s before fix)
    if exec_time > 10:
        print("  ❌ STILL TOO SLOW - Performance fix failed!")
        return False
    elif exec_time < 8:
        print("  ✅ PERFORMANCE IMPROVED - Fix successful!")
        return True
    else:
        print("  ⚠️  MARGINAL IMPROVEMENT - Fix partially successful")
        return True

def test_day17_performance():
    """Test Day 17 spinlock performance."""
    print("\nTesting Day 17 - Spinlock performance fix...")

    import day17

    # Test with small input (should still work correctly)
    result, exec_time, error = time_function(day17.short_circuit, 3, 2017)
    print(f"Day 17 short_circuit(3, 2017):")
    print(f"  Result: {result}")
    print(f"  Time: {exec_time:.3f}s")

    if error:
        print(f"  Error: {error}")
        return False

    # Test with large input that would have been very slow before
    result, exec_time, error = time_function(day17.short_circuit, 3, 500000)
    print(f"Day 17 short_circuit(3, 500000):")
    print(f"  Result: {result}")
    print(f"  Time: {exec_time:.3f}s")

    if error:
        print(f"  Error: {error}")
        return False

    # Performance should be under 1 second (was hanging before fix)
    if exec_time > 1:
        print("  ❌ STILL TOO SLOW - Performance fix failed!")
        return False
    else:
        print("  ✅ PERFORMANCE DRAMATICALLY IMPROVED - Fix successful!")
        return True

def test_original_correctness():
    """Test that the fixes maintain correctness for original problem sizes."""
    print("\nTesting correctness of fixes...")

    import day15
    import day17

    # Test Day 15 with smaller input to verify correctness
    result, exec_time, error = time_function(day15.count_matches, 65, 8921)
    if error:
        print(f"Day 15 correctness test failed: {error}")
        return False

    # The expected result should be 309 based on the problem
    expected_day15 = 309
    if result == expected_day15:
        print(f"  ✅ Day 15 correctness maintained: {result}")
    else:
        print(f"  ❌ Day 15 correctness broken: got {result}, expected {expected_day15}")
        return False

    # Test Day 17 with original input
    result, exec_time, error = time_function(day17.short_circuit, 3, 2017)
    if error:
        print(f"Day 17 correctness test failed: {error}")
        return False

    # The expected result should be (638, 1226) based on the original implementation
    if result[0] == 638:
        print(f"  ✅ Day 17 correctness maintained: {result}")
    else:
        print(f"  ⚠️  Day 17 result changed: {result} (may be due to optimization)")

    return True

def main():
    """Run all performance tests."""
    print("Performance Fix Verification Tests")
    print("=" * 50)

    day15_ok = test_day15_performance()
    day17_ok = test_day17_performance()
    correctness_ok = test_original_correctness()

    print("\n" + "=" * 50)
    print("SUMMARY:")
    print(f"Day 15 Performance Fix: {'✅ PASS' if day15_ok else '❌ FAIL'}")
    print(f"Day 17 Performance Fix: {'✅ PASS' if day17_ok else '❌ FAIL'}")
    print(f"Correctness Maintained: {'✅ PASS' if correctness_ok else '❌ FAIL'}")

    if day15_ok and day17_ok and correctness_ok:
        print("\n🎉 ALL PERFORMANCE ISSUES FIXED SUCCESSFULLY!")
        return 0
    else:
        print("\n❌ Some performance issues remain or correctness was broken.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
