def is_anagram(string1, string2):
    """
    Determine if two input strings are anagrams of each other.
    
    Args:
    string1 (str): The first input string.
    string2 (str): The second input string.
    
    Returns:
    bool: True if string1 and string2 are anagrams, False otherwise.
    """
    return sorted(string1.lower()) == sorted(string2.lower())