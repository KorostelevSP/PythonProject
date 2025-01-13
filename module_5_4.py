# "Различие атрибутов класса и экземпляра"
class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        # if cls.houses_history is None:
        #     cls.houses_history = houses_history
        if args[0] in cls.houses_history:
            print('этот элемент уже есть в списке')
        else:
            cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self,new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for i in range(1,new_floor+1):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if not isinstance(other, House):
            raise ArithmeticError("Правый операнд должен объектом House")
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if not isinstance(other, House):
            raise ArithmeticError("Правый операнд должен объектом House")
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if not isinstance(other, House):
            raise ArithmeticError("Правый операнд должен объектом House")
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if not isinstance(other, House):
            raise ArithmeticError("Правый операнд должен объектом House")
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if not isinstance(other, House):
            raise ArithmeticError("Правый операнд должен объектом House")
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if not isinstance(other, House):
            raise ArithmeticError("Правый операнд должен объектом House")
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if not isinstance(value, int):
            raise ArithmeticError("Операнд должен быть типом int")
        self.number_of_floors += value
        return self

    def __iadd__(self, value):
        if not isinstance(value, int):
            raise ArithmeticError("Операнд должен быть типом int")
        return self.__add__(value)

    def __radd__(self, value):
        if not isinstance(value, int):
            raise ArithmeticError("Операнд должен быть типом int")
        return self.__add__(value)

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

class Example:

    def __new__(cls, *args, **kwargs):
        print(args)
        print(kwargs)
        # super.__new__(cls)
        return object.__new__(cls)


    def __init__(self, first, second, third):
        print(first)
        print(second)
        print(third)

    # def __init(self,*args, **kwargs):
    #    # создание в объекте именованных параметров
    #     self.args = args
    #     for key, values in kwargs.items():
    #         setattr(self,key,values)

ex = Example('data', second=25, third=3.14)

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)

h2 = House('ЖК Акация', 20)
print(House.houses_history)

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)