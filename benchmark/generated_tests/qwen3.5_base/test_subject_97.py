import unittest

class TestSimpleSegmentTree(unittest.TestCase):
    def test_init(self):
        arr = [1, 2, 3, 4, 5]
        st = SimpleSegmentTree(arr)
        self.assertEqual(st.n, 5)
        self.assertEqual(st.tree[10], 1)
        self.assertEqual(st.tree[11], 2)
        self.assertEqual(st.tree[12], 3)
        self.assertEqual(st.tree[13], 4)
        self.assertEqual(st.tree[14], 5)

    def test_update(self):
        arr = [1, 2, 3, 4, 5]
        st = SimpleSegmentTree(arr)
        st.update(2, 10)
        self.assertEqual(st.tree[12], 10)
        self.assertEqual(st.query(0, 4), 19)

    def test_query(self):
        arr = [1, 2, 3, 4, 5]
        st = SimpleSegmentTree(arr)
        self.assertEqual(st.query(0, 4), 15)
        self.assertEqual(st.query(1, 3), 9)

if __name__ == '__main__':
    unittest.main()
