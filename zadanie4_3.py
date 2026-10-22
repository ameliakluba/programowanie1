print("==== MÓJ BUDŻET ====")

while True:
    print("1. Dodaj przychód")
    print("2. Dodaj wydatek")
    print("3. Wyświetl historię operacji")
    print("4. Wyświetl stan konta")
    print("5. Podsumowanie finansowe")
    print("6. Usuń operację")
    print("0. Zakończ")
    print("==================")

    opcja = int(input("Wybierz opcję: "))
    portfel = []

    if opcja == 1:
        przychody = []
        input("Opis: ")
        kwota_przychodu = int(input("Kwota: "))
        
        portfel.append(kwota_przychodu)
        przychody.append(kwota_przychodu)

        print("Dodano przychód.")

    elif opcja == 2:
            wydatki = []
            input("Opis: ")
            kwota_wydatku = int(input("Kwota: "))
            wydatek = kwota_wydatku * (-1)

            portfel.append(wydatek)
            wydatki.append(kwota_wydatku)

            print("Dodano wydatek.")

    elif opcja == 4:
         suma_portfela = sum(portfel)
         print(f"Stan konta: {suma_portfela} zł")

    elif opcja == 5:
         suma_przychodow = sum(przychody)
         suma_wydatkow = sum(wydatki)
         bilans = suma_przychodow - suma_wydatkow

         if bilans < 0:
              bilans * (-1)

         print(f"Suma przychodów: {suma_przychodow}")
         print(f"Suma wydatków: {suma_wydatkow}")
         print(f"Bilans: {bilans}")
         print(f"Największy wydatek: {max(wydatki)}")

    elif opcja == 6:
         usuniecie = int(input("Podaj numer operacji do usuniecia: "))
        

    elif opcja == 0:
        break

    else:
        print("Nieprawidłowe dane.")