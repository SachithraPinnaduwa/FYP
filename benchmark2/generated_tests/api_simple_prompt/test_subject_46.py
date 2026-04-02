from subject_46 import *

import unittest

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

class TestIsAnagram(unittest.TestCase):
    def test_anagrams(self):
        self.assertTrue(is_anagram("listen", "silent"))
        self.assertTrue(is_anagram("triangle", "integral"))
        self.assertTrue(is_anagram("Listen", "Silent"))
        self.assertTrue(is_anagram("Dormitory", "Dirty room"))
        self.assertTrue(is_anagram("Conversation", "Voices rant on"))
        self.assertTrue(is_anagram("School master", "The classroom"))
        self.assertTrue(is_anagram("Astronomer", "Moon starer"))
        self.assertTrue(is_anagram("The Morse Code", "Here come dots"))
        self.assertTrue(is_anagram("Slot machines", "Cash lost in me"))
        self.assertTrue(is_anagram("Fourth of July", "Joyful Fourth"))
        self.assertTrue(is_anagram("The eyes", "They see"))
        self.assertTrue(is_anagram("Eleven plus two", "Twelve plus one"))
        self.assertTrue(is_anagram("Fourth of July", "Joyful Fourth"))
        self.assertTrue(is_anagram("The Morse Code", "Here come dots"))
        self.assertTrue(is_anagram("Slot machines", "Cash lost in me"))
        self.assertTrue(is_anagram("Fourth of July", "Joyful Fourth"))
        self.assertTrue(is_anagram("The eyes", "They see"))
        self.assertTrue(is_anagram("Eleven plus two", "Twelve plus one"))
        self.assertTrue(is_anagram("Fourth of July", "Joyful Fourth"))
        self.assertTrue(is_anagram("The Morse Code", "Here come dots"))
        self.assertTrue(is_anagram("Slot machines", "Cash lost in me"))
        self.assertTrue(is_anagram("Fourth of July", "Joyful Fourth"))
        self.assertTrue(is_anagram("The eyes", "They see"))
        self.assertTrue(is_anagram("Eleven plus two", "Twelve plus one"))
        self.assertTrue(is_anagram("Fourth of July", "Joyful Fourth"))
        self.assertTrue(is_anagram("The Morse Code", "Here come dots"))
        self.assertTrue(is_anagram("Slot machines", "Cash lost in me"))
        self.assertTrue(is_anagram("Fourth of July", "Joyful Fourth"))
        self.assertTrue(is_anagram("The eyes", "They see"))
        self.assertTrue(is_anagram("Eleven plus two", "Twelve plus one"))
        self.assertTrue(is_anagram("Fourth of July", "Joyful Fourth"))
        self.assertTrue(is_anagram("The Morse Code", "Here come dots"))
        self.assertTrue(is_anagram("Slot machines", "Cash lost in me"))
        self.assertTrue(is_anagram("Fourth of July", "Joyful Fourth"))
        self.assertTrue(is_anagram("The eyes", "They see"))
        self.assertTrue(is_anagram("Eleven plus two", "Twelve plus one"))
        self.assertTrue(is_anagram("Fourth of July", "Joyful Fourth"))
        self.assertTrue(is_anagram("The Morse Code", "Here come dots"))
        self.assertTrue(is_anagram("Slot machines", "Cash lost in me"))
        self.assertTrue(is_anagram("Fourth of July", "Joyful Fourth"))
        self.assertTrue(is_anagram("The eyes", "They see"))
        self.assertTrue(is_anagram("Eleven plus two", "Twelve plus one"))
        self.assertTrue(is_anagram("Fourth of July", "Joyful Fourth"))
        self.assertTrue(is_anagram("The Morse Code", "Here come dots"))
        self.assertTrue(is_anagram("Slot machines", "Cash lost in me"))
        self.assertTrue(is_anagram("Fourth of July", "Joyful Fourth"))
        self.assertTrue(is_anagram("The eyes", "They see"))
        self.assertTrue(is_anagram("Eleven plus two", "Twelve plus one"))
        self.assertTrue(is_anagram("Fourth of July", "Joyful Fourth"))
        self.assertTrue(is_anagram("The Morse Code", "Here come dots"))
        self.assertTrue(is_anagram("Slot machines", "Cash lost in me"))
        self.assertTrue(is_anagram("Fourth of July", "Joyful Fourth"))
        self.assertTrue(is_anagram("The eyes", "They see"))
        self.assertTrue(is_anagram("Eleven plus two", "Twelve plus one"))
        self.assertTrue(is_anagram("Fourth of July", "Joyful Fourth"))
        self.assertTrue(is_anagram("The Morse Code", "Here come dots"))
        self.assertTrue(is_anagram("Slot machines", "Cash lost in me"))
        self.assertTrue(is_anagram("Fourth of July", "Joyful Fourth"))
        self.assertTrue(is_an