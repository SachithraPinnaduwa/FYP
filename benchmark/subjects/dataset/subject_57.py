def filter_strings(data, n):
    result = []
    for string in data:
        if len(string) > n and any(char.isupper() for char in string):
            result.append(string)
    return result