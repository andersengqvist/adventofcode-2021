

class Vec3:
    """ A 3d vector (column matrix) """
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def x(self):
        return self._x

    def y(self):
        return self._y

    def z(self):
        return self._z

    def len_sq(self):
        """ The length of the vector squared """
        return self._x * self._x + self._y * self._y + self._z * self._z

    def abs_distance(self, other):
        """ The absolute distance to other vector, results in a new Vec3 """
        return Vec3(abs(self._x - other.x()), abs(self._y - other.y()), abs(self._z - other.z()))

    def taxi_distance(self, other):
        """ The taxi distance to other vector, a scalar """
        return abs(self._x - other.x()) + abs(self._y - other.y()) + abs(self._z - other.z())

    def __add__(self, other):
        return Vec3(self._x + other.x(), self._y + other.y(), self._z + other.z())

    def __sub__(self, other):
        """ The absolute distance to other vector """
        return Vec3(self._x - other.x(), self._y - other.y(), self._z - other.z())

    def __eq__(self, other):
        if isinstance(other, Vec3):
            return self._x == other.x() and self._y == other.y() and self._z == other.z()

    def __hash__(self):
        return self._x * 7 + self._y * 13 + self._z * 17

    def __repr__(self):
        return "[{}, {}, {}]".format(self._x, self._y, self._z)


class Mat3:
    """ A 3d matrix """
    def __init__(self, mat):
        self._mat = [[mat[0][0], mat[0][1], mat[0][2]],
                     [mat[1][0], mat[1][1], mat[1][2]],
                     [mat[2][0], mat[2][1], mat[2][2]]]

    @classmethod
    def fill(cls, value):
        return cls([[value, value, value],
                    [value, value, value],
                    [value, value, value]])

    def __getitem__(self, row):
        return self._mat[row]

    def __mul__(self, other):
        if isinstance(other, Vec3):
            return Vec3(self._mat[0][0] * other.x() + self._mat[0][1] * other.y() + self._mat[0][2] * other.z(),
                        self._mat[1][0] * other.x() + self._mat[1][1] * other.y() + self._mat[1][2] * other.z(),
                        self._mat[2][0] * other.x() + self._mat[2][1] * other.y() + self._mat[2][2] * other.z())
        elif isinstance(other, Mat3):
            return Mat3([[self._mm(other, 0, 0), self._mm(other, 0, 1), self._mm(other, 0, 2)],
                         [self._mm(other, 1, 0), self._mm(other, 1, 1), self._mm(other, 1, 2)],
                         [self._mm(other, 2, 0), self._mm(other, 2, 1), self._mm(other, 2, 2)]])
        else:
            raise Exception("Cannot multiply")

    def _mm(self, other, row, col):
        return self._mat[row][0] * other[0][col]\
               + self._mat[row][1] * other[1][col]\
               + self._mat[row][2] * other[2][col]

    def __repr__(self):
        return "[[{}, {}, {}],\n [{}, {}, {}],\n [{}, {}, {}]]".format(
            self._mat[0][0], self._mat[0][1], self._mat[0][2],
            self._mat[1][0], self._mat[1][1], self._mat[1][2],
            self._mat[2][0], self._mat[2][1], self._mat[2][2])

    def __eq__(self, other):
        return self._mat[0][0] == other[0][0] and self._mat[0][1] == other[0][1] and self._mat[0][2] == other[0][2]\
            and self._mat[1][0] == other[1][0] and self._mat[1][1] == other[1][1] and self._mat[1][2] == other[1][2]\
            and self._mat[2][0] == other[2][0] and self._mat[2][1] == other[2][1] and self._mat[2][2] == other[2][2]

    def __hash__(self):
        return self._mat[0][0] + 3 * self._mat[0][1] + 5 * self._mat[0][2]\
               + 7 * self._mat[1][0] + 11 * self._mat[1][1] + 13 * self._mat[1][2]\
               + 17 * self._mat[2][0] + 23 * self._mat[2][1] + 31 * self._mat[2][2]
