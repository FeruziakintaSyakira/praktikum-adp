print("Nama  : Feruziakinta Syakira")
print("NIM   : 2310431008")
print("Shift : 1")
print("Tugas : Modul VI")
print()
#soal a
print('Jadwal keberangkatan : ')
jadwal_keberangkatan= [
    ["1", "Jambi", "Jakarta", "08:00", "09:20"],
    ["2", "Padang", "Bali", "11:00", "15.40"],
    ["3", "Jakarta", "Lombok", "13:00", "15:00"],
    ["4", "Padang", "Jakarta", "09:00", "10:30"],
]
print("|=============================================================================|")
print("| No.Rute | Kota Asal  | Kota Tujuan | Waktu Keberangkatan | Waktu Kedatangan |")
print("|=============================================================================|")

for i in jadwal_keberangkatan:
    print("| {:7} | {:10} | {:11} | {:19} | {:16} |".format(*i))

print("|=============================================================================|")

#soal b
print()
print("Menentukan Rute Tercepat")
print()
rute_a = int(input("Masukkan Nomor Rute a : "))
rute_b = int(input("Masukkan Nomor Rute b : "))
rute_1 = "Jambi-Jakarta"
rute_2 = "Padang-Bali"
rute_3 = "Jakarta-Lombok"
rute_4 = "Padang-Jakarta"
if rute_a == 1 and rute_b == 2 :
    print("Rute tercepat antara", rute_1,"dan",rute_2 ,"adalah", rute_1)
if rute_a == 1 and rute_b == 3 : 
    print("Rute tercepat antara", rute_1,"dan",rute_3 ,"adalah", rute_1)
if rute_a == 1 and rute_b == 4 : 
    print("Rute tercepat antara", rute_1,"dan",rute_4 ,"adalah", rute_1)
if rute_a == 2 and rute_b == 3 : 
    print("Rute tercepat antara", rute_2,"dan",rute_3 ,"adalah", rute_3)
if rute_a == 2 and rute_b == 4 : 
    print("Rute tercepat antara", rute_2,"dan",rute_4 ,"adalah", rute_4)
if rute_a == 3 and rute_b == 4 : 
    print("Rute tercepat antara", rute_3,"dan",rute_4 ,"adalah", rute_3)
