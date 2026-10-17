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