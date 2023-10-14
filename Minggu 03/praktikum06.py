# REKURSIF

def rekursif(angka):
    if angka > 0:
        print(angka)
        angka -= 1
        rekursif(angka)
    else:
        print(angka)
inputAngka = int(input("Masukkan angka : "))
rekursif(inputAngka)