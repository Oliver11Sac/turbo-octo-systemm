class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Имя: {self.name}, Возраст: {self.age}")

    def say_hello(self):
        print(f"Привет, меня зовут {self.name}!")

p1 = Person("Ирина", 20)
p2 = Person("Олег", 22)
p3 = Person("Андрей", 25)

p1.show_info()
p2.show_info()
p3.show_info()

p1.say_hello()