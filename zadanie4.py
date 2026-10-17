<<<<<<< HEAD
wiek = int(input("Podaj wiek:"))

if wiek < 18 and (wiek > 12):
    zgoda = input("Czy masz zgodę opiekuna? (tak/nie)").lower()

dokument_tozsamosci = input("Czy masz dokument tożsamości? (tak/nie)").lower()

if dokument_tozsamosci == "tak" and (wiek >= 18 or (wiek >= 13 and zgoda == "tak")):
    print("Wypożyczenie możliwe")
else:
    print("Wypożyczenie niemożliwe")
    
=======
temperatury = []
pow_sredniej = []

for i in range(7):
    numer = i + 1
    temperatura = int(input(f"Dzień {numer}: "))
    temperatury.append(temperatura)
    srednia = sum(temperatury)/ 7
    if temperatura > srednia:
        pow_sredniej.append(temperatura)

l_dni = len(pow_sredniej)

print("Średnia:", srednia, "C")
print("Najwyższa:", max(temperatury), "C")
print("Najniższa:", min(temperatury), "C")
print("Powyżej średniej:", pow_sredniej)
print("Liczba dni:", l_dni)
>>>>>>> d9f1b38 (lista 2)
