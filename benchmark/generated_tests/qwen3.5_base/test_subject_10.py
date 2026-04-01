import unittest

class TestVector3D(unittest.TestCase):
    def test_init(self):
        v = Vector3D(1, 2, 3)
        self.assertEqual(v.x, 1)
        self.assertEqual(v.y, 2)
        self.assertEqual(v.z, 3)

    def test_add(self):
        v1 = Vector3D(1, 2, 3)
        v2 = Vector3D(4, 5, 6)
        v3 = v1.add(v2)
        self.assertEqual(v3.x, 5)
        self.assertEqual(v3.y, 7)
        self.assertEqual(v3.z, 9)

    def test_dot(self):
        v1 = Vector3D(1, 2, 3)
        v2 = Vector3D(4, 5, 6)
        self.assertEqual(v1.dot(v2), 32)

    def test_magnitude(self):
        v = Vector3D(3, 4, 0)
        self.assertEqual(v.magnitude(), 5)

if __name__ == '__main__':
    unittest.main()
