zadania = []

while True:
    print("1. Dodaj zadanie")
    print("2. Wyświetl zadania")
    print("3. Usuń zadanie")
    print("4. Liczba zadań")
    print("0. Zakończ")

    opcja = int(input("Wybierz opcję: "))
    
    if opcja == 1:
        zadanie = input("Podaj zadanie: ")
        zadania.append(zadanie)
    
    elif opcja == 2:
        if not zadania:
            print("Brak zadań.")
        else:
            for idx, zadanie in enumerate(zadania, start=1):
                print(f"{idx}. {zadanie}")
    
    elif opcja == 3:
        if not zadania:
            print("Brak zadań do usunięcia.")
        else:
            usuniecie = int(input("Podaj numer zadania do usunięcia: "))
            indeks = usuniecie - 1
            if 0 <= indeks < len(zadania):
                zadania.pop(indeks)
                print("Zadanie usunięte.")
            else:
                print("Brak zadań.")
    
    elif opcja == 4:
        print("Liczba zadań: ", len(zadania))
    
    elif opcja == 0:
        print("Do widzenia!")
        break
    
    else:
        print("Niepoprawne dane.")