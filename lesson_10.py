#1.  Напишіть програму, яка пропонує користувачу ввести ціле число
# і визначає чи це число парне чи непарне, чи введені дані коректні.
# a=False
# while a != True:
#     try:
#         a = int(input("Enter num: "))
#         if a % 2 ==0:
#             print("Even num")
#             a = True
#         else:
#             print("Not even num")
#             a = True
#     except ValueError:
#         print("Enter corect type !")
#2.  Напишіть програму, яка пропонує користувачу ввести свій вік,
# після чого виводить повідомлення про те чи вік є парним чи непарним числом.
# Необхідно передбачити можливість введення від’ємного числа,
# в цьому випадку згенерувати власну виняткову ситуацію.
# Головний код має викликати функцію, яка обробляє введену інформацію.

# class AgeError(Exception):
#     def __init__(self, data):
#         self.data = data
#     def __str__(self):
#         return repr(self.data)
#
# def check_age():
#     age=False
#     while age != True:
#         try:
#             age = int(input("Enter your age: "))
#             if age <= 0:
#                 raise AgeError("Number is less than 0 ")
#             elif age % 2 == 0:
#                 print("Even age")
#                 age = True
#             else:
#                 print("Not even age")
#                 age = True
#         except AgeError as e:
#             print("We obtain error: ", e.data)
#         except ValueError:
#             print ("Enter corect type !")
# print(check_age())


#3. Напишіть програму для обчислення частки двох чисел, які вводяться користувачем послідовно через кому,
# передбачити випадок ділення на нуль, випадки синтаксичних помилок та випадки інших виняткових ситуацій.
# Використати блоки else та finaly.
# correct_age = False
# while correct_age != True:
#     try:
#         age = int(input("Enter first num: ")), int(input("Enter second num: "))
#         fraction = age[0] / age[1]
#         print(int(fraction))
#         correct_age = True
#     except ValueError:
#         print("You did not enter a num")
#     except ZeroDivisionError:
#         print("You can't divide by zero")
#     else:
#         print("All right")
#     finally:
#         print("Program code finished")
#4. Написати  програму, яка аналізує введене число та в залежності від числа видає день тижня,
# який відповідає цьому числу (1 це Понеділок, 2 це Вівторок і т.д.) .
# Врахувати випадки введення чисел від 8 і більше, а також випадки введення не числових даних.
# correct_num = False
# while correct_num != True:
#     try:
#         days_of_the_week = {1 : "Понеділок", 2 : "Вівторок", 3 : "Середа", 4 : "Четвер", 5 : "Пятниця", 6 : "Субота", 7 : "Неділя" }
#         print(days_of_the_week[int(input("Enter num:"))])
#         correct_num = True
#     except ValueError:
#         print("You did not enter a num")
#     except KeyError:
#         print("The number must be from 1 to 7")
#     else:
#         print("All right")
#     finally:
#         print("Program code finished")




