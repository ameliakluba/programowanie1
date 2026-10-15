wysokosc = int(input("Podaj wysokość choinki: "))

for i in range(1, wysokosc + 1):
    spacje = wysokosc - i
    gwiazdki = 2 * i - 1
    print(" " * spacje + "*" * gwiazdki)

print(" " * (wysokosc - 1) + "*")