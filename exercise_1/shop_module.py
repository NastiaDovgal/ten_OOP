class Shop():
    def __init__(self, shop_name, store_type):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = 0

    def describe_shop(self):
        print(f"\t\tІм'я -> {self.shop_name};")
        print(f"\t\tТип -> {self.store_type};")

    def open_shop(self):
        print("\t\tМагазин відкритий! Ласкаво просимо!")

    def set_number_of_units(self, number_of_units):
        self.number_of_units = number_of_units

    def increment_number_of_units(self, increment):
        self.number_of_units += increment
