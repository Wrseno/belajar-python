inputBaris = int(input("Masukkan jumlah baris : "))
inputKolom = int(input("Masukkan jumlah kolom : "))

matrix = []
print("Masukkan entri secara berurutan : ")

for i in range(inputBaris):
    array = []
    for j in range(inputKolom):
        array.append(int(input()))
    matrix.append(array)

for x in range(inputBaris):
    for y in range(inputKolom):
        print(matrix[x][y], end=" ")
    print()