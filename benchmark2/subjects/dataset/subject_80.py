def check_substring(base_string, sub_string):
    # Convert both strings to lowercase for case-insensitive comparison
    base_string = base_string.lower()
    sub_string = sub_string.lower()
    
    # Check if the sub-string appears in the base string
    return sub_string in base_string