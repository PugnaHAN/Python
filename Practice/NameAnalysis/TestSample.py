class T():
    def __init__(self, a = 0, b = 0):
        self.__a__ = a
        self.__b__ = b

    @property
    def a(self):
        return self.__a__

    @property
    def b(self):
        return self.__b__

    def print_num(self):
        print("a is {0}, b is {1}".format(self.__a__, self.__b__))

    @classmethod
    def print_cls(cls):
        print(cls)


if __name__ == "__main__":
    t = T(1, 2)
    t.print_num()

    T.print_cls()