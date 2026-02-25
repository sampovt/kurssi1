tuumat = float(input("Anna pituus tuumina: "))

while tuumat >= 0:
    senttimetrit = tuumat * 2.54
    print(f"{tuumat} tuumaa on {senttimetrit} senttimetriä.")
    tuumat = float(input("Anna uusi pituus tuumina:"))

print("Kiitos, jatketaan myöhemmin :)")