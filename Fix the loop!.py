def list_animals(animals):
    lst = ''
    num=1
    for i in animals:
        lst += str(num) + '. ' + i + '\n'
        num+=1
    return lst