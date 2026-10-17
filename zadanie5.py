<<<<<<< HEAD
czas = int(input("Podaj czas parkowania w godzinach: "))

if czas <= 0:
    print("Nieprawidłowy czas")
else:
    if czas <= 1:
        oplata = 5
    elif czas <= 3:
        oplata = 12
    elif czas <=6:
        oplata = 20
    else:
        oplata = 30

print("Czas postoju:", czas, "h")
print("Opłata za parking:", oplata, "zł")
=======
haslo = "Python123"
proby = 0

while proby >= 0 and (proby < 3):
    podane_haslo = input("Podaj hasło: ")
    pozostale_proby = 2 - proby
    proby += 1
    if podane_haslo == haslo:
        print("Logowanie udane!")
        break
    else:
        print(f"Niepoprawne hasło. Pozostałe próby: {pozostale_proby}")
>>>>>>> d9f1b38 (lista 2)
