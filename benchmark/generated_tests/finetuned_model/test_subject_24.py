from typing import List

def test_binary_search():
    # Test case 1: Target is in the middle of the list
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target1 = 6
    assert binary_search(arr1, target1) == 5

    # Test case 2: Target is at the beginning of the list
    arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target2 = 1
    assert binary_search(arr2, target2) == 0

    # Test case 3: Target is at the end of the list
    arr3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target3 = 10
    assert binary_search(arr3, target3) == 9

    # Test case 4: Target is not in the list
    arr4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target4 = 11
    assert binary_search(arr4, target4) == -1

    # Test case 5: Empty list
    arr5 = []
    target5 = 5
    assert binary_search(arr5, target5) == -1

    # Test case 6: List with one element
    arr6 = [5]
    target6 = 5
    assert binary_search(arr6, target6) == 0

    # Test case 7: List with two elements
    arr7 = [1, 3]
    target7 = 3
    assert binary_search(arr7, target7) == 1

    # Test case 8: Target is in the first half of the list
    arr8 = [1, 3, 5, 7, 9]
    target8 = 3
    assert binary_search(arr8, target8) == 1

    # Test case 9: Target is in the second half of the list
    arr9 = [1, 3, 5, 7, 9]
    target9 = 7
    assert binary_search(arr9, target9) == 3

    # Test case 10: Target is in the list with negative numbers
    arr10 = [-10, -5, 0, 5, 10]
    target10 = 0
    assert binary_search(arr10, target10) == 2