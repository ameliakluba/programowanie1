print("====BIBLIOTEKA====")

while True:
    print("1. Dodaj książkę")
    print("2. Wyświetl wszystkie ksiązki")
    print("3. Wypożycz książkę")
    print("4. Zwróc książkę")
    print("5. Usuń książkę")
    print("0. Zakończ")
    print("==================")

    ksiazki = []
        
    opcja = int(input("Wybierz opcję: "))

    if opcja == 1:
        tytul = input("Tytuł: ")
        autor = input("Autor: ")

        print("Książka dodana.")


         

    elif opcja == 3:
            tytul = input("Tytuł: ")
            autor = input("Autor: ")
    
            print("Książka wypożyczona.")

    elif opcja == 4:
            tytul = input("Tytuł: ")
            autor = input("Autor: ")
    
            print("Książka zwrócona.")

    
    elif opcja == 0:
        break

    else:
        print("Nieprawidłowe dane.")