class Human:
    def __init__(self, name):
        self.name = name
class Male(Human):
    def __init__(self, name, age):
        self.name = name
        self.gender = "Male"
        self.age = age
    def speak(self):
        return f"Hi! My name is {self.name}!"
class Female(Human):
    def __init__(self, name, age):
        self.name = name
        self.gender = "Female"
        self.age = age
    def speak(self):
        return f"Hey! I'm {self.name}!"
male = Male("Ivan", 30)
female = Female("Maria", 25)
print(male.name)
print(female.name)
print(male.speak())
print(female.speak())
print(male.age)
print(female.age)
