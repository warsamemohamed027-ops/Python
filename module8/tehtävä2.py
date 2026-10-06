names = set()
while True:
    name = input("what is ur name: ")
    if name == "":
        break
    
    if name in names:
        print("existing name")

    else:
        print("new name")
        names.add(name)

for name in names:
    print(names)