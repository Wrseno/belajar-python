nim = []
nama = []
asalDaerah = []

pilihan = 1
while pilihan != 0:
    print("1. Masukkan data")
    print("2. Tampilkan data")
    print("3. Hapus data")
    print("0. Keluar")

    pilihan = int(input("Masukkan Pilihan Anda : "))
    print("")
    print("")
    print("")

    if pilihan == 1:
        inputNim = input("Masukkan NIM Anda : ")
        nim.append({'NIM': inputNim})
        inputNama = input("Masukkan Nama Anda : ")
        nama.append({'Nama': inputNama})
        inputAsalDaerah = input("Masukkan Asal Daerah Anda : ")
        asalDaerah.append({"Asal Daerah": inputAsalDaerah})
    elif pilihan == 2:
        penentu = True
        for i in range(len(nim)):
            if penentu:
                print("NIM\t\tNama\t\tAsal Daerah")
            print(nim[i]['NIM'],'\t',nama[i]['Nama'],'\t',asalDaerah[i]['Asal Daerah'])
            penentu = False
    elif pilihan == 3:
        inputNim = input("Masukkan NIM Anda : ")
        for i in range(len(nim)):
            if inputNim == nim[i]["NIM"]:
                print(i)
                del nim[i]
                del nama[i]
                del asalDaerah[i]
                break
        print("")
        print("")
        print("")
