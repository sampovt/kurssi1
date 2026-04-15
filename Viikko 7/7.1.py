vuodenajat = ("talvi", "kevät", "kesä", "syksy")

syote = input("Anna kuukauden numero (1-12): ")

if syote.isdigit():
    kuukausi = int(syote)

    if 1 <= kuukausi <= 12:

        indeksi = (kuukausi % 12) // 3

        vuodenaika = vuodenajat[indeksi]

        print(f"Lukua {kuukausi} vastaa vuodenaika {vuodenaika}.")
    else:
        print("Virheellinen numero! Kuukauden numeron pitää olla väliltä 1-12.")
else:

    print("Virheellinen syöte! Ole hyvä ja anna pelkkä kokonaisluku.")