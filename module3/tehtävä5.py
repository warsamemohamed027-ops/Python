import math
leiviskät = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit:"))

leiviskä_naulat= leiviskät * 20
luodit_naulat= leiviskä_naulat *32 + luodit

grammaksi=luodit_naulat * 13.3
kilogrammaski= int(grammaksi /1000)

loput_grammat= grammaksi % 1000
print("massa nykymittojen mukaan:")
print("f(kilogrammaksi) kilogramma ja (loput_grammat : 2f) grammaa")