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

    def is_zero(self, tolerance=1e-10):
        return self.magnitude() < tolerance

    def is_parallel_to(self, v):
        if self.dimension != v.dimension:
            raise ValueError('Vectors must have same dimension')
        return ( self.is_zero() or
                v.is_zero() or
                self.angle_with(v) == 0 or
                self.angle_with(v) == math.pi )

    def is_orthogonal_to(self, v, tolerance=1e-10):
        if self.dimension != v.dimension:
            raise ValueError('Vectors must have same dimension')
        return abs(self.dot(v)) < tolerance


    def component_orthoganal_to(self, basis):
        projection = self.component_parallel_to(basis)
        return self - projection

    def component_parallel_to(self, basis):
        u = basis.normalized()
        weight = self.dot(u)
        return u.scale(weight)

    def cross(self, v):
        if self.dimension != 3 or v.dimension != 3:
            raise ValueError('Vectors must be three dimensional')
        new_coordinates = [
            self.coordinates[1] * v.coordinates[2] - v.coordinates[1] * self.coordinates[2],
            -1 * (self.coordinates[0] * v.coordinates[2] - v.coordinates[0] * self.coordinates[2]),
            self.coordinates[0] * v.coordinates[1] - v.coordinates[0] * self.coordinates[1],
        ]
        return Vector(new_coordinates)

    def area_of_parallelogram_spanned(self, v):
        cross = self.cross(v)
        return cross.magnitude()

    def area_of_triangle_spanned(self, v):
        return self.area_of_parallelogram_spanned(self, v) / 2.0
