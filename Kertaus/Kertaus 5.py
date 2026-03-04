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
        luku1 = float(input("Anna ensimmäinen luku: "))
        luku2 = float(input("Anna toinen luku: "))

        if valinta == "1":
            tulos = luku1 + luku2
            print(f"Tulos: {luku1} + {luku2} = {tulos}")

        elif valinta == "2":
            tulos = luku1 - luku2
            print(f"Tulos: {luku1} - {luku2} = {tulos}")

        elif valinta == "3":
            tulos = luku1 * luku2
            print(f"Tulos: {luku1} * {luku2} = {tulos}")

        elif valinta == "4":

            if luku2 != 0:
                tulos = luku1 / luku2
                print(f"Tulos: {luku1} / {luku2} = {tulos}")
            else:
                print("Virhe: Nollalla ei voi jakaa!")
    else:
        print("Virheellinen valinta, yritä uudelleen.")

        #Tämä tehtävä oli järkyttävä..