poczatek=int(input("Podaj początek zakresu:"))
koniec=int(input("Podaj koniec zakresu:"))

parzyste = 0

for i in range(poczatek, koniec+1):
    if i % 2 == 0:
        print(i, "- Parzysta" )
        parzyste += 1
    else:
        print(i, "- Nieparzysta")

print ("Liczba liczb parzystych: ",parzyste)