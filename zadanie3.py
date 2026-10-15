cena = float(input("Podaj cenę produktu: "))
rabat = float(input("Podaj rabat (%): "))

kwota_rabatu = cena * rabat/100
cena_koncowa = cena - kwota_rabatu

if rabat >= 20:
    print("Duża promocja!")
else:
    print("Standardowa promocja")

print("Cena początkowa:", cena, "zł")
print("Kwota rabatu:", kwota_rabatu, "zł")
print("Cena końcowa:", cena_koncowa, "zł")
