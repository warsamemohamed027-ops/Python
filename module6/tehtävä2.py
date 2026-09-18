numbers=[]
while True:
 number=input("enter a number")
 if number == "":
  break 
 number=int(number)
 numbers.append(number)
 numbers.sort(reverse=True)
 numbers[:5]
 print(numbers)