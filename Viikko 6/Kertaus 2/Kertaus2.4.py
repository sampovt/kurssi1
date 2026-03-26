def kuusi(koko):
    print("Tämä on kuusi!")


    for i in range(1, koko + 1):
        valilyonnit = " " * (koko - i)
        tahdet = "*" * (2 * i - 1)
        print(valilyonnit + tahdet)

    jalka_valilyonnit = " " * (koko - 1)
    print(jalka_valilyonnit + "*")


kuusi(6)