# import pyowm
#
# owm = pyowm.OWM('ef2206ff5da67de63306d0b143e20872')  # You MUST provide a valid API key
#
# # Have a pro subscription? Then use:
# # owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')
#
# # Search for current weather in London (Great Britain)
# observation = owm.weather_at_place('Lviv')
# w = observation.get_weather()
#                               # <Weather - reference time=2013-12-18 09:20,
#                               # status=Clouds>
#
# # Weather details
# w.get_wind()                  # {'speed': 4.6, 'deg': 330}
# w.get_humidity()              # 87
# w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
#
# # Search current weather observations in the surroundings of
# # lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
# observation_list = owm.weather_around_coords(-22.57, -43.12)
#
#
#
# inp = input("Enter your city: ")
# observation = owm.weather_at_place(inp)
# w = observation.get_weather()
#
# print("Speed of wind: {}".format(w.get_wind()["speed"]))
# print("Humidity: {}".format(w.get_humidity()))
# print("Middle temperature in Celsius: {}".format(w.get_temperature('celsius')['temp']))



#1.  Напишіть скрипт-гру, яка генерує випадковим чином число з діапазону чисел від 1 до 100
# і пропонує користувачу вгадати це число. Програма зчитує числа,
# які вводить користувач і видає користувачу підказки про те чи загадане число більше чи менше за введене користувачем.
# Гра має тривати до моменту поки користувач не введе число, яке загадане програмою, тоді друкує повідомлення привітання.
#(для виконання завдання необхідно імпортувати  модуль random, а з нього функцію randint()
# import random
# que = input("Do you want to play the game (Enter 'Yes' or 'No'): ")
# if que == "Yes":
#     num=random.randint(1,100)
#     inp = int(input("Enter number: "))
#     while inp != num:
#         if inp < num:
#             inp = int(input("Enter a larger number: "))
#         else:
#             inp = int(input("Enter smaller number: "))
#     print("Congratulations!!! You win")
# else:
#     print("Bye")


#2.  Напишіть скрипт, який обчислює площу прямокутника a*b, площу трикутника 0.5*h*a, площу кола pi*r**2.
#(для виконання завдання необхідно імпортувати  модуль math, а з нього функцію pow() та значення змінної пі).
# from math import pi
# from math import pow
# que = input("If you want to calculate the area of rectangle enter - 1,  triangle -2, circle -3: ")
# if que == "1":
#     inp_rt_a = int(input("Please enter side a: "))
#     inp_rt_b = int(input("Please enter side b: "))
#     print("The area of rectangle = {}".format(inp_rt_a*inp_rt_b))
# elif que == "2":
#     inp_tr_a = int(input("Please enter side a: "))
#     inp_tr_h = int(input("Please enter side h: "))
#     print("The area of triangle = {}".format(inp_tr_a * inp_tr_h*0.5))
# elif que == "3":
#     inp_ci_r = int(input("Please enter side r: "))
#     print("The area of circle = {}".format(pi*pow(inp_ci_r,2)))
# elif que == 1 or 2 or 3:
#     print("Please read the assignment again!")