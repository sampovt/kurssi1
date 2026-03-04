nimi = input("Mikä on nimesi? ")

if nimi != "Matti":

    annokset = int(input("Kuinka monta keittoannosta haluat ostaa? "))


    yksikköhinta = 5.90
    kokonaishinta = annokset * yksikköhinta

    # Tulostetaan hinta (kahden desimaalin tarkkuudella)
    print(f"Kiitos tilauksesta! Kokonaishinta on {kokonaishinta:.2f} euroa.")
else:
    print(f"Hei {nimi}, kiitos käynnistä!")


