tarina = []

while True:
    sana = input("Kirjoita sana ja teen siitä tarinan. Lopeta syöttämällä (loppu)")

    # Tarkistetaan, haluaako käyttäjä lopettaa
    if sana.lower() == "loppu":
        break

    tarina.append(sana)

valmis_tarina = " ".join(tarina)

print("\n--- Tässä valmis tarina ---")
print(valmis_tarina)