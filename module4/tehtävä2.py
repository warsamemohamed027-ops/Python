hytti_luokka = input("anna hyttiluokka")
if hytti_luokka == "LUX":
    print("parvekkeellinen hytti yläkannella")
elif hytti_luokka == "A":
    print("ikkunallinen hytti autokannen yläpuolella")
elif hytti_luokka == "B":
    print("ikkunaton hytti autokannen yläpuolella")
elif hytti_luokka == "C":
    print("ikkunaton hytti autokannen alapuolella")
else:
    print("virheellinen hyttiluokka")