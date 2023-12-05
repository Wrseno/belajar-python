# angka = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# pangkat = [n+1 for n in angka]
# print(pangkat)

# var_array = [1, 5, 8, 5, 100]
# left_pointer = var_array[0]

# for i in range(1, len(var_array)):
#     right_pointer = var_array[i]
#     print(f"Cek apakah {right_pointer} > {left_pointer}")
#     if right_pointer > left_pointer:
#         print(f"{right_pointer} > {left_pointer} maka left_pointer berganti nilai")
#         left_pointer = right_pointer
#         print(f"Nilai berubah menjadi {left_pointer}")
#     else:
#         print(f"{right_pointer} < {left_pointer} maka dilewati")

# print(f"Nilai terbesar adalah {left_pointer}")

# var_elemen = [i for i in range(101)]

# jumlah_seluruh_elemen = 0
# banyak_elemen = 0

# for elemen in var_elemen:
#     banyak_elemen = elemen
#     jumlah_seluruh_elemen += elemen

# if elemen > 0:
#     result = jumlah_seluruh_elemen/banyak_elemen
#     print("Rata-rata dari elemen adalah {}".format(result))
# else:
#     print("Rata-rata tidak ditemukan, elemen tidak ada dalam list")


# hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]

# # Header tabel
# # print("  ".join(hari))  # Menampilkan nama hari di atas tabel
# for i in hari:
#     print(i, end="|")

# # Loop untuk setiap tanggal
# for t in range(1, 31):  # Anggaplah bulan memiliki 30 hari
#     if t % 7 == 1:
#         print()  # Pindah baris setelah satu minggu (7 hari)
#     print("{:5}".format(t), end="|")  # Menampilkan tanggal dengan lebar 2 karakter

var_mat = [[5, 0], [1, -2]]
def_mat = [[0 for j in range(2)] for i in range(2)]

for i in range(len(var_mat)):
    for j in range(len(var_mat[0])):
        def_mat[i][j] = var_mat[i][j] * 2

print(def_mat)
