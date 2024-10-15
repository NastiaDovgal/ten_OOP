# class Shop():
#     def __init__(self, shop_name, store_type):
#         self.shop_name = shop_name
#         self.store_type = store_type
#         self.number_of_units = 0
#
#     def describe_shop(self):
#         print(f"\t\tІм'я -> {self.shop_name};")
#         print(f"\t\tТип -> {self.store_type};")
#
#     def open_shop(self):
#         print("\t\tМагазин відкритий! Ласкаво просимо!")
#
#     def set_number_of_units(self, number_of_units):
#         self.number_of_units = number_of_units
#
#     def increment_number_of_units(self, increment):
#         self.number_of_units += increment
from shop_module import Shop

if __name__ == '__main__':
    print("Для екзепляру 'store':")
    store = Shop("Comfy", "техніка")

    print(f"\tАтрибут shop_name = '{store.shop_name}'")
    print(f"\tАтрибут store_type = '{store.store_type}'")
    print(f"\tАтрибут number_of_units = {store.number_of_units}")
    store.number_of_units = 11
    print(f"\tАтрибут number_of_units = {store.number_of_units}")
    store.set_number_of_units(15)
    print(f"\tАтрибут number_of_units = {store.number_of_units}")
    store.increment_number_of_units(5)
    print(f"\tАтрибут number_of_units = {store.number_of_units}")


    print("\tВиклик методу 'describe_shop': ")
    store.describe_shop()

    print("\tВиклик методу 'open_shop': ")
    store.open_shop()

    print("Для екзепляру 'store_two':")
    store_two = Shop("nike", "одяг")
    print("\tВиклик методу 'describe_shop': ")
    store_two.describe_shop()

    print("Для екзепляру 'all_shop':")
    all_shop = Shop("Apple", "техніка")
    print("\tВиклик методу 'describe_shop': ")
    all_shop.describe_shop()
