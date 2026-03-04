import math

while True:
    luku = int(input("Syötä kokonaisluku tai syöttämällä 0: "))

    if luku == 0:
        print("Ohjelma lopetettu :)")
        break

    elif luku < 0:
        print("Virheellinen numero")

    else:
        tulos = math.sqrt(luku)
        print(f"Luvun {luku} neliöjuuri on {tulos}")