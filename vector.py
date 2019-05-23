import math


class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def add(self, v):
        result = [self.coordinates[0] + v.coordinates[0]]
        result2 = [self.coordinates[1] + v.coordinates[1]]
        return result + result2

    def subtract(self, v):
        result = [self.coordinates[0] - v.coordinates[0]]
        result2 = [self.coordinates[1] - v.coordinates[1]]
        return result + result2

    def scale(self, scalar):
        result = tuple(scalar * x for x in self.coordinates)
        return result

    def magnitude(self):
        mag = 0
        for i in range(len(self.coordinates)):
            mag += self.coordinates[i] ** 2
        result = math.sqrt(mag)
        return result

    def normalize(self):
        try:
            magnitude = self.magnitude()
            direction = tuple(1 / magnitude * x for x in self.coordinates)
            return direction
        except ZeroDivisionError:
            raise Exception('Zero vector cannot be normalized')

    def dotProduct(self, v):
        try:
            dotProductScalar = 0
            for i in range(len(self.coordinates)):
                dotProductScalar += self.coordinates[i] * v.coordinates[i]
            return dotProductScalar
        except ZeroDivisionError:
            raise Exception('Cannot compute dot product of zero vector')

    def findAngle(self, v, in_degrees=False):
        magnitudeSelf = self.magnitude()
        magnitudeV = v.magnitude()
        products = self.dotProduct(v) / (magnitudeSelf * magnitudeV)
        theta = math.acos(products)
        if in_degrees:
            return math.degrees(theta)
        return theta

    def checkIfParallel(self, v):
        # Check if both vectors' y/x is equal
        m1 = self.coordinates[1] / self.coordinates[0]
        m2 = v.coordinates[1] / v.coordinates[0]
        if (m1 == m2):
            return True
        else:
            return False

    def checkIfOrthogonal(self, v):
        # If their dot product is 0, then they are orthogonal
        if self.dotProduct(v) == 0:
            return True
        else:
            return False

    def projection(self, v):
        # Projection Formula:
        # Dot product of 2 vectors divided by the length ^2 of the second vector times the second vector
        # Returns a vector
        projection = tuple((self.dotProduct(v) / (v.magnitude()) ** 2) * x for x in v.coordinates)
        return projection

    def componentOrthogonalTo(self, v):
        # Orthogonal Component Formula:
        # vector - projection
        component = []
        projection = self.projection(v)
        coordinates = self.coordinates
        for i in range(len(projection)):
            component.append(coordinates[i] - projection[i])

        return component

    def componentParallelTo(self, v):
        # Parallel Component Formula:
        # multiply the normalization of v by the dot product of self with the normalization of v(again)
        component = []
        u = Vector(v.normalize())
        weight = self.dotProduct(u)
        component = u.scale(weight)
        return component

    def crossProduct(self, v):
        # replaced with x,y,z for easier representation
        x_1, y_1, z_1 = self.coordinates
        x_2, y_2, z_2 = v.coordinates
        cross = [y_1 * z_2 - y_2 * z_1,
                 -(x_1 * z_2 - x_2 * z_1),
                 x_1 * y_2 - x_2 * y_1]
        return cross

    def parallelogram(self, v):
        cross = Vector(self.crossProduct(v))
        parallelogram = cross.magnitude()
        return parallelogram

    def areaOfTriangle(self, v):
        # parallelogram/2
        parallelogram = self.parallelogram(v)
        triangle = parallelogram / 2
        return triangle


# All vectors given by the exercise
# add 2 vectors
vector1 = Vector([8.218, -9.341])
vector2 = Vector([-1.129, 2.111])
result1 = vector1.add(vector2)

# subtract 2 vectors
vector1 = Vector([7.119, 8.215])
vector2 = Vector([-8.223, 0.878])
result2 = vector1.subtract(vector2)

# scale a vector
vector3d = Vector([1.671, -1.012, -0.318])
result3 = vector3d.scale(7.41)

# find magnitudes (length)
vector1 = Vector([-0.221, 7.437])
vector3d = Vector([8.813, -1.331, -6.247])
result4 = vector1.magnitude()
result5 = vector3d.magnitude()

