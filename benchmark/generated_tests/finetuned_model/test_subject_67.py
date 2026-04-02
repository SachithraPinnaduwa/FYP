import math

def compute_sum(x, K):
    total = sum(x)

    if total % K == 0:
        return format(total, ".2f")
    else:
        return math.ceil(total)

# Test cases
def test_compute_sum():
    assert compute_sum([10, 20, 30], 5) == '60.00', "Test case 1 failed"
    assert compute_sum([1, 2, 3, 4, 5], 3) == 15, "Test case 2 failed"
    assert compute_sum([0, 0, 0, 0], 10) == '0.00', "Test case 3 failed"
    assert compute_sum([7, 14, 21], 7) == '49.00', "Test case 4 failed"
    assert compute_sum([12, 24, 36, 48, 60], 12) == 180.00, "Test case 5 failed"
    assert compute_sum([1], 1) == 1.00, "Test case 6 failed"
    assert compute_sum([9, 18, 27], 9) == 54.00, "Test case 7 failed"
    assert compute_sum([15, 30, 45, 60], 15) == 150.00, "Test case 8 failed"
    assert compute_sum([2], 2) == 2.00, "Test case 9 failed"
    assert compute_sum([13, 26, 39], 13) == 78.00, "Test case 10 failed"