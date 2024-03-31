program SegitigaAngka;
uses crt; 
var
  tinggi, baris, kolom: integer;

begin
  clrscr;
  
  writeln(' Nama : Feruziakinta Syakira');
  writeln(' NIM  : 2310431008');
  writeln(' Shift: 1');
  writeln(' Tugas: Modul IV');
  writeln(' ');
  
  write('Masukkan tinggi segitiga: ');
  readln(tinggi);
  writeln(' ');
  if tinggi<=0 then begin writeln ('Terjadi kesalahan');
  write('Masukkan tinggi segitiga : ');
  readln(tinggi);
  writeln(' ');
  end;
  for baris := 1 to tinggi do
  begin
    for kolom := 1 to baris do
    begin
      write(' ',kolom, ' ');
    end;
    writeln(); 
  end;
  
  readln;
end.
