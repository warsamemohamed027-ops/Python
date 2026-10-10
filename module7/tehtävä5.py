
def remove_odd_numbers(numbers):
    even_numbers = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)

    return even_numbers

numbers = [1, 2, 3, 4, 5, 6]
result = remove_odd_numbers(numbers)

print("Original list:", numbers)
print("Even numbers:", result)
