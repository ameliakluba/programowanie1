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