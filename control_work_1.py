class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def set_name(self, name):
        self.__name = name
    def set_age(self, age):
        self.__age = age
    def make_sound(self):
        pass
class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def make_sound(self):
        print("gavgav")
class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def make_sound(self):
        print("meowmeow")
Dog1 = Dog("", 0)
Cat1 = Cat("",0)
Dog1.set_name("sharik")
Dog1.set_age(20)
Cat1.set_name("Murzik")
Cat1.set_age(3)
print(Dog1.get_name())
print(Dog1.get_age())
Dog1.make_sound()
print(Cat1.get_name())
print(Cat1.get_age())
Cat1.make_sound()




































