from fib_series import compute_fibonacci_series

def test_compute_fibonacci_series():
    # Test with n = 0
    assert compute_fibonacci_series(0) == []
    
    # Test with n = 1
    assert compute_fibonacci_series(1) == [0]
    
    # Test with n = 2
    assert compute_fibonacci_series(2) == [0, 1]
    
    # Test with n = 5
    assert compute_fibonacci_series(5) == [0, 1, 1, 2, 3]
    
    # Test with n = 10
    assert compute_fibonacci_series(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    
    # Test with n = 15
    assert compute_fibonacci_series(15) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]