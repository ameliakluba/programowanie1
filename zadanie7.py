<<<<<<< HEAD
oszczednosci = float(input("Ile złotych odkładasz tygodniowo? "))
tygodnie = int(input("Przez ile tygodni? "))
suma = 0

for i in range(1,tygodnie+1):
  suma += oszczednosci
  print ("Tydzień", i, ":", suma, "zł")

print("Łączne oszczędności:", suma, "zł")
=======
magazyn = {"Mysz": 5, "Klawiatura": 3, "Monitor": 2}

print("1. Stan magazynu")
print("2. Przyjęcie towaru")
print("3. Wydanie towaru")
print("0. Zakończ")

while True:
    opcja = int(input("Wybierz opcję: "))

    if opcja == 1:
        if not magazyn:
            print("Magazyn jest pusty.")
        else:
            for idx, (produkt, ilosc) in enumerate(magazyn.items(), start=1):
                print(f"{idx}. {produkt}: {ilosc} szt.")

    elif opcja == 2:
        nowy_produkt = input("Nazwa produktu: ").capitalize()
        l_sztuk = int(input("Liczba sztuk: "))

        if nowy_produkt in magazyn:
            magazyn[nowy_produkt] += l_sztuk
            print("Zaktualizowano stan produktu.")
        else:
            magazyn[nowy_produkt] = l_sztuk
            print("Dodano produkt.")
    

    elif opcja == 3:
        produkt_do_wydania = input("Nazwa produktu: ").capitalize()
        
        if produkt_do_wydania in magazyn:
            l_sztuk_do_wydania = int(input("Liczba wydawanych sztuk: "))
            stan_magazynu = magazyn[produkt_do_wydania]
            if l_sztuk_do_wydania <= stan_magazynu:
                magazyn[produkt_do_wydania] -= l_sztuk_do_wydania
                print(f"Wydano {l_sztuk_do_wydania} szt.")
            else:
                print("Nieprawidłowa liczba sztuk.")
        else:
            print("Nieznany produkt.")

    elif opcja == 0:
        print("Do widzenia!")
        break

    else:
        print("Nieprawidłowe dane.")
>>>>>>> d9f1b38 (lista 2)
