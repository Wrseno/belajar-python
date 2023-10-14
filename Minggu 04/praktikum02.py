# menambah list kosong untuk menampung hobi
hobi = []
stop = False
i = 0

# mengisi hobi
while(not stop):
    hobi_baru = input("Inputkan hobi yang ke-{}: " +  format(i) + " ")
    hobi.append(hobi_baru)

# increment i
    i += 1
    tanya = input("Mau isi lagi ? (y/t) :")
    if (tanya == "t"):
        stop = True

# cetak semua hobi
print("=" * 15)
print("Kamu memiliki " + format(len(hobi)) + " hobi, yaitu :")
for hb in hobi:
    print("*" + format(hb))