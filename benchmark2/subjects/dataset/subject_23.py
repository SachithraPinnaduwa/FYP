def entrance(str1, str2):
    # Convert the input strings to lowercase and remove whitespace
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")

    # Sort the characters in both strings alphabetically
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    # Compare the sorted strings
    return sorted_str1 == sorted_str2