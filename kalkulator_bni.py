berat = int(input("Masukkan berat badan anda (kg): "))
tinggi = int(input("Masukkan tinggi badan anda (cm): "))

BMI = berat / ((tinggi / 100) ** 2)

if (BMI < 18.5) :
    kategori = "Kurus (Underweight)"
    keterangan = "perlu tambah berat badan"
elif (BMI < 24.9) :
    kategori = "Normal (Ideal)"
    keterangan = "pertahankan gaya hidup sehat"
elif (BMI < 29.9) :
    kategori = "Gemuk (Overweight)"
    keterangan = "perlu olahraga lebih"
else :
    kategori = "Obesitas (Obesity)"
    keterangan = "konsultasi dokter"
    
print("nilai bmi : ", BMI)
print("kategori : ", kategori)
print("keterangan : ", keterangan)