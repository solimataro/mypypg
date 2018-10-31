import math

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        return self._radius ** 2 * math.pi

    @property
    def perimeter(self):
        return self._radius * 2 * math.pi


if __name__ == '__main__':
    c = Circle(10)
    print('面積:{}'.format(c.area))
    print('外周:{}'.format(c.perimeter))
