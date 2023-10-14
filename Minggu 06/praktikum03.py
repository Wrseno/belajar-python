inputNomor = int(input("Masukkan nomor : "))

for i in range(inputNomor):
    for j in range(inputNomor):
        if i == j:
            print(f"1 {i,j}", end=" ")
        else:
            print(f"0 {i,j}", end=" ")
    print()
