print("====KALKULATOR====")

while True:
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Potęgowanie")
    print("6. Średnia z podanych liczb")
    print("0. Zakończ")
    print("==================")

    opcja = int(input("Wybierz opcję: "))

    if opcja == 1:
        p_l_dod = float(input("Pierwsza liczba: "))
        d_l_dod = float(input("Druga liczba: "))

        wynik_dod = p_l_dod + d_l_dod

        print(f"Wynik: {p_l_dod} + {d_l_dod} = {wynik_dod}")

    elif opcja == 2:
        p_l_odj = float(input("Pierwsza liczba: "))
        d_l_odj = float(input("Druga liczba: "))

        wynik_odj = p_l_odj - d_l_odj

        print(f"Wynik: {p_l_odj} - {d_l_odj} = {wynik_odj}")

    elif opcja == 3:
        p_l_mn = float(input("Pierwsza liczba: "))
        d_l_mn = float(input("Druga liczba: "))
        
        wynik_mn = p_l_mn * d_l_mn

        print(f"Wynik: {p_l_mn} * {d_l_mn} = {wynik_mn}")


    elif opcja == 4:
        p_l_dz = float(input("Pierwsza liczba: "))
        d_l_dz = float(input("Druga liczba: "))
    
        wynik_dz = p_l_dz/ d_l_dz

        if d_l_dz == 0:
            print("Nie można dzielić przez zero.")
        else:
            print(f"Wynik: {p_l_dz}:{d_l_dz} = {wynik_dz}")
        

    elif opcja == 5:
        p_l_pot = int(input("Pierwsza liczba: "))
        d_l_pot = int(input("Druga liczba: "))
            
        wynik_pot = p_l_pot ** d_l_pot

        print(f"Wynik: {p_l_pot}^ {d_l_pot} = {wynik_pot}")

    elif opcja == 6:
        liczby = []

        ilosc_liczb = int(input("Ile liczb?: "))

        for i in range(ilosc_liczb):
            indeks = i + 1
            liczba = int(input(f"Liczba {indeks}: "))
            liczby.append(liczba)

            srednia = sum(liczby)/ilosc_liczb

        print(f"Średnia: {srednia}") 

    elif opcja < 0 or (opcja > 6):
        print("Nieprawidłowe dane")
        

    else:
        break
        

