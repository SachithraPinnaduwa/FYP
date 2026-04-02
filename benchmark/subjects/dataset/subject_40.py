def min_increment_operations(arr, N):
    c = 0
    arr.sort()
    for i in range(1, N):
        if arr[i] <= arr[i - 1]:
            c += arr[i - 1] + 1 - arr[i]
            arr[i] = arr[i - 1] + 1
    return c