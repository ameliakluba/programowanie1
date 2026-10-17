<<<<<<< HEAD
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
=======
zakupy = []
ilosc = int(input("Podaj liczbę produktów: "))

for i in range(1, ilosc + 1):
    print()
    produkt = input(f"Produkt{i}: ",)

    zakupy.append(produkt)

print("Lista:", zakupy)
print("Liczba produktów: ", ilosc)

usuniecie = input(f"Produkt do usunięcia: ").lower()
zakupy.remove(usuniecie)

print("Nowa lista:", zakupy)
>>>>>>> d9f1b38 (lista 2)
