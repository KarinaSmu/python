import logging
import argparse


class NegativeValueError(ValueError):
    pass


logging.basicConfig(filename='Log/log_1.log',
                    filemode='w',
                    encoding='utf-8',
                    format='{levelname} - {asctime} в строке {lineno} '
                           'функция "{funcName}()" : {msg}',
                    style='{',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


class Rectangle:

    def __init__(self, width, height=None):
        """
        >>> r1 = Rectangle(5)
        >>> r1.width
        5
        >>> r1.height
        5
        >>> r2 = Rectangle(3, 4)
        >>> r2.width
        3
        >>> r2.height
        4
        >>> r3 = Rectangle(-2)
        Traceback (most recent call last):
        ...
        NegativeValueError: Ширина должна быть положительной, а не -2
        >>> r4 = Rectangle(5, -3)
        Traceback (most recent call last):
        ...
        NegativeValueError: Высота должна быть положительной, а не -3
        """
        try:
            if width <= 0:
                raise NegativeValueError(f'Ширина должна быть положительной, а не {width}')
            self._width = width
            if height is None:
                self._height = width
            else:
                if height <= 0:
                    raise NegativeValueError(f'Высота должна быть положительной, а не {height}')
                self._height = height

            logger.info(f'Создан новый прямоугольник: Ширина={self._width}, Высота={self._height}')

        except NegativeValueError as e:
            logger.error(e)

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        try:
            if value > 0:
                self._width = value
            else:
                raise NegativeValueError(f'Ширина должна быть положительной, а не {value}')
        except NegativeValueError as e:
            logger.error(e)

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        try:
            if value > 0:
                self._height = value
            else:
                raise NegativeValueError(f'Высота должна быть положительной, а не {value}')
        except NegativeValueError as e:
            logger.error(e)

    def perimeter(self):
        """
        >>> r1 = Rectangle(5)
        >>> r1.perimeter()
        20
        >>> r2 = Rectangle(3, 4)
        >>> r2.perimeter()
        14
        """
        try:
            return 2 * (self._width + self._height)
        except Exception as e:
            logger.error(f'Ошибка в вычислении периметра: {e}')

    def area(self):
        """
        >>> r1 = Rectangle(5)
        >>> r1.area()
        25
        >>> r2 = Rectangle(3, 4)
        >>> r2.area()
        12
        """
        try:
            return self._width * self._height
        except Exception as e:
            logger.error(f'Ошибка в вычислении площади: {e}')

    def __add__(self, other):
        """
        >>> r1 = Rectangle(5)
        >>> r2 = Rectangle(3, 4)
        >>> r3 = r1 + r2
        >>> r3.width
        8
        >>> r3.height
        6.0
        """
        try:
            width = self._width + other._width
            perimeter = self.perimeter() + other.perimeter()
            height = perimeter / 2 - width
            result_rectangle = Rectangle(width, height)

            logger.info(f'Прямоугольники сложены: Ширина={result_rectangle.width}, Высота={result_rectangle.height}')

            return result_rectangle

        except Exception as e:
            logger.error(f'Ошибка сложения прямоугольников: {e}')

    def __sub__(self, other):
        """
        >>> r1 = Rectangle(5)
        >>> r2 = Rectangle(3, 4)
        >>> r3 = r1 - r2
        >>> r3.width
        2
        >>> r3.height
        2.0
        """
        try:
            if self.perimeter() < other.perimeter():
                self, other = other, self
            width = abs(self._width - other._width)
            perimeter = self.perimeter() - other.perimeter()
            height = perimeter / 2 - width
            result_rectangle = Rectangle(width, height)

            logger.info(f'Прямоугольники вычтены: Ширина={result_rectangle.width}, Высота={result_rectangle.height}')

            return result_rectangle

        except Exception as e:
            logger.error(f'Ошибка вычитания прямоугольников: {e}')



if __name__ == "__main__":
    import doctest

    parser = argparse.ArgumentParser(description='Rectangle Operations')
    parser.add_argument('-width1', type=int, default=5, help='Width of the first rectangle')
    parser.add_argument('-height1', type=int, default=None, help='Height of the first rectangle')
    parser.add_argument('-width2', type=int, default=3, help='Width of the second rectangle')
    parser.add_argument('-height2', type=int, default=4, help='Height of the second rectangle')
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)

    r1 = Rectangle(args.width1, args.height1)
    r2 = Rectangle(args.width2, args.height2)

    r3 = r1 + r2
    r4 = r1 - r2

    print(f"r3 width: {r3.width}, height: {r3.height}")
    print(f"r4 width: {r4.width}, height: {r4.height}")
    print(f"r3 perimeter: {r3.perimeter()}, area: {r3.area()}")
    print(f"r4 perimeter: {r4.perimeter()}, area: {r4.area()}")

    doctest.testmod()

