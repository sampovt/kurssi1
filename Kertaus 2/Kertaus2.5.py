def suurin_arvo(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

luku1 = float(input("Anna ensimmäinen luku: "))
luku2 = float(input("Anna toinen luku: "))
luku3 = float(input("Anna kolmas luku: "))

tulos = suurin_arvo(luku1, luku2, luku3)


print("Suurin luku on:", tulos)