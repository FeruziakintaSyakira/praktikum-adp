program pembelian_tiket_pesawat;
uses crt;
var
  nama,umur,JK,tujuan,maskapai:string;
  kursi,pilih_tujuan,pilih_maskapai:integer;
  harga,total_harga:real;
begin
  clrscr;
  writeln('Nama :Feruziakinta Syakira   |');
  writeln('NIM  :2310431008             |');
  writeln('Tugas:Modul II               |');
  writeln('___________|');
  writeln(' ');
  
  writeln('Pembelian tiket pesawat Eagle');
  writeln(' ');
  writeln('Lokasi Awal:Padang');
  writeln(' ');
  writeln('SELAMAT DATANG');
  writeln('SILAHKAN ISI');
  write('Nama           :');
  readln(nama);
  write('Umur           :');
  readln(umur);
  write('Jenis kelamin  :');
  readln(JK);
  writeln(' ');
  
  writeln('|====================|');
  writeln('|Tujuan keberangkatan|');
  writeln('|--------------------|');
  writeln('|1. Jakarta          |');
  writeln('|2. Yogyakarta       |');
  writeln('|3. Bandung          |');
  writeln('|====================|');
  writeln(' ');
  write('Pilih tujuan :');
  readln(pilih_tujuan);
  
  
  if (pilih_tujuan=1) then begin tujuan:='Jakarta';
  writeln('Jakarta');
  end; 
 
  if(pilih_tujuan=2) then begin tujuan:='Yogyakarta';
  writeln('Yogyakarta');
  end; 
 
  if(pilih_tujuan=3) then begin tujuan:='Bandung';
  writeln('Bandung');
  end;
  writeln(' ');
  
  writeln('|================|');
  writeln('| Jenis maskapai |');
  writeln('|1. Ekonomi      |');
  writeln('|2. Bussines     |');
  writeln('|3. First class  |');
  writeln('|================|');
  writeln(' ');
  write('Pilih maskapai :');
  readln(pilih_maskapai);
  
  if(pilih_maskapai=1) then begin maskapai:='Ekonomi';
  writeln('Ekonomi');
  end;
  
  if (pilih_maskapai=2) then begin maskapai:='Bussines';
  writeln('Business');
  end;
  
  if (pilih_maskapai=3) then begin maskapai:='First class';
  writeln('First class');
  end;
  writeln(' ');
  
  if (pilih_tujuan=1) and (pilih_maskapai=1) then begin harga:=1500000;
  end;
  
  if (pilih_tujuan=1) and (pilih_maskapai=2) then begin harga:=2500000;
  end;
  
  if (pilih_tujuan=1) and (pilih_maskapai=3) then begin harga:=3500000
  end;
  
  if (pilih_tujuan=2) and (pilih_maskapai=1) then begin harga:=1200000;
  end;
  
  if (pilih_tujuan=2) and (pilih_maskapai=2) then begin harga:=2200000;
  end;
  
  if (pilih_tujuan=2) and (pilih_maskapai=3) then begin harga:=3200000
  end;
  
  if (pilih_tujuan=3) and (pilih_maskapai=1) then begin harga:=1000000;
  end;
  
  if (pilih_tujuan=3) and (pilih_maskapai=2) then begin harga:=2000000;
  end;
  
  if (pilih_tujuan=3) and (pilih_maskapai=3) then begin harga:=3000000;
  end;
  
  write('Jumlah kursi:');
  readln(kursi);
  if (kursi>3) then begin total_harga:=((harga*kursi)-((harga*kursi)*0.25));
  writeln('Diskon 25%');
  end;
  if (kursi<=3) then begin total_harga:=(harga*kursi);
  end;
  writeln(' ');
  writeln('Total harga=',total_harga);
  writeln(' ');
  writeln('===================================');
  writeln('         Struk Pembelian           ');
  writeln('Lokasi Awal  : Padang              ');
  writeln('Nama         : ' ,nama              );
  writeln('Umur         : ',umur               );
  writeln('Jenis kelamin: ',JK                 );
  writeln('-----------------------------------');
  writeln('Tujuan       : ',Tujuan             );
  writeln('Maskapai     : ',Maskapai           );
  writeln('Jumlah kursi : ',Kursi              );
  writeln('Total harga  : ',total_harga        );
  writeln('           TERIMA KASIH            ');
  writeln('===================================');
  readln;
end.
