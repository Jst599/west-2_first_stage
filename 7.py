class goods:
    def __init__(self, order, name, price, num, left_num):
        self.__order = order
        self.__name = name
        self.__price = price
        self.__num = num
        self.__left = left_num

    def display(self):
        print(self.__order)
        print(self.__name)
        print(self.__price)
        print(self.__num)
        print(self.__left)

    def setdata(self):
        income = self.__price * (self.__num - self.__left)
        print(income)
        self.__init__(self.__order, self.__name, self.__price, self.__num, self.__left)
        self.display()

store = goods(1, "a", 2, 3, 1)
store.setdata()



