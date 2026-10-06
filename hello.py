# class Isä():
#     def __init__(self, auto):
#         self.auto = auto


# class Äiti():
#     def __init__(self, linna):
#         self.linna = linna


# class Minä(Isä, Äiti):
#     def __init__(self, auto, linna, personallisuus):
#         Isä.__init__(self, auto)
#         Äiti.__init__(self, linna)
#         self.personallisuus = personallisuus

# minä=Minä("Wolkswagen" , "suomenlinna", " rohkea")

# print(minä.auto)
# print(minä.linna)
# # print(minä.personallisuus)
# class Dog:
#     def __init__(self,name,age,owner):

#         self.name=name
#         self.age=age
#         self.owner=owner


#     def bark(self,):

          
#           print("dog barked woof")

#     def introduce(self,):

#          print(f"my name is {self.name} and i am {self.age} years old")


#     def birthday(self):
#      self.age+=1

# class Owner:
#        def __init__(self,name):
#             self.name =name

# owner1= Owner("Ali")

# Dog1=Dog("bro",16,owner1)
# Dog2=Dog("yolo", 18, owner1)





# print(Dog1.owner.name)


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def introduce(self):
        print(f"my name is {self.name} and i am {self.age} years old")
        


class Student(Person):
    def __init__(self,name, age,school):
        
        self.school=school
        self.age=age
        self.name=name

    def study(self):
        print("opiskelija opiskelee")

class Teacher(Person):

    def __init__(self ,name ,age,subject):

        
        self.subject=subject
        self.age=age
        self.name=name

    def teach(self):
        print("opettaja opettaa")

student1 = Student("Ali", 17, "Omnia")
teacher1 = Teacher("Sara", 35, "Python")

student1.introduce()
student1.study()
teacher1.introduce()
teacher1.teach()

