class Student:
    grade = 6
    age = 11
    teacher = "Mr. Who"

    def standUp(self):
        self.say()

    def say(self):
        print("Hello Teacher")

    def __init__(self, grade):
        self.grade = grade



student = Student(6)
student.standUp()

class Dog:
    name = "Henry"
    dogType = "Pug"
    colour = "purple"
    food = "bone"

    def __init__(self, name, dogType, colour, food):
        self.name = name
        self.dogType = dogType
        self.colour = colour
        self.food = food

    def bark(self):
        print("I love" + self.food)

    def description(self):
        print("My name is " + self.name + " I am a " + self.colour + " " + self.dogType)
pug = Dog("Henry", "Pug", "brown", " watermelon")
pug.description()
pug.bark()
        

    
