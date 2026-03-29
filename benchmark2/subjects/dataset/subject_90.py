def transform_array_after_operations(a, k):
    li = []
    for i in range(k):
        m = max(a)
        a = [m - i for i in a]
        if a in li:
            if not k % 2:
                return li[-1]
            return a
        li.append(a)
    return a