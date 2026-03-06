"""
Sorting Algorithms module - Subject for test generation benchmarking.
Contains various sorting algorithm implementations.
"""

from typing import List, Callable, Optional


def bubble_sort(arr: List) -> List:
    """
    Sort a list using bubble sort algorithm.

    Args:
        arr: List of comparable elements

    Returns:
        A new sorted list

    Raises:
        TypeError: If input is not a list
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    result = arr.copy()
    n = len(result)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break
    return result


def insertion_sort(arr: List) -> List:
    """
    Sort a list using insertion sort algorithm.

    Args:
        arr: List of comparable elements

    Returns:
        A new sorted list
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    result = arr.copy()
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
    return result


def merge_sort(arr: List) -> List:
    """
    Sort a list using merge sort algorithm.

    Args:
        arr: List of comparable elements

    Returns:
        A new sorted list
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    if len(arr) <= 1:
        return arr.copy()

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return _merge(left, right)


def _merge(left: List, right: List) -> List:
    """Merge two sorted lists."""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr: List) -> List:
    """
    Sort a list using quick sort algorithm.

    Args:
        arr: List of comparable elements

    Returns:
        A new sorted list
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    if len(arr) <= 1:
        return arr.copy()

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


def selection_sort(arr: List) -> List:
    """
    Sort a list using selection sort algorithm.

    Args:
        arr: List of comparable elements

    Returns:
        A new sorted list
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    result = arr.copy()
    n = len(result)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if result[j] < result[min_idx]:
                min_idx = j
        result[i], result[min_idx] = result[min_idx], result[i]
    return result


def is_sorted(arr: List, reverse: bool = False) -> bool:
    """
    Check if a list is sorted.

    Args:
        arr: The list to check
        reverse: If True, check for descending order

    Returns:
        True if the list is sorted
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    if len(arr) <= 1:
        return True
    if reverse:
        return all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


def binary_search(arr: List, target) -> int:
    """
    Perform binary search on a sorted list.

    Args:
        arr: A sorted list
        target: The element to search for

    Returns:
        The index of the target, or -1 if not found

    Raises:
        ValueError: If the list is not sorted
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    if not is_sorted(arr):
        raise ValueError("List must be sorted for binary search")

    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
