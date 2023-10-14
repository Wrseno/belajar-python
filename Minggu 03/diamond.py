inputBintang = int(input("Masukkan Jumlah Bintang : "))

for i in (range(1, inputBintang + 1)):
        print(" " * (inputBintang - i) + "*" * (2*i-1))
for i in (range(inputBintang - 1, 0, -1)):
        print(" " * (inputBintang - i) + "*" * (2*i-1))
