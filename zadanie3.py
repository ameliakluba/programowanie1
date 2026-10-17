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
    
    