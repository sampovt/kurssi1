luvut = []

while True:
    syote = input("Syötä luku (tyhjä rivi lopettaa)")

    if syote == "":
        break

    luku = float(syote)
    luvut.append(luku)

luvut.sort(reverse=True)

print("\nViisi suurinta lukua ovat:")

for luku in luvut[:5]:
    print(luku)
