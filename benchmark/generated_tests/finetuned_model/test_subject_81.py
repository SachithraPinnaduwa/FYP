import random
import string

def generate_random_integer():
    return ''.join(random.choice(string.digits[1:]) for _ in range(random.randint(1, 18)))

def generate_random_digit():
    return random.choice(string.digits[1:])

def test_find_min_number():
    # Test cases with expected results
    test_cases = [
        ("35", "4", "34"),
        ("42", "4", "24"),
        ("24", "9", "24"),
        ("999", "9", "999"),
        ("123456789", "1", "111111111"),
        ("987654321", "1", "111111111"),
        ("111111111", "2", "121111111"),
        ("111111111", "1", "111111111"),
        ("222222222", "2", "222222222"),
        ("222222222", "1", "211111111"),
    ]
    
    for i, (N, d, expected) in enumerate(test_cases, 1):
        result = find_min_number(N, d)
        assert result == expected, f"Test case {i} failed: expected {expected}, got {result}"
    
    # Test cases with random inputs
    for _ in range(10):
        N = generate_random_integer()
        d = generate_random_digit()
        result = find_min_number(N, d)
        expected = min(int(N[:i] + d + N[i+1:]) for i in range(len(N)))
        assert int(result) == expected, f"Random test case failed: expected {expected}, got {result}"
    
    print("All test cases passed.")

# Run the test cases
test_find_min_number()