lista = []

while True:
    syote = input("Syötä sanoja ja lisään ne listaan. Kun olet valmis syötä 0: ")
    lista.append(syote)

    pitkat_sanat = []

    for sana in lista:
        if len(sana) > 5:
            pitkat_sanat.append(sana)

    print('x', "Lista tähän mennessä:", lista, "Näin monessa sanassa on enemmän kuin 5 kirjainta:",len(pitkat_sanat))

    if syote == "0":
     break