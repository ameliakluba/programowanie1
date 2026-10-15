cena = float(input("Podaj cenę produktu: "))
ilosc = int(input("Podaj ilość sztuk: "))
koszt_dostawy = 12
wartosc = cena * ilosc

if wartosc >= 100:
    koszt_dostawy = 0
else:
    koszt_dostawy = 12

razem = wartosc + koszt_dostawy

print("Wartość produktów:", wartosc, "zł")
print("Koszt dostawy:", koszt_dostawy, "zł")
print("Kwota do zapłaty:", razem, "zł")
