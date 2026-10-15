studenci = int(input("Podaj liczbę studentów:"))

zaliczyli = 0

for i in range(1, studenci + 1):
    print()

    nazwisko = input(f"Nazwisko studenta {i}: ")
    punkty = int(input("Punkty: "))

    if punkty < 0 or (punkty > 100):
        print("Nieprawidłowa liczba punktów")
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
    
    print(nazwisko, "-", punkty, "pkt - ocena", ocena)



print("Liczba studentów, którzy zaliczyli: ", zaliczyli)