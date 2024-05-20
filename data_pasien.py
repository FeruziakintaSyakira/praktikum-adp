print("Nama  : Feruziakinta Syakira")
print("NIM   : 2310431008")
print("Shift : 1")
print("Tugas : Modul 8")
print(' ')

def tambah():
	with open("data.txt","a") as file:
		file.write(f"{n},{u},{jk},{gd},{rp},{do}\n")
	print("Data telah ditambah")

def tampil():
	with open("data.txt","r") as file:
		for line in file :
			print(line)
			
def hapus():
	with open("data.txt","w") as file:
		file.write(' ')
	print("Data telah dihapus")

print("|===================|")
print("|    Pilihan Menu   |")
print("|-------------------|")
print("|1. Menambahkan data| ")
print("|2. Menampilkan data|")
print("|3. Menghapus data  |")
print("|4. Keluar          |")
print("|===================|")

while True :
	pilih = input("Masukkan pilihan : ")
	if pilih == "1":
		n = input("Nama : ")
		u = input("Umur : ")
		jk = input("Jenis kelamin : ")
		gd = input("Golongan darah : ")
		rp = input("Riwayat penyakit : ")
		do = input("Daftar obat : ")
		tambah()
	elif pilih== "2":
		tampil()
	elif pilih == "3":
		hapus()
	elif pilih == "4" :
		break
