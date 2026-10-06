import random

def dice_roll(number_of_sides):
   

   return  random.randint(1,number_of_sides)
number_of_sides = int(input("How many sides does the dice have? "))

while True:
   result=dice_roll(number_of_sides)
   print(result)

   if result==number_of_sides:
      break