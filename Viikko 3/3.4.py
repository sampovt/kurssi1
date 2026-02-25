vuosiluku = int(input("Anna vuosiluku"))

if (vuosiluku % 4==0 and vuosiluku % 100 != 0) or (vuosiluku % 400 == 0):
    print("Annettu vuosi on karkausvuosi")
else:
    print("Annettu vuosi ei ole karkausvuosi")





#Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa,
# onko annettu vuosi karkausvuosi. Vuosi on karkausvuosi, jos se on jaollinen neljällä.
# Sadalla jaolliset vuodet ovat karkausvuosia vain
# jos ne ovat jaollisia myös neljälläsadalla.