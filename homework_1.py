class Person:
    def __init__(self, name, birth_date, occupation ,higher_education):
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education
        self.name = name
    def introduce(self):
        print(f"меня зовут {self.name}, я родился {self.birth_date}, профессия: {self.occupation},высшее образование {self.higher_education}" )


person1 = Person("Бекназар","12 января 2010","программист", False)
person2 = Person("Эмир", "6 сентября 1997", "экономист", True)
person3 = Person("Эмиль", "28 мая 1989", "юрист", True)
print(person1.name,person1.birth_date, person1.occupation, person1.higher_education)
print(person2.name,person2.birth_date, person2.occupation, person2.higher_education)
print(person3.name,person3.birth_date, person3.occupation, person3.higher_education)
person1.introduce()
person2.introduce()
person3.introduce()



















