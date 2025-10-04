class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def myfunc(self):
        print(f"Hello, my name is {self.name}, and my student ID is {self.id}.")
