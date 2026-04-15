lentoasemat = {}

while True:
    print("\nLentoasematiedot:")
    print("1 - Syötä uusi lentoasema")
    print("2 - Hae lentoaseman tiedot")
    print("0 - Lopeta")

    valinta = input("Valitse toiminto (0, 1 tai 2): ")

    if valinta == "1":
        icao = input("Syötä lentoaseman ICAO-koodi: ").upper()
        nimi = input("Syötä lentoaseman nimi: ")

        lentoasemat[icao] = nimi
        print(f"Lentoasema {nimi} ({icao}) tallennettu.")

    elif valinta == "2":
        icao = input("Syötä haettavan lentoaseman ICAO-koodi: ").upper()

        if icao in lentoasemat:
            print(f"ICAO-koodia {icao} vastaava lentoasema on {lentoasemat[icao]}.")
        else:
            print("Lentoasemaa ei löydy järjestelmästä.")

    elif valinta == "0":
        print("Ohjelma päättyy. Kiitos!")
        break

    else:
        print("Virheellinen valinta. Yritä uudelleen.")