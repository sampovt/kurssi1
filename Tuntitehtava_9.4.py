hedelma = {
    'Omena': '1',
    'Persikka': '2',
    'Mango': '3', }

while True:
    hinta = input("Syötä hedelmä ja annan hinnan Euroissa (Omena, Persikka, Mango): ")

    if hinta == "":
        print("Tuo ei ollut listalla.")
        break

    if hinta in hedelma:
    print(hedelma[hinta])

    else:
    print("Tuo ei ollut listalla. Käynnistä ohjelma uudelleen")