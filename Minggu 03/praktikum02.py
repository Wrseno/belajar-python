inputBintang = int(input("Masukkan Jumlah Bintang : "))

for i in (range(inputBintang)):
    for j in range(i+1):
        print("*", end="-")
    print()
for i in reversed(range(inputBintang)):
    for j in range(i+1):
        print("*", end="-")
    print()