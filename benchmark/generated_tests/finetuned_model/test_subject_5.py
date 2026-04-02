import random

def test_find_lexicographically_preceding_permutation():
    # Test case 1: Regular case with a valid permutation
    n = 4
    permutation = [1, 3, 2, 4]
    expected = [1, 2, 3, 4]
    assert find_lexicographically_preceding_permutation(n, permutation) == expected, "Test case 1 failed"

    # Test case 2: Permutation is the lexicographically least permutation
    n = 3
    permutation = [1, 2, 3]
    expected = [1, 2, 3]
    assert find_lexicographically_preceding_permutation(n, permutation) == expected, "Test case 2 failed"

    # Test case 3: Permutation is the lexicographically greatest permutation
    n = 3
    permutation = [3, 2, 1]
    expected = [1, 2, 3]
    assert find_lexicographically_preceding_permutation(n, permutation) == expected, "Test case 3 failed"

    # Test case 4: Permutation with repeated elements
    n = 4
    permutation = [1, 3, 2, 3]
    expected = [1, 2, 3, 3]
    assert find_lexicographically_preceding_permutation(n, permutation) == expected, "Test case 4 failed"

    # Test case 5: Random permutation
    n = 5
    permutation = [3, 1, 4, 2, 5]
    expected = [3, 1, 2, 4, 5]
    assert find_lexicographically_preceding_permutation(n, permutation) == expected, "Test case 5 failed"

    # Test case 6: Large permutation
    n = 1000000
    permutation = list(range(1, n+1))
    random.shuffle(permutation)
    expected = sorted(permutation, reverse=True)
    assert find_lexicographically_preceding_permutation(n, permutation) == expected, "Test case 6 failed"

    print("All test cases passed!")