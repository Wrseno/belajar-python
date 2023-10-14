i = a = b = c = 0
nama = []
npm = []
kelas = []
jurusan = []
angkatan = []

while True:
    print("Masukkan data ke -", i+1)
    nama.append(input('Nama Anda : '))
    npm.append(input('NPM Anda : '))
    if len(npm[i]) != 8:
        print("NPM Salah")
        print()
        nama.pop(i)
        npm.pop(i)
        continue
    kelas.append(input("Kelas Anda : "))
    if len(kelas[i]) != 5:
        print("Kelas Salah")
        print()
        nama.pop(i)
        npm.pop(i)
        kelas.pop(i)
        continue
    jurusan.append(kelas[i][1:3])
    angkatan.append(npm[i][3:5])
    if (jurusan[i] == 'IA'):
        jurusan[i] = 'Teknik Informatika'
        a += 1
    elif (jurusan[i] == 'IB'):
        jurusan[i] = 'Teknik Industri'
        b += 1
    elif (jurusan[i] == 'IC'):
        jurusan[i] = 'Teknik Mesin'
        c += 1
    else:
        print("Kelas Salah")
        print
        continue
    lagi = ""
    while lagi != 'y' and lagi != 't':
        lagi = input('INPUT LAGI (Y/T) ?')
    i += 1
    if lagi == 't':
        break
    print('Daftar Mahasiswa')
    print('=====================================')
    print('No. Nama NPM Kelas Angkatan Jurusan')
    print("=====================================")
    for n in range(i):
        print(n + 1, ' ', nama[n],' ', npm[n],' ', kelas[n],' ', angkatan[n],' ', jurusan[n])
    print("TOTAL JURUSAN TEKNIK INFORMATIKA = ", a ,"orang\n")
    print("TOTAL JURUSAN TEKNIK INDUSTRI = ", b ,"orang\n")
    print("TOTAL JURUSAN TEKNIK MESIN = ", c ,"orang\n")
    lihatHasil = ''
    while lihatHasil != 'y' and lihatHasil != 't':
        lihatHasil = input('Ingin melihat hasil [Y/T] ?')
    if lihatHasil == 'y':
        cari = input('Cari Berdasarkan NPM : ')
        for n in range(i):
            if cari == npm[n]:
                print
                print('Nama : ', nama[n])
                print('Kelas : ', kelas[n])
                print('Angkatan : ', angkatan[n])
                print('Jurusan : ', jurusan[n])
                break
        else: 
            print('NPM TIDAK ADA')
            break