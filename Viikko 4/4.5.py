oikea_tunnus = "python"
oikea_salasana = "rules"

print("Anna käyttäjätunnus ja salasana")

yritykset = 0
maksimi_yritykset = 5
kirjautunut = False

while yritykset < maksimi_yritykset:
    tunnus = input("Käyttäjätunnus:")
    salasana = input("Salasana: ")

    if tunnus == oikea_tunnus and salasana == oikea_salasana:
        kirjautunut = True
        break

    else:
        yritykset += 1
        print(f"Väärä tunnus tai salasana. Yrityksiä jäljellä {maksimi_yritykset}")

if kirjautunut:
    print("Tervetuloa, käyttäjä!")
else:
    print("Tili lukittu")

