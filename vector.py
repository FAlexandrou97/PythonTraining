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

    def add(self,v):
        result = [self.coordinates[0] + v.coordinates[0]]
        result2 = [self.coordinates[1] + v.coordinates[1]]
        return result + result2

    def subtract(self,v):
        result = [self.coordinates[0] - v.coordinates[0]]
        result2 = [self.coordinates[1] - v.coordinates[1]]
        return result + result2

    def scale(self,scalar):
        result = tuple(scalar *x for x in self.coordinates)
        return result

    def magnitude(self):
        mag = 0
        for i in range(len(self.coordinates)):
            mag += self.coordinates[i]**2
        result = math.sqrt(mag)
        return result
    
    def normalize(self):
        try:
            magnitude = self.magnitude()
            direction = tuple(1/magnitude *x for x in self.coordinates)
            return direction
        except ZeroDivisionError:
            raise Exception('Zero vector cannot be normalized')

    def dotProduct(self,v):
        try:
            dotProductScalar = 0
            for i in range(len(self.coordinates)):
                dotProductScalar += self.coordinates[i] * v.coordinates[i]
            return dotProductScalar
        except ZeroDivisionError:
            raise Exception('Cannot compute dot product of zero vector')

    def findAngle(self,v,in_degrees = False):
        magnitudeSelf = self.magnitude()
        magnitudeV = v.magnitude()
        products = self.dotProduct(v) / (magnitudeSelf * magnitudeV)
        theta = math.acos(products)
        if(in_degrees):
            return math.degrees(theta)
        return theta
    
#All vectors given by the exercise
#add 2 vectors
vector1 = Vector([8.218,-9.341])
vector2 = Vector([-1.129, 2.111])
result1 = vector1.add(vector2)

#subtract 2 vectors
vector1 = Vector([7.119,8.215])
vector2 = Vector([-8.223, 0.878])
result2 = vector1.subtract(vector2)

#scale a vector
vector3d = Vector([1.671,-1.012,-0.318])
result3 = vector3d.scale(7.41)

#find magnitudes
vector1 = Vector([-0.221, 7.437])
vector3d = Vector([8.813,-1.331,-6.247])
result4 = vector1.magnitude()
result5 = vector3d.magnitude()

#normalize vector
vector1 = Vector([5.581, -2.136])
vector3d = Vector([1.996,3.108,-4.554])
result6 = vector1.normalize()
result7 = vector3d.normalize()

#dot Product
vector1 = Vector([7.887, 4.138])
vector2 = Vector([-8.802, 6.776])
vector3d = Vector([-5.955,-4.904,-1.874])
vector3d2 = Vector([-4.496,-8.755,7.103])
result8 = vector1.dotProduct(vector2)
result9 = vector3d.dotProduct(vector3d2)

#Find angle of 2 vectors (by their dot product)
vector1 = Vector([3.183, -7.627])
vector2 = Vector([-2.668, 5.319])
result10 = vector1.findAngle(vector2)
vector3d = Vector([7.35, 0.221, 5.188])
vector3d2 = Vector([2.751, 8.259, 3.985])
result11 = vector3d.findAngle(vector3d2,True)

#print results
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