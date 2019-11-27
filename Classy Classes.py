#It is my decision to the task but but it is not correct for CodeWars
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        return "{} age is {}".format(self.name, self.age)
