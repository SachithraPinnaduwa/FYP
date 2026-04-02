import random
import string
from typing import *

def solve(input_list):
    subarrays = [element for element in input_list if isinstance(element, list)]
    normal_elements = [element for element in input_list if not isinstance(element, list)]

    def bubble_sort(l):
        n = len(l)
        for i in range(n):
            for j in range(0, n - i - 1):
                if l[j] > l[j + 1] :
                    l[j], l[j + 1] = l[j + 1], l[j]
        return l

    def average(l):
        return sum(l) / len(l)

    sorted_subarrays = sorted([bubble_sort(subarray) for subarray in subarrays], key=average)
    sorted_elements = bubble_sort(normal_elements)
    return sorted_subarrays + sorted_elements

# Test cases
def test_solve():
    # Test case 1: Empty list
    assert solve([]) == []

    # Test case 2: List with no sub-arrays
    assert solve([1, 3, 2]) == [1, 2, 3]

    # Test case 3: List with sub-arrays and normal elements
    assert solve([[3, 2, 1], 5, [4, 6], 7]) == [[1, 2, 3], 4, [5, 6], 7]

    # Test case 4: List with sub-arrays containing different types of elements
    assert solve([[3, 'a', 1], 5, [4, 6], 'b']) == [[1, 3, 'a'], 4, [5, 6], 'b']

    # Test case 5: List with sub-arrays containing negative numbers
    assert solve([[-3, 2, -1], 5, [4, -6], 7]) == [[-3, -1, 2], 4, [-6, 5], 7]

    # Test case 6: List with sub-arrays containing decimals
    assert solve([[3.5, 2.1, 1.9], 5.0, [4.2, 6.3], 7.4]) == [[1.9, 2.1, 3.5], 4.2, [5.0, 6.3], 7.4]

    # Test case 7: List with sub-arrays containing single element
    assert solve([[3], 5, [4], 7]) == [[3], 4, [5], 7]

    # Test case 8: List with sub-arrays containing all the same elements
    assert solve([[3, 3, 3], 5, [4, 4], 7]) == [[3, 3, 3], 4, [4, 4], 5, 7]

    # Test case 9: List with sub-arrays containing large numbers
    assert solve([[1000000, 2000000, 3000000], 5000000, [4000000, 6000000], 7000000]) == [[1000000, 2000000, 3000000], 4000000, [5000000, 6000000], 7000000]

    # Test case 10: Random test case
    random_input = random.sample(range(-100, 100), 10)
    random_input = [random.sample(random_input, random.randint(1, 5)) if random.choice([True, False]) else num for num in random_input]
    sorted_input = [sorted(subarray) if isinstance(subarray, list) else subarray for subarray in random_input]
    sorted_input = sorted(sorted_input, key=lambda x: sum(x) / len(x) if isinstance(x, list) else x)
    assert solve(random_input) == sorted_input