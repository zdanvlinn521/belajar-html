# contoh: tabel perkalian 1_3
for i in range(1, 4):          # loop luar: baris
    for j in range(1, 4):      # loop dalam: kolom
        print(i, "X", j, "=", i * j)
    print()  # baris kosong antar tabel