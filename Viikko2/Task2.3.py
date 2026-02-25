import math

Kanta_str = input("Anna suorakulmion kanta: ")
Korkeus_str = input("Anna suorakulmion korkeus: ")

Kanta = float(Kanta_str)
Korkeus = float(Korkeus_str)

Pinta_ala = (Korkeus*Kanta)
Piiri = (Kanta*2+Korkeus*2)

print(f"Pinta_ala: {Pinta_ala:.2f}")
print(f"Piiri: {Piiri: .2f}")
