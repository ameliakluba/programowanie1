punkty = int(input("Podaj liczbę punktów:"))

if punkty < 0 or punkty > 100:
    print("Niepoprawne dane")
elif punkty >= 90:
    ocena = 5.0
elif punkty >= 80:
    ocena = 4.5
elif punkty >= 70:
    ocena = 4.0
elif punkty >= 60:
    ocena = 3.5
elif punkty >= 50:
    ocena = 3.0
else:
    ocena = 2.0

if 0 <= punkty <= 100:   
    print("Liczba punktów:", punkty)
    print("Ocena:", ocena)