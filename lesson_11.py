# 1.  Спробуйте переписати наступний код через map.
# Він приймає список реальних імен і замінює їх хеш-прізвищами,
# використовуючи  більш надійний метод-хешування.

# names = ['Sam', 'Don', 'Daniel']
# for i in range(len(names)):
#     names[i] = hash(names[i])
# print(names)

# names = ['Sam', 'Don', 'Daniel']
# hash_name = map(hash,names)
# print(list(hash_name))


#2.  Вивести список кольору “red”,
# який найчастіше зустрічається в даному списку
# [“red”, “green”, “black”, “red”, “brown”, “red”, “blue”, “red”, “red”, “yellow” ]
# використовуючи функцію filter.
# colors = ["red", "green", "black", "red", "brown", "red", "blue", "red", "red", "yellow" ]
# col_fix = filter(lambda x : x == "red", colors)
# print(list(col_fix))


# 3. Всі ці числа в списку мають стрічковий тип даних, наприклад  [‘1’,’2’,’3’,’4’,’5’,’7’],
# перетворити цей список  в список, всі числа якого мають тип даних integer:
# 1)  використовуючи метод  append
# lst_str = ['1','2','3','4','5','7']
# lst_int =[]
# for i in lst_str:
#     lst_int.append(int(i))
# print(lst_str)
# print(lst_int)
#
# # 2)  використовуючи метод  map
# lst_str = ['1','2','3','4','5','7']
# lst_int =map(int , lst_str)
# print(lst_str)
# print(list(lst_int))


#4. Перетворити список, який містить милі ,  в список, який містить кілометри (1 миля=1.6 кілометра)
#a) використовуючи функцію map
# lst_km = [12, 25, 64]
# lst_m = map()


#b) використовуючи функцію map та lambda
# lst_m = [12, 25, 64]
# lst_km = map(lambda i: i * 1.6 , lst_m)
# print(list(lst_km))


#5. Знайти найбільший елемент в списку  використовуючи функцію reduce
# from functools import reduce
# nums = [8, 2, 3, 6, 10, 1, 4]
#
# res = reduce(lambda a,b: a if a>b else b, nums)
# print(res)

# 6. Перепишіть наступний код, використовуючи map, reduce і filter. Filter приймає функцію і колекцію.
# Повертає колекцію тих елементів, для яких функція повертає True.
# people = [{'name': 'Sam', 'height': 160}, {'name': 'Alex', 'height': 80}, {'name': 'Jack'}]
# height_total = 0
# height_count = 0
# for person in people:
#     if 'height' in person:
#         height_total += person['height']
#         height_count += 1
# print(height_total)

#map
# people = [{'name': 'Sam', 'height': 160}, {'name': 'Alex', 'height': 80}, {'name': 'Jack'}]
# height_total = map(lambda i: i["height"] if "height" in i else 0, people)
# print (sum(list(height_total)))


#reduse
from functools import reduce
people = [{'name': 'Sam', 'height': 160}, {'name': 'Alex', 'height': 80}, {'name': 'Jack'}]
height_total = reduce(lambda i, j: i["height"] if "height" in i else 0, people)
print (sum(list(height_total)))


