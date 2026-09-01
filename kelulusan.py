# program penentu kelulusan smk tjp tuban
print ("=" * 40)
print (" sistem penilaian siswa")
print ("=" * 40)
naman        = input("nama siswa         : ")  
nilai_uts    = float(input("NILAI UTS   (0-100) : "))
nilai_uas    = float(input("NILAI UAS   (0-100) : "))
nilai_tugas  = float(input("NILAI TUGAS         : "))

# hitung rata rata
rata = (nilai_uts * 0.3) + (nilai_uas * 0.5) + (nilai_tugas * 0.2)

#tentukan kategori
if rata >= 90:
    predikat = "A - sangat baik"
elif rata >= 80:
    predikat = "B - baik"
elif rata >= 70:
    predikat = "C - cukup"
elif rata >= 60:
    predikat = "D - kurang"
else:
    predikat = "E - sangat kurang"
    
lulus =rata >= 70

print ()
print ("=" * 40)
print ("    Hasil Penilaian")
print ("=" * 40)
print ("Nama          :",  naman)
print ("Rata-rata     :",  round(rata, 2))
print ("Predikat      :",  predikat)
print ("status  n     :",  "Lulus" if lulus else "Tidak Lulus")