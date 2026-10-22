

while True:
    print("==== KSIĄŻKA KONTAKTÓW ====")
    print("1. Dodaj kontakt")
    print("2. Wyświetl wszystkie kontakty")
    print("3. Wyszukaj kontakt")
    print("4. Edytuj kontakt")
    print("5. Usuń kontakt")
    print("0. Zakończ")
    print("==========================")

    
    opcja = int(input("Wybierz opcję: "))

    kontakty = {}

    if opcja == 1:
        imie = input("Imię: ")
        nazwisko = input("Nazwisko: ")
        nr = int(input("Telefon: "))


        print("Kontakt dodany.")

    elif opcja < 0 or (opcja > 5):
            print("Nieprawidłowe dane")
            
    
    else:
        break