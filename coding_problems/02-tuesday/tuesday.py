class Animal:
    def __init__(self, name: str):
        self.name = name

class Cat(Animal):
    def make_noise(self):
        print('meow')

class Dog(Animal):
    def make_noise(self):
        print('woof')

my_dog = Dog('Rex')
my_cat = Cat('Snowdrop')

print(isinstance(my_dog, Animal))