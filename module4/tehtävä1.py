kuhan_pituus=float(input("anna kuhan pituus"))
if kuhan_pituus < 37: 
    puuttuu= 37 - kuhan_pituus
    print ("kuha on alamittainen")
    print("heitä kuha takaisin veteen")
    print("alimmasta mitasta puuttuu", puuttuu, "cm")
else:
    print(" kuha voidaan käyttää")