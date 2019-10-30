#Task_1_a
py_science = "Beautiful is better than ugly. \
    Explicit is better than implicit. \
    Simple is better than complex. \
    Complex is better than complicated. \
    Flat is better than nested. \
    Sparse is better than dense. \
    Readability counts. \
    Special cases aren't special enough to break the rules. \
    Although practicality beats purity. \
    Errors should never pass silently. \
    Unless explicitly silenced. \
    In the face of ambiguity, refuse the temptation to guess. \
    There should be one-- and preferably only one --obvious way to do it. \
    Although that way may not be obvious at first unless you're Dutch. \
    Now is better than never. \
    Although never is often better than *right* now. \
    If the implementation is hard to explain, it's a bad idea. \
    If the implementation is easy to explain, it may be a good idea. \
    Namespaces are one honking great idea -- let's do more of those! "

print(py_science.count('better'))
print(py_science.count('never'))
print(py_science.count('is'))

count_better = 0
for i in py_science.split():
    if i =='better':
        count_better+=1
print(count_better)

#Task_1_b
print(py_science.upper())

#Task_1_c
print(py_science.replace('i','&'))