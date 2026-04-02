def binary_search(arr, target, find_leftmost):
    low = 0
    high = len(arr) - 1
    result = -1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            result = mid
            if find_leftmost:
                high = mid - 1
            else:
                low = mid + 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return result

def count_and_indices(arr, target):
    left = binary_search(arr, target, True)
    if left == -1:
        return 0, []

    right = binary_search(arr, target, False)
    count = right - left + 1
    indices = [i for i in range(left, right + 1)]
    return count, indices