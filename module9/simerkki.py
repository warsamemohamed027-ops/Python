# class koira:
#      pass
# koira1= koira()

# koira1.nimi = "jasper"
# koira1.syntymävuosi = "2022"
# koira1.keskiarvo = 1


# class Koira:
#     koirien_määrä = 0

#     def __init__(self, nimi, vuosi, keskiarvo, huudahdus="haha"):
#         self.nimi = nimi
#         self.vuosi = vuosi
#         self.keskiarvo = keskiarvo
#         self.huudahdus = huudahdus
#         Koira.koirien_määrä += 1

#     def huuda(self, kerrat=1):
#         for i in range(kerrat):
#             print(self.huudahdus)

#     def itke(self):
#         print(f"{self.nimi} itkee: {self.huudahdus}")


# koira1 = Koira("jasper", "2022", "2", "Shit")
# koira2 = Koira("rekku", "2005", "5", "lets goo")

# print(f"{koira1.nimi} syntynyt vuonna {koira1.vuosi} ja hänen keskiarvo on {koira1.keskiarvo}, ja hän huutaa {koira1.huudahdus}")
# print(f"{koira2.nimi} syntynyt vuonna {koira2.vuosi} ja hänen keskiarvo on {koira2.keskiarvo} ja hän huutaa {koira2.huudahdus}")

# class Pelaaja:
#     def __init__(self, nimi, elämät=3, kolikot=0, pisteet=0):
#         self.nimi = nimi
#         self.elämät = elämät
#         self.kolikot = kolikot
#         self.pisteet = pisteet

# mario = Pelaaja("mario")

# print(f"{mario.nimi}\n{mario.elämät}\n{mario.kolikot}\n{mario.pisteet}")
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
