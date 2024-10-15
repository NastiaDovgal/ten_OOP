class Lock:
    def __init__(self):
        self.__combination = None

    def set_combination(self, combination):
        self.__combination = combination

    def open_lock(self, combination):
        if combination == self.__combination:
            print("Замок відкритий!")
        else:
            print("Неправильна комбінація. Замок залишається закритим.")

    def __check_combination(self, combination):
        return combination == self.__combination

    def __str__(self):  # Private method
        return f"Замок з комбінацією {self.__combination}"

    def reset_lock(self):
        self.__combination = None

if __name__ == '__main__':
    lock = Lock()
    lock.set_combination("1234")

    lock.open_lock("1234")
    lock.open_lock("5678")

    try:
        print(lock.__combination)
    except AttributeError:
        print("Помилка: неможливо отримати доступ до приватного атрибута __combination")


    print(lock._Lock__combination)

    try:
        lock._check_combination("1234")
    except AttributeError:
        print("Помилка: неможливо отримати доступ до приватного методу _check_combination")

    # print(lock._Lock__str())

    lock.reset_lock()
    lock.open_lock("1234")
