def find_median(arr):
    arr_length = len(arr)
    sorted_arr = sorted(arr)
    
    if arr_length % 2 == 1:
        median_index = arr_length // 2
        median = sorted_arr[median_index]
    else:
        median_index_1 = arr_length // 2 - 1
        median_index_2 = arr_length // 2
        median = (sorted_arr[median_index_1] + sorted_arr[median_index_2]) / 2
    
    return round(median)