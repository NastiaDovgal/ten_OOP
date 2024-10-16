class Dish:
    def __init__(self, name, price):
        """
        Initializes a Dish object with a name and price.

        :param name: The name of the dish.
        :param price: The price of the dish.
        """
        self.name = name
        self.price = price


class Table:
    def __init__(self, number):
        """
        Initializes a Table object with a table number.

        :param number: The table number.
        """
        self.number = number


class Order:
    def __init__(self, table, dishes):
        """
        Initializes an Order object with a table and a list of dishes.

        :param table: The table object.
        :param dishes: A list of Dish objects.
        """
        self.table = table
        self.dishes = dishes

    def total_price(self):
        """
        Calculates the total price of the order.

        :return: The total price of the order.
        """
        return sum(dish.price for dish in self.dishes)


class Restaurant:
    def __init__(self, name):
        """
        Initializes a Restaurant object with a name.

        :param name: The name of the restaurant.
        """
        self.name = name
        self.tables = []
        self.orders = []

    def add_table(self, table):
        """
        Adds a table to the restaurant.

        :param table: The table object.
        """
        self.tables.append(table)

    def add_order(self, order):
        """
        Adds an order to the restaurant.

        :param order: The order object.
        """
        self.orders.append(order)

    def print_orders(self):
        """
        Prints all orders in the restaurant.
        """
        for order in self.orders:
            print(f"Table {order.table.number}:")
            for dish in order.dishes:
                print(f"  {dish.name}: {dish.price}")
            print(f"  Total: {order.total_price()}")
            print()


# Create a restaurant
restaurant = Restaurant("My Restaurant")

# Create tables
table1 = Table(1)
table2 = Table(2)
restaurant.add_table(table1)
restaurant.add_table(table2)

# Create dishes
dish1 = Dish("Pizza", 10.99)
dish2 = Dish("Salad", 8.99)
dish3 = Dish("Burger", 12.99)

# Create orders
order1 = Order(table1, [dish1, dish2])
order2 = Order(table2, [dish3])
restaurant.add_order(order1)
restaurant.add_order(order2)

# Print orders
restaurant.print_orders()
