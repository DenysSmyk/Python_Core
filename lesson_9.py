#1.  Створити клас машина з атрибутами name,  make, model та методами start та stop,
# які виводять інформацію про те що автомобіль стартував чи зупинився відповідно.
# class Car():
#     def __init__(self, name, model, color):
#         self.name = name
#         self.model = model
#         self.color = color
#     def start(self):
#         print("{} {} {} started".format(self.color, self.name, self.model))
#
#     def stop(self):
#         print("{} {} {} stoped".format(self.color, self.name, self.model))
#
# car_audi = Car("Audi", "RS6", "Black")
# car_bmw = Car("BMW", "M5", "Red")
# car_audi.start()
# car_audi.stop()
# car_bmw.start()
# car_bmw.stop()


#2.  Створити клас особа,  в якому конструктор встановлює ім’я,
# а метод info виводить повідомлення “Hello, my name is {ім’я конкретного екземпляра класу}”, а також створити клас автомобіль,
# в якому конструктор встановлює ім’я, а метод move виводить повідомлення
#{ім’я конкретного екземпляра класу}  moves at the speed {speed(цей параметр метод moveотримує як вхідний)} km / h

# class Person():
#     def __init__(self,name):
#         self.name = name
#
#     def info(self):
#         print("Hello, my name is {}".format(self.name))
#
# class Car():
#     def __init__(self, name):
#         self.name = name
#
#     def move(self, speed):
#         print("Max speed {} is {} km/h".format(self.name, speed))
#
#
# per_info = Person("Den")
# per_info.info()
#
# car_audi = Car("Audi")
# car_audi.move("320")


#3.  Створити клас особа,  в якому конструктор встановлює ім’я, вік. Використати в цьому класі геттери та сеттери,
# а також створити метод info, який виводить інформацію про ім’я та вік особи.
# А тоді створити клас працівник, який наслідується від класу особи і містить метод details,
# який на вхід отримує параметр про компанію, в якій працює працівник і цей метод виводить інформацію про те,
# що працівник з таким то іменем працює в такій то компанії.

# class Person():
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     @property
#     def p_name(self):
#         return self.__name
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         if age in range(1, 100):
#             self.__age = age
#         else:
#             print("Age is incorrect")
#
#     def info(self):
#         print("User name is {}. He is {} year old.".format(self.__name, self.__age))
#
# den = Person("Den", 19)
# den.age =-34
# den.info()
#
# class Worker(Person):
#     def __init__(self, __name, __age):
#         super(Worker, self).__init__(__name, __age)
#
#     def details(self, company):
#         print("{} working in {}".format(self.__name, company))
#
# w_den = Worker("Den", 19)
# w_den.details('Soft Serve')




#######################################################################################################################

# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     # @property
#     # def p_name(self):
#     #     return self.__name
#     #
#     # @property
#     # def age(self):
#     #     return self.__age
#     #
#     # @age.setter
#     # def age(self, age):
#     #     if age in range(1, 100):
#     #         self.__age = age
#     #     else:
#     #         print("Age is incorrect")
#
#     def info(self):
#         print("User name is {}. He is {} year old.".format(self.name, self.age))
#
# den = Person("Den", 19)
# den.age =-34
# den.info()
#
# class Worker(Person):
#     def __init__(self, name, age):
#         super(Worker, self).__init__(name, age)
#
#     def details(self, company):
#         print("{} working in {}".format(self.name, company))
#
# w_den = Worker("Den", 19)
# w_den.details('Soft Serve')

#4. Створити батьківський клас Figure з методами init: ініціалізується колір,
# get_color: повертає колір фігури, info: надає інформацію про фігуру та колір,
# від якого наслідуються такі класи як Rectangle, Square, які мають інформацію про ширину,
# висоту фігури, метод square, який знаходить площу фігури.
# class Figure():
#     def __init__(self, color, width, height):
#         self.color = color
#         self.width = width
#         self.height = height
#
# class Rectangle(Figure):
#     def info(self):
#         print("Rectangle color is {}, width {}, height {}".format(self.color, self.width, self.height))
#     def __mul__(self):
#         print("Rectangle area is {}".format(self.width * self.height))
#
# class Square(Figure):
#     def info(self):
#         print("Square color is {}, width {}, height {}".format(self.color, self.width, self.height))
#
#     def __mul__(self):
#         print("Square area is {}".format(self.width * self.height))
#
#
# rec = Rectangle("Black", 5,8)
# rec.info()
# rec.__mul__()
# squ = Rectangle("Red", 5,5)
# squ.info()
# squ.__mul__()


