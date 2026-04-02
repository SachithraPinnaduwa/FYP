```python
import unittest
from collections import Counter
from typing import List, Tuple

def make_strings_equal(s: str, t: str) -> Tuple[int, List[Tuple[int, int]]]:
    n = len(s)
    cnt = Counter(s + t)
    
    # Check if the total count of 'a' and 'b' is even
    for key in cnt:
        if cnt[key] % 2 != 0:
            return -1, []
    
    ans = []
    ff = [i + 1 for i in range(n) if s[i] == 'a' and t[i] == 'b']
    ss = [i + 1 for i in range(n) if s[i] == 'b' and t[i] == 'a']
    
    # Perform swaps to make the strings equal
    while len(ff) > 1:
        t1 = ff.pop(0)
        t2 = ff.pop(0)
        ans.append((t2, t1))
    
    while len(ss) > 1:
        t1 = ss.pop(0)
        t2 = ss.pop(0)
        ans.append((t1, t2))
    
    if len(ff) > 0:
        t1 = ff.pop(0)
        t2 = ss.pop(0)
        ans.append((t2, t2))
        ans.append((t1, t2))
    
    return len(ans), ans

class TestMakeStringsEqual(unittest.TestCase):
    def test_case_1(self):
        result = make_strings_equal("abab", "aabb")
        self.assertEqual(result, (2, [(3, 3), (3, 2)]))

    def test_case_2(self):
        result = make_strings_equal("a", "b")
        self.assertEqual(result, (-1, []))

    def test_case_3(self):
        result = make_strings_equal("babbaabb", "abababaa")
        self.assertEqual(result, (3, [(2, 6), (1, 3), (7, 8)]))

    def test_case_4(self):
        result = make_strings_equal("aaaa", "bbbb")
        self.assertEqual(result, (-1, []))

    def test_case_5(self):
        result = make_strings_equal("abcde", "edcba")
        self.assertEqual(result, (-1, []))

    def test_case_6(self