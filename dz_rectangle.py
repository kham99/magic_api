

class Rectangle:
    def __init__(self, width: int, heigh: int):
        if not isinstance(width, int):
            raise TypeError("Ширина прямоугольника должны быть целым числом!")
        if not isinstance(heigh, int):
            raise TypeError("Длина прямоугольника должны быть целым числом!")
        self.width = width
        self.heigh = heigh

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width * self.heigh == other.width * other.heigh
        else: return False

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.width * self.heigh < other.width * other.heigh
        else: return False

    def __le__(self, other):
        if isinstance(other, Rectangle):
            return self.width * self.heigh <= other.width * other.heigh
        else: return False


rectangle1 = Rectangle(1, 1)
rectangle2 = Rectangle(2, 2)
rectangle3 = Rectangle(2, 2)

print(rectangle1 == rectangle2)
print(rectangle2 == rectangle3)
print(rectangle1 < rectangle2)
print(rectangle2 < rectangle3)
print(rectangle2 <= rectangle3)

