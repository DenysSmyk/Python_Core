#1.  Роздрукувати всі парні числа менші 100
# (написати два варіанти коду: один використовуючи цикл while,
# а інший з використанням циклу for).

# for i in range(1,100):
#     if i%2==0:
#         print(i)

# i=2
# while i < 100:
#     print(i)
#     i+=2

# print(list(range(2,100,2)))


#2.  Роздрукувати всі непарні числа менші 100.
# (написати два варіанти коду: один використовуючи оператор continue,
# а інший без цього оператора).

# for i in range(0,100):
#     if i%2!=0:
#         continue
#     print(i)


#3.  Перевірити чи список містить непарні числа.
#         (Підказка: використати оператор break)
# l = [1,2,3,4,5,6,7,8,9,10]
# for i in l:
#     if i%2==1:
#         break
#     print(i)


#4.  Створити список, який містить елементи цілочисельного типу,
# потім за допомогою циклу перебору змінити тип даних елементів
# на числа з плаваючою крапкою.
#(Підказка: використати вбудовану функцію float ()).

# l = [1,2,3,4,5,6,7,8,9,10]
# for i in l:
#     print(float(i),end=' ')


#5.  Вивести числа Фібоначі включно до введеного числа n, використовуючи цикли.
# (Послідовність чисел Фібоначі 0, 1, 1, 2, 3, 5, 8, 13 і т.д.)

# fib = []
# a=1
# b=1
# for i in range(1,10):
#     c=a+b
#     fib.append(c)
#     a=b
#     b=c
# print(fib)


#6.  Створити список, що складається з чотирьох елементів типу string.
# Потім, за допомогою циклу for, вивести елементи по черзі на екран.

# l =["a", "b", "c", "d"]
# for i in l:
#     print(i)


#7.  Змінити попередню програму так, щоб в кінці кожної букви
# елементів при виводі додавався певний символ, наприклад “#”.
#          (Підказка: цикл for може бути вкладений в інший цикл,
#          а також  треба використати функцію print(“ ”, end=”%”)).

# l =["a", "b", "c", "d"]
# for i in l:
#     print(i,end='#')

#8.  Юзер вводить число з клавіатури, написати скріпт,
# який визначає чи це число просте чи складне.

# num = int(input('Введіть число: '))
# r_num= list(range(2,num))
# for i in r_num:
#     if num % i == 0:
#         print('{} - cкладне число'.format(num))
#         break
# else:
#     print('{} - просте число'.format(num))


#9.  Знайти максимальну цифру дійсного числа.
# Дійсне число генеруємо випадковим чином за допомогою методу random() з модуля random
#(для цього підключаємо модуль random наступним чином from random import random)

# import random
#
# num = random.randint(10,1000)
# num_str = str(num)
# print(num)
# print(max(num_str))


#10.  Визначити чи введене слово паліндром,
# тобто чи воно читається однаково зліва направо і навпаки.

# num = input('Введіть число: ')
# if num == num[::-1]:
#     print('{} це число паліндром'.format(num))
# else:
#     print('{} це число не паліндром'.format(num))

