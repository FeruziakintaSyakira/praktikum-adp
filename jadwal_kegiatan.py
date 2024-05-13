print('Nama :Feruziakinta Syakira')
print('Nim  :2310431008')
print('Tugas:Modul VII')
print(' ')

print('|================|')
print('|  Pilihan menu  |')
print('|----------------|')
print('|1. Tambah jadwal|')
print('|2. Hapus jadwal |')
print('|3. Tampil jadwal|')
print('|4. Keluar       |')
print('|================|')
print(' ')
		
def tambah_kegiatan():
	waktu_mulai=str(input('Masukkan waktu mulai : '))
	waktu_selesai=str(input('Masukkan waktu selesai : '))
	keterangan=str(input('Masukkan keterangan : '))
	jadwal_kegiatan.append([waktu_mulai,waktu_selesai,keterangan])
	return jadwal_kegiatan

print(' ')
	
def hapus_kegiatan():
   if not jadwal_kegiatan:
   	print('Jadwal kegiatan tidak ada')
   else:
   	print('Jadwal kegiatan')
   	print('No.| Waktu mulai | Waktu selesai | Keterangan Kegiatan | ')
   	print('='*56)
   	for i in range(len(jadwal_kegiatan)):
   		tabel= jadwal_kegiatan[i]
   		print(f'{i+1}  | {tabel[0]}       | {tabel[1]}         | {tabel[2]:20}|')
   	hapus = int(input('Masukkan nomor kegiatan yang ingin dihapus: '))-1
   	if hapus < len(jadwal_kegiatan):
   		jadwal = jadwal_kegiatan[:hapus]+ jadwal_kegiatan[hapus+1:]
   		print('Kegiatan telah dihapus')
   		jadwal_kegiatan[:]=jadwal
   	else :
   		print('Nomor kegiatan tidak valid')
   return jadwal_kegiatan
print(' ')

def tampilkan_jadwal():
	if not jadwal_kegiatan:
		print('jadwal kegiatan kosong')
	else :
		print('Jadwal kegiatan')
		print('No.| Waktu mulai | Waktu selesai | Keterangan Kegiatan | ')
		print('='*56)
		for i in range(len(jadwal_kegiatan)):
		 		tabel= jadwal_kegiatan[i]
		 		print(f'{i+1}  | {tabel[0]}       | {tabel[1]}         | {tabel[2]:20}|')
		 		
	return jadwal_kegiatan
	
jadwal_kegiatan= []

while True :
		print(' ')
		pilihan = int(input('Masukkan pilihan menu :'))
		
		if pilihan == 1:
			tambah_kegiatan()
		elif pilihan ==2:
			hapus_kegiatan()
			tampilkan_jadwal()
		elif pilihan ==3:
			tampilkan_jadwal()
		elif pilihan ==4:
			break
		else :
