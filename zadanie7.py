oszczednosci = float(input("Ile złotych odkładasz tygodniowo? "))
tygodnie = int(input("Przez ile tygodni? "))
suma = 0

for i in range(1,tygodnie+1):
  suma += oszczednosci
  print ("Tydzień", i, ":", suma, "zł")

print("Łączne oszczędności:", suma, "zł")