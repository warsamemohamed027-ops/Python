secret_number = 7
number = int(input("Guess the secret number between 1 and 10: "))
while number <= 7:
   print("too low")
   number = int(input("Guess the secret number between 1 and 10: "))
if number > 7:
   print("too high")
else:
    print("correct the answer was 7:")