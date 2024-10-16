# Клас "Страва"
class Dish:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price} грн"

# Клас "Стіл"
class Table:
    def __init__(self, table_number):
        self.table_number = table_number

    def __str__(self):
        return f"Стіл №{self.table_number}"

# Клас "Ресторан"
class Restaurant:
    def __init__(self, name, tables):
        self.name = name
        self.tables = [Table(i+1) for i in range(tables)]  # Генеруємо список столів

    def __str__(self):
        return f"Ресторан '{self.name}' має {len(self.tables)} столів"

# Клас "Замовлення"
class Order:
    def __init__(self, table, dishes):
        self.table = table  # Стіл, за яким зроблено замовлення
        self.dishes = dishes  # Список об'єктів класу Dish

    def total_price(self):
        # Підрахунок загальної суми замовлення
        return sum(dish.price for dish in self.dishes)

    def __str__(self):
        dishes_str = "\n".join([str(dish) for dish in self.dishes])
        return f"{self.table}\nЗамовлення:\n{dishes_str}\nЗагальна сума: {self.total_price()} грн"


# Демонстрація роботи з класами
def main():
    # Створюємо ресторан з 5 столами
    restaurant = Restaurant(name="Українська кухня", tables=5)
    print(restaurant)

    # Створюємо кілька страв
    dish1 = Dish(name="Борщ", price=120)
    dish2 = Dish(name="Вареники", price=80)
    dish3 = Dish(name="Котлета по-київськи", price=150)

    # Створюємо замовлення для столу №3
    order1 = Order(table=restaurant.tables[2], dishes=[dish1, dish2])

    # Створюємо ще одне замовлення для столу №1
    order2 = Order(table=restaurant.tables[0], dishes=[dish3, dish2])

    # Виводимо інформацію про замовлення
    print("\n--- Замовлення 1 ---")
    print(order1)

    print("\n--- Замовлення 2 ---")
    print(order2)


if __name__ == "__main__":
    main()
