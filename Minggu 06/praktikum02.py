import numpy as np

inputBaris = int(input("Masukkan jumlah baris : "))
inputKolom = int(input("Masukkan jumlah kolom : "))

print("Masukkan entri dalam satu baris dengan dipisahkan spasi : ")

entri = list(map(int, input().split()))

matrix = np.array(entri).reshape(inputBaris, inputKolom)
print(matrix)