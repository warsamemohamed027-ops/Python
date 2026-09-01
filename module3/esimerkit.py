import random
# base= float(input("give me the base of a triangle"))
# height=float(input("give me the height of a triangle"))
# area = base * height / 2
# print (f" the area of a triangle is : {area}")
secret_number= random.randint(1,10)
guess=int (input("guess the number between 1 and 10"))
if guess == secret_number:
    print("you guessed it right")

else: 
 print("you guessed it wrong")
