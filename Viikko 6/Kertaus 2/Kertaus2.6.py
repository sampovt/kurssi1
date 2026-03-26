def summaa(a, b):
    return a + b

def erotus(a, b):
    return a - b

def tulo(a, b):
    return a * b

def osamaara(a, b):
    if b == 0:
        return "Virhe: Nollalla ei voi jakaa!"
    return a / b

while True:
    print("\n--- Valitse laskutoimitus ---")
    print("1: Yhteenlasku (+)")
    print("2: Vähennyslasku (-)")
    print("3: Kertolasku (*)")
    print("4: Jakolasku (/)")
    print("0: Lopeta ohjelma")

    valinta = input("Valintasi: ")

    if valinta == "0":
        print("Kiitos, nähdään taas!")
        break

    if valinta in ("1", "2", "3", "4"):
        try:
            luku1 = float(input("Anna ensimmäinen luku: "))
            luku2 = float(input("Anna toinen luku: "))
        except ValueError:
            print("Virhe: Syötä vain numeroita!")
            continue

        if valinta == "1":
            print(f"Tulos: {luku1} + {luku2} = {summaa(luku1, luku2)}")

        elif valinta == "2":
            print(f"Tulos: {luku1} - {luku2} = {erotus(luku1, luku2)}")

        elif valinta == "3":
            print(f"Tulos: {luku1} * {luku2} = {tulo(luku1, luku2)}")

        elif valinta == "4":
            tulos = osamaara(luku1, luku2)
            if isinstance(tulos, str): # Jos funktio palautti virhetekstin
                print(tulos)
            else:
                print(f"Tulos: {luku1} / {luku2} = {tulos}")
    else:
        print("Virheellinen valinta, yritä uudelleen.")