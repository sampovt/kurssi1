lista = []

while True:
    syote = input("Syötä luku, niin lisään sen listaan. Lopeta syöttämällä 0: ")
    lista.append(syote)

    print('x', "Lista tähän mennessä:", lista, "Järjestettynä:",sorted(lista))
    if syote == "0":
        break
print("Ohjelma lopetettu")