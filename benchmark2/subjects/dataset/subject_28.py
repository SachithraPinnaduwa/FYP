def longest_repeating_substring(s):
    length = len(s)
    sub_strings = {}

    for i1 in range(length):
        for i2 in range(i1+1, length+1):
            item = s[i1:i2]
            if item in sub_strings:
                sub_strings[item][0] += 1
            else:
                sub_strings[item] = [1, i1]

    max_length = 0
    earliest_starting_position = float("inf")
    longest_substring = ""

    for key, value in sub_strings.items():
        if value[0] > 1:
            if len(key) > max_length or (len(key) == max_length and value[1] < earliest_starting_position):
                max_length = len(key)
                earliest_starting_position = value[1]
                longest_substring = key
    return longest_substring