ostoslista = ["Nugetti", "Maito", "Porkkana"]


while ostoslista:
    ostos = input("Mitä ostit?").lower()

    if ostos in ostoslista:
        ostoslista.remove(ostos)
         print("Löytyy listalta. Jäljellä",ostoslista)
    else:
        print("Tuotetta ei löydy listalta. Vie takaisin hyllyyn.")

Print("Sitten kotiin!")
