import math
sukupuoli = input("Anna sukupuoli (mies/nainen): ")
veriarvo= float(input("anna veriarvo"))
if sukupuoli == "mies" and veriarvo < 134:
    print(" veriarvo on liaan alhainen")
elif sukupuoli == "mies" and veriarvo >= 134 and veriarvo <= 195:
    print("veriarvo on normaali")
elif sukupuoli == "mies" and veriarvo > 195:
    print("veriarvo on liian korkea")
elif sukupuoli == "nainen" and veriarvo <117:
    print("veriarvo on liian alhainen")
elif sukupuoli == "nainen" and veriarvo >= 117 and veriarvo <=175:
    print("veriarvo on normaali")
elif sukupuoli == "nainen" and veriarvo > 175:
    print("veriarvo on liian korkea")
else:
    print("sukupuoli on virheellinen")