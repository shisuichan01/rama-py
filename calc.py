Jooinfoo.com: Jurnal | Berita | Informasi
×
type to search

 
Home › Programing › Python
√ Kumpulan Script Python Simple Keren Buat Belajar
Thursday, June 6, 2019 
Ok pada kesempatan ini saya akan share dan membahas tutorial mengenai bahasa pemrograman yang akhir-akhir ini sangat trending, yaitu Python, bahasa pemrograman python untuk saat ini sudah memasuki versi 3. Kelebihan dari bahasa pemrograman yang satu ini adalah penulisan kode yang lebih indah tanpa menggunakan semicolom, 

Baca Juga :
Cara Mengetahui Bahasa Pemrogaraman Dan Teknologi Yang Digunakan Perusahaan IT
Tutorial Membuat CRUD dengan Express dan MongoDB
Tutorial Membuat Pemutar Musik Menggunakan HTML5 dan Javascript




Bahasa pemrograman ini juga banyak di pakai oleh perusahaan top dunia, seperti produk google. Dan karena python bisa digunakan untuk banyak hal. Seperti untuk website kita mengenal framwork Djanggo, Untuk data science kita mengenal NumPy, untuk data visualization dan masih banyak lagi. Sehingga bahasa pemrograman yang satu ini sangat di minati oleh banyak perusahaan dan para developer. Bapak pytho sendiri atau pencipta python yaitu Guido van Rossum.

Related
√ Daftar 9 Text Editor Terbaik Untuk Para Programer Dan Developer
Download Source Code Aplikasi Berita Menggunakan React Native
√ Download Source Kode Aplikasi Pembelajaran Huruf Java Netbeans

Kumpulan Script Python Simple Keren Buat Belajar Keren

1. Script Python menghitung tanggal dan waktu :
 from datetime import datetime
now = datetime.now()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)
print (mm + "/" + dd + "/" + yyyy + " " + hour + ":" + mi + ":" + ss)

2. Script Python menghitung 2 angka yang di inputkan :
 number1 = input("Angka Pertama: ")
number2 = input("\nANgka Kedua: ")

sum = float(number1) + float(number2)

print("Penjumlahan dari {0} dan {1} adalah {2}" .format(number1, number2, sum)) 


3. Script Python untuk menampilkan nama :
 # Python program showing
# a use of raw_input()
g = raw_input("Enter your name : ")
print g 


4. Script Python untuk kalkulator :
 # Program make a simple calculator that can add, subtract, multiply and divide using functions
# This function adds two numbers
def add(x, y):
   return x + y
# This function subtracts two numbers
def subtract(x, y):
   return x - y
# This function multiplies two numbers
def multiply(x, y):
   return x * y
# This function divides two numbers
def divide(x, y):
   return x / y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
# Take input from the user
choice = input("Enter choice(1/2/3/4):")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))
elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))
elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")
