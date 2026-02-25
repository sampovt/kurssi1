import math

kuha = float(input("Anna kuhan pituus senttimetreinä: "))

if kuha<=37:
    puuttuu = 37-kuha
    print(f"Heitä kuha takaisin järveen. Se on:{puuttuu: .2f}cm liian lyhyt")