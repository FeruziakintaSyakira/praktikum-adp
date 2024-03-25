program perkalian_penjumlahan_nxn;
const 
  MAX_SIZE=10;
  Menu=3;
  
uses crt;
var
  i,n,j,pilih_menu:integer;
begin
  clrscr;
  writeln('Nama :Feruziakinta Syakira   |');
  writeln('NIM  :2310431008             |');
  writeln('Tugas:Modul III              |');
  writeln('Shift:1                      |');
  writeln('___________|');
  writeln(' ');

  write('Input n:');
  readln(n);
  writeln(' ');
  if (n > MAX_SIZE) then
  begin
    writeln('Terjadi kesalahan');
    write('Input n:');
    readln(n);
  end;
 repeat
 writeln(' ');
  begin
  writeln('|========================|');
  writeln('|       Pilih menu       |');
  writeln('|------------------------|');
  writeln('|1. Tabel perkalian nxn  |');
  writeln('|2. Tabel penjumlahan n+n|');
  writeln('|3. Keluar               |');
  writeln('|========================|');
  writeln(' ');
  end;
  writeln(' ');
  write ('Pilih menu :');
  readln(pilih_menu);
  if (pilih_menu > menu) then
  begin
    writeln('Terjadi kesalahan');
    write('Pilih menu :');
    readln(pilih_menu);
  end;
  writeln(' ');
  if (pilih_menu=1) then begin writeln('    Tabel perkalian nxn');
  writeln(' ');
  write('    ');
  for i := 1 to n do
    write(i:4,'|');
  writeln;
writeln('  ----------------------');
  
  for i := 1 to n do
  begin
    write(i:3,'|');
    for j := 1 to n do
      write((i * j):4,'|');
    writeln;
  end;
  end;
  if (pilih_menu=2) then begin writeln('   Tabel penjumlahan n+n');
  writeln(' ');
  write('    ');
  for i := 1 to n do
    write(i:4,'|');
  writeln;
writeln('  ----------------------');

  for i := 1 to n do
  begin
    write(i:3,'|');
    for j := 1 to n do
      write((i + j):4,'|');
    writeln;
  end;
  end;
 until pilih_menu=3;
  readln;
end.
