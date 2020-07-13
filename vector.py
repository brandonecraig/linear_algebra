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

    def __add__(self, v):
        if self.dimension != v.dimension:
            raise ValueError('Vectors must have same dimension')
        new_coordinates = [x + y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def __sub__(self, v):
        if self.dimension != v.dimension:
            raise ValueError('Vectors must have same dimension')
        new_coordinates = [x - y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def scale(self, s):
        new_coordinates = [x * s for x in self.coordinates]
        return Vector(new_coordinates)

    def magnitude(self):
        return math.sqrt(sum([ math.pow(x, 2) for x in self.coordinates ]))

    def normalized(self):
        try:
            return self.scale(1.0 / self.magnitude())

        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')

    def dot(self, v):
        if self.dimension != v.dimension:
            raise ValueError('Vectors must have same dimension')
        return sum([x * y for x,y in zip(self.coordinates, v.coordinates)])

    def angle_with(self, v, in_degrees=False):
        if self.dimension != v.dimension:
            raise ValueError('Vectors must have same dimension')
        radians = math.acos(self.normalized().dot(v.normalized()))

        if in_degrees:
            degrees_per_radians = 180.0 / math.pi
            return radians * degrees_per_radians
        else:
            return radians
