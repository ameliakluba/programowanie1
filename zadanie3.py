<<<<<<< HEAD
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
=======
napoje = ["woda", "sok", "cola"]
ceny = [3, 5, 6]

suma = 0

i = 0

while i < len(napoje):
    print(f"{i + 1}. {napoje[i]} - {ceny[i]} zł")
    i += 1
print("0. Zakończ")

while True:
    wybor = int(input("Wybierz opcję: "))
    indeks = wybor - 1
    print(f"Wybrano: {napoje[indeks]}, cena: {ceny[indeks]} zł")
    if wybor == 0:
        print("Łącznie do zapłaty:", suma, "zł")
        break
    
    if 0 <= indeks < len(napoje):
        koszt = ceny[indeks]
        suma += koszt
    else:
        print("Niepoprawny numer")
    
    
>>>>>>> d9f1b38 (lista 2)
