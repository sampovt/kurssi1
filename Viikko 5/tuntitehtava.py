lista = ["sininen", "keltainen", "punainen"]

color = input("Anna lempiväri:").capitalize()
if color in lista:
    print("Väri löytyy listalta")

else:
    print("Väriä ei löydy listalta")