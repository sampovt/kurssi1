import math

leiviska = float(input("Syötä leiviskä: "))
naula = float(input("Syötä naulat: "))
luoti = float(input("Syötä luodit: "))


leiviska_grammoina = leiviska * 20 * 32 * 13.3
naula_grammoina = naula * 32 * 13.3
luoti_grammoina = luoti * 13.3

kokonais_grammat = leiviska_grammoina + naula_grammoina + luoti_grammoina
kilot = kokonais_grammat//1000
grammat = kokonais_grammat%1000
print(f"kilot: {kilot: .2f} grammat: {grammat:.2f}")