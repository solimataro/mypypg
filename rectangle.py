class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height =  height

    @property
    def info(self):
        return 'Rectangle (W:{} * H:{})'.format(self._width, self._height)

    @property
    def area(self):
        return self._width * self._height

    @property
    def perimeter(self):
        return (self._width + self._height) * 2


if __name__ == '__main__':
    rectangle = Rectangle(4, 5)
    print('長方形:{}'.format(rectangle.info))
    print('面積:{}'.format(rectangle.area))
    print('外周:{}'.format(rectangle.perimeter))
