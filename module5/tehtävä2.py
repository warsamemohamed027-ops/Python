while True:
    inches = int(input("how many inches do you want to convert to centimeters?"))
    if inches < 0:
        print("you can't convert negative numbers")
        break
    centimeters = inches * 2.54
    print("your inches in centimeters is", centimeters)