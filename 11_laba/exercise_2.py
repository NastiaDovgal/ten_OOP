import turtle

class Star:
    def __init__(self, x, y, size, points=5, color="blue"):
        """
        Конструктор класу, який визначає початкові координати (x, y),
        розмір зірки та кількість променів (points).
        """
        self.x = x
        self.y = y
        self.size = size
        self.points = points
        self.color = color
        self.t = turtle.Turtle()

    def draw(self):
        """
        Метод для малювання зірки.
        """
        angle = 180 - (180 / self.points)

        # Переміщення на стартові координати без малювання
        self.t.penup()
        self.t.goto(self.x, self.y)
        self.t.pendown()

        self.t.color(self.color)
        self.t.begin_fill()

        for _ in range(self.points):
            self.t.forward(self.size)
            self.t.right(angle)

        self.t.end_fill()

    def set_position(self, x, y):
        """
        Метод для зміни координат початкової позиції.
        """
        self.x = x
        self.y = y

    def set_size(self, size):
        """
        Метод для зміни розміру зірки.
        """
        self.size = size

    def set_color(self, color):
        """
        Метод для зміни кольору зірки.
        """
        self.color = color

# Демонстрація роботи з класом Star
def main():
    # Створення першої зірки
    star1 = Star(x=-400, y=300, size=250, points=5, color="pink")
    star1.draw()

    # Створення другої зірки з іншими параметрами
    star2 = Star(x=-50, y=100, size=350, points=7, color="grey")
    star2.draw()

    # Зміна параметрів зірки та малювання нової зірки
    star3 = Star(x=-400, y=-100, size=300, points=9, color="lightblue")
    star3.draw()

    turtle.done()

if __name__ == "__main__":
    main()
