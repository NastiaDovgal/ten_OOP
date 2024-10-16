import math

class Triangle:
    def __init__(self, side1, side2, side3):
        self._side1 = side1
        self._side2 = side2
        self._side3 = side3

    # Setters (сетер)
    def set_side1(self, side1):
        self._side1 = side1

    def set_side2(self, side2):
        self._side2 = side2

    def set_side3(self, side3):
        self._side3 = side3

    # Getters (гетер)
    def get_side1(self):
        return self._side1

    def get_side2(self):
        return self._side2

    def get_side3(self):
        return self._side3

    # Метод для обчислення периметра
    def perimeter(self):
        return self._side1 + self._side2 + self._side3

    # Метод для обчислення площі за формулою Герона
    def area(self):
        p = self.perimeter() / 2  # напівпериметр
        return math.sqrt(p * (p - self._side1) * (p - self._side2) * (p - self._side3))

    # Статичний метод для перевірки, чи можливий трикутник з такими сторонами
    @staticmethod
    def is_valid_triangle(side1, side2, side3):
        return side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1


# Демонстрація роботи з класом Triangle
def main():
    side1 = 3
    side2 = 4
    side3 = 5

    # Статичний метод для перевірки трикутника
    if Triangle.is_valid_triangle(side1, side2, side3):
        triangle = Triangle(side1, side2, side3)
        
        # Виведення початкових сторін трикутника
        print(f"Сторони трикутника: {triangle.get_side1()}, {triangle.get_side2()}, {triangle.get_side3()}")

        # Виведення периметра
        print(f"Периметр трикутника: {triangle.perimeter()}")

        # Виведення площі
        print(f"Площа трикутника: {triangle.area()}")

        # Зміна значення однієї сторони
        triangle.set_side1(6)
        print(f"Нова сторона 1: {triangle.get_side1()}")
        print(f"Новий периметр трикутника: {triangle.perimeter()}")
        print(f"Нова площа трикутника: {triangle.area()}")

    else:
        print("Неможливо створити трикутник з такими сторонами!")

if __name__ == "__main__":
    main()
