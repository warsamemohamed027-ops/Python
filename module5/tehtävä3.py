number = float(input("give a number:"))

smallest = float(number)
largest = float(number)

while number != "":
    number = float(number)
    if number < smallest:
        smallest = number
    if number > largest:
        largest = number
    number = input("give a number:")
print("Program ends")

print(f"Smallest number {smallest}")
print(f"Largest number {largest}")     