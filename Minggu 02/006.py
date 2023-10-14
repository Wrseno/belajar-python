inputJarak = float(input("Masukkan jarak tempuh : "))
inputJam = float(input("Masukkan waktu tempuh dalam jam : "))
inputMenit = float(input("Masukkan waktu tempuh dalam menit : "))
inputDetik = float(input("Masukkan waktu tempuh dalam detik : "))

waktu = inputJarak*1000
detik = (60*60*inputJam) + (60*inputMenit) + inputDetik
kecepatan = round(waktu/detik, 3)

print(f"Kecepatan mobil adalah {kecepatan}m/s")