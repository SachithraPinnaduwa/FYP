from subject_25 import *

import unittest

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' ')
    beat_duration = []
    for note in notes:
        if note == 'o':
            beat_duration.append(4)
        elif note == 'o|':
            beat_duration.append(2)
        elif note == '.|':
            beat_duration.append(1)
    return beat_duration

class TestParseMusic(unittest.TestCase):
    def test_parse_music(self):
        self.assertEqual(parse_music('o o| .|'), [4, 2, 1])
        self.assertEqual(parse_music('o| o| o|'), [2, 2, 2])
        self.assertEqual(parse_music('.| .| .|'), [1, 1, 1])
        self.assertEqual(parse_music('o o| .| o|'), [4, 2, 1, 2])
        self.assertEqual(parse_music(''), [])

if __name__ == '__main__':
    unittest.main()