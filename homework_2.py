
class Person:
    def __init__(self, name, birth_date, occupation ,higher_education):
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education
        self.name = name
    def introduce(self):
        print(f"меня зовут {self.name}, я родился {self.birth_date}, профессия: {self.occupation}, высшее образование {self.higher_education}" )
person1 = Person("Бекназар","12 января 2010","программист", False)




class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group = group
    def introduce(self):
        print(f"привет меня зовут {self.name}, я одногруппник Бекназара в группе {self.group}, я родился {self.birth_date}, работаю {self.occupation}")
classmate1 = Classmate("Айман", "18 мая 2009", "программистом", False, "103ПО2" )
classmate2 = Classmate("Нурсултан", "25 июля 2009", "программистом", False, "103ПО2" )

class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby
    def introduce(self):
        print(f"привет меня зовут {self.name}, я друг Бекназара, Я родился {self.birth_date}, мое хобби {self.hobby}, работаю {self.occupation} ")
friend1 = Friend("Давид", "27 августа 2009", "кассиром", False, "баскетбол")
friend2 = Friend("Саит",  "21 сентября 2009", "портным", False,  "видеоигры")
classmate1.introduce()
classmate2.introduce()
friend1.introduce()
friend2.introduce()
































