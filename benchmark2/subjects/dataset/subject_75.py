def reverseArray(arr, start, end):
    if start >= end:
        return
    # Swap elements at start and end indices
    arr[start], arr[end] = arr[end], arr[start]
    # Recursive call with updated start and end indices
    reverseArray(arr, start + 1, end - 1)