#Task_2_a
num =2341
num_str = str(num)
dob = int(num_str[0]) * int(num_str[1]) * int(num_str[2]) * int(num_str[3])
print("Добуток:",dob)

#Task_2_b
num =2341
num_str = str(num)
revrs = int(num_str[::-1])
print("Реверсне число:",revrs)


#Task_2_c
num =2341
n_lst = list(str(num))
sort = sorted(n_lst)
str_sort = ''.join(sort)
print("Sort:",int(str_sort))

# Bubble Sort
a = [2,3,4,1 ]
for i in range(len(a)-1, 0, -1):
    for i in range(0, len(a)):
        for u in range(i):
            if a[u]>a[u+1]:
                b = a[u]
                a[u] = a[u+1]
                a[u+1] = b

print("Bubble sort:", a)