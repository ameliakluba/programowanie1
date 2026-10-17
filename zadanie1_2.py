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