import unittest

from lib.matrix import Vec3, Mat3


class MyTestCase(unittest.TestCase):
    def test_vec_add(self):
        self.assertEqual(Vec3(6, 4, 7), Vec3(1, 2, 3) + Vec3(5, 2, 4))
        self.assertEqual(Vec3(6, 4, 7), Vec3(5, 2, 4) + Vec3(1, 2, 3))

    def test_vec_sub(self):
        self.assertEqual(Vec3(5, 2, 4), Vec3(6, 4, 7) - Vec3(1, 2, 3))
        self.assertEqual(Vec3(1, 2, 3), Vec3(6, 4, 7) - Vec3(5, 2, 4))

    def test_mat(self):
        matrix = Mat3.fill(0)
        self.assertEqual(0, matrix[0][0])
        matrix[0][0] = 1
        self.assertEqual(1, matrix[0][0])

    def test_mat_vec_multiplication(self):
        matrix = Mat3([[1, 0, -2],
                       [0, 3, -1],
                       [1, 2, 1]])
        vector = Vec3(3, -1, 4)
        self.assertEqual(Vec3(-5, -7, 5), matrix * vector)

    def test_mat_mat_multiplication(self):
        m1 = Mat3([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
        m2 = Mat3([[1, 2, 1],
                   [2, 4, 6],
                   [7, 2, 5]])
        result = Mat3([[26, 16, 28],
                       [56, 40, 64],
                       [86, 64, 100]])
        self.assertEqual(result, m1 * m2)


if __name__ == '__main__':
    unittest.main()
