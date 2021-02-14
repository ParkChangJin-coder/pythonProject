class Person2:
    name = "빡창"
    def say_hello2(self):
        print("Hi, my name is " + self.name)
p2 = Person2()
p2.say_hello2()



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self, to_name):
        print("Hello! " + to_name + " i'm " + self.name)

    def introduce(self):
        print("I and " + self.name + " and " + str(self.age) + " years old")

wonie = Person("Wonie", 15)
michael = Person("Michael", 21)
jenny = Person("Jenny", 30)

wonie.say_hello("chul")
michael.say_hello("young")
jenny.say_hello("miji")

wonie.introduce()
michael.introduce()
jenny.introduce()

class Police(Person):
    def arrest(self, to_arrest):
        print("You're under Arrest " + to_arrest)

class Programmer(Person):
    def programmer(self, to_program):
        print("I'm gonna make some " + to_program)

wonie2 = Person("워니", 20)
michael2 = Police("마이클", 22)
jenny2 = Programmer("제니", 23)

wonie2.introduce()
michael2.arrest("워니")
jenny2.programmer("이메일 클라이언트")

# wonie2.arrest("jenny")
# michael2.programmer("shop")





