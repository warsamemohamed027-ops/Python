class Merirosvolaiva:

    def __init__(self, nimi, tykkien_maara, miehiston_maara, kulta=0):
        self.nimi = nimi
        self.tykkien_maara = tykkien_maara
        self.miehiston_maara = miehiston_maara
        self.kulta = kulta

    def loyda_aarre(self, maara):
        self.kulta += maara

    def meneta_kultaa(self, maara):
        self.kulta -= maara


laiva = Merirosvolaiva("The Black Pearl", 12, 40)

laiva.loyda_aarre(200)
laiva.loyda_aarre(75)
laiva.meneta_kultaa(100)

print("Nimi:", laiva.nimi)
print("tykkien määrä", laiva.tykkien_maara)
print("miehiston määrä", laiva.miehiston_maara)
print("kullan määrä", laiva.kulta)

