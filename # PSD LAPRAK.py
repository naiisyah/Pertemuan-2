# PSD LAPRAK
# fungsi sederhana
def selamat_pagi():
    print("Selamat pagi")

selamat_pagi()

# fungsi dengan parameter
def sapa(nama):
    print(f"Hai, {nama}!")

sapa("Andi")
sapa("Budi")

# #fungsi dengan parameter nilai kembalian
# #nilai kembalian yaitu nilai yang pakai return
import math

def luas_lingkaran():
    r = float(input())
    luas = math.pi * r **2
    return luas
LL = luas_lingkaran()
print(f"luas lingkaran{LL}")

def sum(a, b):
    return a + b

hsum = sum(10, 20)
print(f"hasil jumlahan adalah {hsum}")


#fungsi dengan parameter dan dengan nilai kembali
def jumlahkan(a, b):
    return a + b
hasil_jumlah = jumlahkan(10, 20)
print(f"Hasil Penjumlahan:{hasil_jumlah}")

# #fungsi dengan parameter nilai default
def sapa(nama="Jhon Doe"):
    print(f"Hai, {nama}!")

sapa("Andi")
sapa()#tanpa parameter makan output akan menggunakan nama default

# #fungsi dengan paraeter dan argumen keyword
def info(nama, usia):
    print(f"Nama: {nama}, usia; {usia}")

info(nama="BUDI", usia=18)

# #memanggil fungsi dengan argument keyword
info(nama="Budi", usia=25)
info(usia=30, nama="Sinta")

# CONTOH SOAL
def data_mahasiswa():
    jumlah_mahasiswa = int(input("Masukkan jumlah Mahasiswa: "))#untuk menginput banyaknya mahasiswa
    data_mahasiswa = []#list kosong untuk menyimpan inputan

    for i in range(jumlah_mahasiswa):#perulangan agar outputan sama dengan jumlah mahasiswanya
        nim = input("Masukkan NIM mahasiswa ke-%d : " % (i+1))#%d digunakan agar ada penomorannya 
        nama = input("Masukkan nama mahasisiwa ke-%d : " % (i + 1))
        asal = input("Masukkan daerah asal mahasisiwa ke-%d : " % (i + 1))
#memasukkan inputan ke list kosong yang telah kita buat
        data_mahasiswa.append([nim, nama, asal])
    
    print("Data Mahasiswa :")
    for i in range(jumlah_mahasiswa):
        print("-"*20)
        print("nim :" + data_mahasiswa [i][0])
        print("nama :" + data_mahasiswa [i][1])
        print("asal :" + data_mahasiswa [i][2])
data_mahasiswa()

#PSD SOAL LATIHAN
def data_mahasiswa():
    jumlah_mahasiswa = int(input("Masukkan jumlah Mahasiswa: "))#untuk menginput banyaknya mahasiswa
    data_mahasiswa = []#list kosong untuk menyimpan inputan

    for i in range(jumlah_mahasiswa):#perulangan agar outputan sama dengan jumlah mahasiswanya
        nama = input("Masukkan nama mahasisiwa ke-%d : " % (i + 1))
        nim = input("Masukkan NIM mahasiswa ke-%d : " % (i+1))#%d digunakan agar ada penomorannya 
        jumlah_nilai = int(input("Masukkan jumlah nilai ujian mahasiswa ke-%d : " % (i + 1)))
        nilai_ujian = []

        for j in range(jumlah_nilai):
            nilai = float(input("Masukkan nilai ujian ke-%d : " % (i + 1)))
            nilai_ujian.append(nilai)                    
#memasukkan inputan ke list kosong yang telah kita buat
        data_mahasiswa.append([nim, nama, nilai_ujian])
       
    print("Data Mahasiswa :")
    for i in range(jumlah_mahasiswa):
        print("nama :" + data_mahasiswa [i][0])
        print("nim :" + data_mahasiswa [i][1])
        print("Rata-rata Nilai Ujian :" + sum(nilai_ujian)/len(nilai_ujian) [i][2])

data_mahasiswa()