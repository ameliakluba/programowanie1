temperatura = float(input("Podaj temperaturę: "))
domownicy = input("Czy ktoś jest w domu? (tak/nie)").lower()
okno = input("Czy okno jest otwarte? (tak/nie)").lower()

if okno == "tak":
    ogrzewanie = "WYŁĄCZONE"
    powod = "Okno jest otwarte"
elif domownicy == "tak" and temperatura < 20:
    ogrzewanie = "WŁĄCZONE"
    powod = "Temperatura poniżej 20 stopni"
elif domownicy == "nie" and temperatura < 16:
    ogrzewanie = "WŁĄCZONE"
    powod = "Temperatura poniżej 16 stopni"
else:
    ogrzewanie = "WYŁĄCZONE"
    powod = "Ogrzewanie niepotrzebne"

print("Ogrzewanie:", ogrzewanie)
print("Powód:", powod)