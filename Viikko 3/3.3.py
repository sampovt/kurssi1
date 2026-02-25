Sukupuoli = (input)("Syötä sukupuoli:")
Hemoglobiini = int(input("Syötä hemoglobiini:"))


if Sukupuoli == "Mies":
    if Hemoglobiini < 134:
        print("Hemoglobiini on matala")
    elif 134 <= Hemoglobiini <= 195:
        print("Hemoglobiini on normaalilla tasolla")
    else:
        print("Hemoglobiini on korkea")

if Sukupuoli == "Nainen":
    if Hemoglobiini < 117:
        print("Hemoglobiini on matala")
    elif 117 <= Hemoglobiini <= 176:
        print("Hemoglobiini on normaalilla tasolla")
    else:
        print("Hemoglobiini on korkea")

#Kirjoita ohjelma
# Käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
# Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.
#Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
#Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.