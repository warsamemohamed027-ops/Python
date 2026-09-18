import random
dice= int(input("kuinka monta noppaa heitetään?"))
summa= 0

for i in range (dice):
 roll= random.randint(1,6)
 summa= summa + roll

 print(summa)