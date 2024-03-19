print('Nama :Feruziakinta Syakira')
print('Nim  :2310431008')
print('Tugas:Modul II')
print(' ')

print('Pembelian tiket pesawat Eagle')
print('Lokasi Awal : Padang')
print(' ')
print('SELAMAT DATANG')
print('SILAHKAN ISI')
print('')

nama=(input('Nama          :'))
umur=(input('Umur          :'))
JK=(input('Jenis kelamin :'))
print(' ')

print('|========================|')
print('|  Tujuan keberangkatan  |')
print('|1. Jakarta              |')
print('|2. Yogyakarta           |')
print('|3. Bandung              |')
print('|========================|')
print(' ')

pilih_tujuan=int(input('Pilih tujuan : '))
if(pilih_tujuan==1):
	print('Jakarta')
	Tujuan='Jakarta'
if(pilih_tujuan==2):
	print('Yogyakarta')
	Tujuan='Yogyakarta'
if(pilih_tujuan==3):
	print('Bandung')
	Tujuan='Bandung'
print(' ')

print('|=====================|')
print('|Jenis Maskapai       |')
print('|1. Ekonomi           |')
print('|2. Bussines          |')
print('|3. First Class       |')
print('|=====================|')
print(' ')

pilih_maskapai=int(input('Pilih Maskapai : '))
if(pilih_maskapai==1):
	print('Ekonomi')
	Maskapai='Ekonomi'  
if(pilih_maskapai==2):
	print('Business')
	Maskapai='Business'
if(pilih_maskapai==3):
	print('First Class')
	Maskapai='First Class'
print(' ')

if(pilih_tujuan==1) & (pilih_maskapai==1):
	Harga=1500000
if(pilih_tujuan==1) & (pilih_maskapai==2):
	Harga=2500000
if(pilih_tujuan==1) & (pilih_maskapai==3):
	Harga=3500000
if(pilih_tujuan==2) & (pilih_maskapai==1):
	Harga=1200000
if(pilih_tujuan==2) & (pilih_maskapai==2):
	Harga=2200000
if(pilih_tujuan==2) & (pilih_maskapai==3):
	Harga=3200000
if(pilih_tujuan==3) & (pilih_maskapai==1):
	Harga=1000000
if(pilih_tujuan==3) & (pilih_maskapai==2):
	Harga=2000000
if(pilih_tujuan==3) & (pilih_maskapai==3):
	Harga=3000000	

kursi=int(input('Jumlah kursi:'))
print(' ')
if (kursi>3):
	total_harga=int((Harga*kursi)-((Harga*kursi)*0.25))
	print('Diskon 25%')
if(kursi<=3):
	total_harga=(int(Harga*kursi))
print(' ')
print('Total Harga:',total_harga)
print(' ')

print('=====================================')
print('           Struk Pembelian            ')
print('Lokasi Awal   : Padang')
print('Nama          :',nama)		
print('Umur          :',umur)
print('Jenis Kelamin :',JK)
print('-------------------------------------')
print('Tujuan        :',Tujuan)
print('Maskapai      :',Maskapai)
print('Jumlah Kursi  :',kursi)
print('Total Harga   :',total_harga)
print('            TERIMA KASIH       ')
print('=====================================')