# normalize vector
vector1 = Vector([5.581, -2.136])
vector3d = Vector([1.996, 3.108, -4.554])
result6 = vector1.normalize()
result7 = vector3d.normalize()

# dot Product
vector1 = Vector([7.887, 4.138])
vector2 = Vector([-8.802, 6.776])
vector3d = Vector([-5.955, -4.904, -1.874])
vector3d2 = Vector([-4.496, -8.755, 7.103])
result8 = vector1.dotProduct(vector2)
result9 = vector3d.dotProduct(vector3d2)

# Find angle of 2 vectors (by their dot product)
vector1 = Vector([3.183, -7.627])
vector2 = Vector([-2.668, 5.319])
result10 = vector1.findAngle(vector2)
vector3d = Vector([7.35, 0.221, 5.188])
vector3d2 = Vector([2.751, 8.259, 3.985])
result11 = vector3d.findAngle(vector3d2, True)

# Check if 2 vectors are parallel
vector1 = Vector([-7.579, -7.88])
vector2 = Vector([22.737, 23.64])
result12 = vector1.checkIfParallel(vector2)
vector3d = Vector([-2.029, 9.97, 4.172])
vector3d2 = Vector([-9.231, -6.639, -7.245])
result13 = vector3d.checkIfParallel(vector3d2)
vector3d = Vector([-2.328, -7.284, -1.214])
vector3d2 = Vector([-1.821, 1.072, -2.94])
result14 = vector3d.checkIfParallel(vector3d2)
vector1 = Vector([2.118, 4.827])
vector2 = Vector([0, 0])
# result15 = vector1.checkIfParallel(vector2) Division by 0 error

# Check if 2 vectors are orthogonal
vector1 = Vector([-7.759, -7.88])
vector2 = Vector([22.737, 23.64])
result16 = vector1.checkIfOrthogonal(vector2)
vector3d = Vector([-2.029, 9.97, 4.172])
vector3d2 = Vector([-9.231, -6.639, -7.245])
result17 = vector3d.checkIfOrthogonal(vector3d2)
vector3d = Vector([-2.328, -7.284, -1.214])
vector3d2 = Vector([-1.821, 1.072, -2.94])
result18 = vector3d.checkIfOrthogonal(vector3d2)
vector1 = Vector([2.118, 4.827])
vector2 = Vector([0, 0])
result19 = vector1.checkIfOrthogonal(vector2)

# Projection of vector 1 to vector 2
vector1 = Vector([3.039, 1.879])
vector2 = Vector([0.825, 2.036])
result20 = vector1.projection(vector2)

# Component of vector 1 orthogonal to vector 2
vector3d = Vector([-9.88, -3.264, -8.159])
vector3d2 = Vector([-2.155, -9.353, -9.473])
result21 = vector3d.componentOrthogonalTo(vector3d2)

# Component of vector 1 parallel to vector 2 + orthogonal for the exercise
vector4d = Vector([3.009, -6.172, 3.692, -2.51])
vector4d2 = Vector([6.404, -9.144, 2.759, 8.718])
result22 = vector4d.componentParallelTo(vector4d2)
result23 = vector4d.componentOrthogonalTo(vector4d2)

# Cross product
vector3d = Vector([8.462, 7.893, -8.187])
vector3d2 = Vector([6.984, -5.975, 4.778])
result24 = vector3d.crossProduct(vector3d2)

# area of parallelogram -> return the magnitute of the cross product
vector3d = Vector([-8.987, -9.838, 5.031])
vector3d2 = Vector([-4.268, -1.861, -8.866])
result25 = vector3d.parallelogram(vector3d2)

# area of triangle -> area of parallelogram / 2
vector3d = Vector([1.5, 9.547, 3.691])
vector3d2 = Vector([-6.007, 0.124, 5.772])
result26 = vector3d.areaOfTriangle(vector3d2)

# print results
print(vector1)
print(vector2)
print(vector3d)
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)
print(result8)
print(result9)
print(result10)
print(result11)
print(result12)
print(result13)
print(result14)
# print(result15)
print(result16)
print(result17)
print(result18)
print(result19)
print(result20)
print(result21)
print(result22)
print(result23)
print(result24)
print(result25)
print(result26)
