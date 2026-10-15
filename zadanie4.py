wiek = int(input("Podaj wiek:"))

if wiek < 18 and (wiek > 12):
    zgoda = input("Czy masz zgodę opiekuna? (tak/nie)").lower()

dokument_tozsamosci = input("Czy masz dokument tożsamości? (tak/nie)").lower()

if dokument_tozsamosci == "tak" and (wiek >= 18 or (wiek >= 13 and zgoda == "tak")):
    print("Wypożyczenie możliwe")
else:
    print("Wypożyczenie niemożliwe")
    