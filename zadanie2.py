<<<<<<< HEAD
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
=======
studenci = int(input("Podaj liczbę studentów: "))

zaliczyli = 0
l_punkty = []

for i in range(1, studenci + 1):
    print()

    nazwisko = input(f"Nazwisko studenta {i}: ")
    punkty = int(input("Punkty: "))
    l_punkty.append(punkty)

    if  punkty < 0 or (punkty > 100):
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

    if punkty >= 50:
        zaliczyli += 1

    srednia = sum(l_punkty)/ studenci
    l_punkty.sort()

print("Średnia: ", srednia)
print("Najwyższy wynik: ", max(l_punkty))
print("Najniższy wynik: ", min(l_punkty))
print("Liczba studentów, którzy zaliczyli: ", zaliczyli)
print("Wyniki rosnąco: ", l_punkty)
>>>>>>> d9f1b38 (lista 2)
