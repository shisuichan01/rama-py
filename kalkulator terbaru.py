print("=== Kalkulator Sederhana ===")

print("Select operation.")
print("1.Pertambahan")
print("2.Pengurangan")
print("3.Perkalian")
print("4.Pembagian")
choice = input("Enter choice(1/2/3/4):")
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

if choice == "1":
    hasil = angka1 + angka2
elif choice == "2":
    hasil = angka1 - angka2
elif choice == "3":
    hasil = angka1 * angka2
elif choice == "4":
    if angka2 != 0:
        hasil = angka1 / angka2
    else:
        hasil = "Error! Tidak bisa bagi nol."
else:
    hasil = "Operator tidak dikenal."

# Jika hasil adalah angka dan bilangan bulat, tampilkan tanpa .0
if isinstance(hasil, float) and hasil.is_integer():
    print(f"Hasil: {int(hasil)}")
else:
    print(f"Hasil: {hasil}")
