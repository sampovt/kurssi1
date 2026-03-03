import random
oikea = random.randint(1, 10)

print("Tervetuloa pelaamaan! Mielessäni on luku 1-10, yritä arvata mikä se on! ;)")

while True:
    arvaus = int(input("Anna arvauksesi:"))

    if arvaus < oikea:
        print("Ei noin pieni!")
    elif arvaus > oikea:
        print("Hui, ei noin iso!")
    else:
        print("Oikein meni!")
        break

print("Kiitos pelistä!")