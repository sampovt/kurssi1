import random

maara = int(input("Anna kuutioiden määrä"))

summa = 0

for i in range(maara):
    silmaluku = random.randint(1,6)
    summa += silmaluku

print(f"Silmälukujen summa on: {summa}")





