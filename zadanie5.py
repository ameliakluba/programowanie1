czas = int(input("Podaj czas parkowania w godzinach: "))

if czas <= 0:
    print("Nieprawidłowy czas")
else:
    if czas <= 1:
        oplata = 5
    elif czas <= 3:
        oplata = 12
    elif czas <=6:
        oplata = 20
    else:
        oplata = 30

print("Czas postoju:", czas, "h")
print("Opłata za parking:", oplata, "zł")