class Dog:
    def __init__(self, name, age,):
        self.name = name
        self.age = age
        

    def bark(self,):
        print("woof")

    def  birthday (self,age):
      self.age += 1
     
Dog1 = Dog("max", 5)

    
print(f"the dog name is {Dog1.name} , {Dog1.age} years old")

Dog1.birthday(1)

print(Dog1.age)