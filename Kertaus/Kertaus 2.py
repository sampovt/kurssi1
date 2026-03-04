tuntipalkka = float(input("Anna tuntipalkkasi: "))
tunnit = float(input("Kuinka monta tuntia teit töitä? "))
viikonpäivä = input("Mikä viikonpäivä tänään on? ").lower()

# Tarkistetaan, onko kyseessä sunnuntai
if viikonpäivä == "sunnuntai":
    # Sunnuntaina palkka on kaksinkertainen
    paivapalkka = (tuntipalkka * 2) * tunnit
    print(f"Oho! Tienasit {paivapalkka:.2f}€.")
else:
    # Arkena ja lauantaina normaali palkka
    paivapalkka = tuntipalkka * tunnit
    print(f"Wow, tienasit {paivapalkka:.2f}€.")