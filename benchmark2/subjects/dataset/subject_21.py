def greedy_sum_subset(arr, target_sum):
    n = len(arr)

    # Sort the array in decreasing order
    arr.sort(reverse=True)

    # Initialize the list of subsets
    subsets = []

    for i in range(n):
        j = 0
        found = False
        
        # Check if the element can be added to the existing subsets
        while j < len(subsets):
            
            if sum(subsets[j]) + arr[i] <= target_sum:
                subsets[j].append(arr[i])
                found = True
                break
            
            j += 1

        if not found:
            # Create a new subset if no subset can contain the element
            subsets.append([arr[i]])

    return subsets