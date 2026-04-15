#pieni = None
#suuri = None

#while True:
    #annettu = input("Syötä luku tai lopeta ketju tyhjällä")

    #if annettu == "":
     #   break

    #luku= float(annettu)

    #if pieni is None or luku < pieni:
   #     pieni = luku
  #  if suuri is None or luku > suuri:
 #       suuri = luku

#if pieni is not None:
  #  print(f"Pienin luku: {pieni}")
 #   print(f"Suuri luku: {suuri}")

#else:
#     print("Syötä luku aloittaaksesi")
#alkuperäinen

luku = input("Anna luku, tyhjä lopettaa:")

pieni = luku
suuri = luku

while luku != "":
    numero = int(luku)

    if pieni == luku or numero < pieni:
        pieni = numero

    if suuri == luku or numero > suuri:

    luku = input("Anna luku, tyhjä lopettaa:")

    print("Pienin luku oli:", pieni)
    print("Suuri luku oli:", suuri)