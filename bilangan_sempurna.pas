rogram CekBilanganSempurna;
uses crt;
var
  bilangan, counter, i: integer;
begin
  clrscr;
  writeln(' Nama : Feruziakinta Syakira');
  writeln(' NIM  : 2310431008');
  writeln(' Shift: 1');
  writeln(' Tugas: Modul IV');
  writeln(' ');
  
  write('Masukkan bilangan: ');
  readln(bilangan);
  writeln(' ');
  
  if bilangan < 0 then begin
    writeln('Terjadi Kesalahan');
    write('Masukkan bilangan : ');
    readln(bilangan);
    writeln(' ');
    end;

  counter := 0;
  for i := 1 to bilangan div 2 do
  begin
    if bilangan mod i = 0 then
      counter := counter + i;
  end;

  if counter = bilangan then
    writeln(bilangan, ' adalah bilangan sempurna')
  else
    writeln(bilangan, ' bukan bilangan sempurna');
writeln(' ');
begin
  if bilangan mod 2 = 0 then
    writeln(bilangan, ' adalah bilangan genap')
  else
    writeln(bilangan, ' adalah bilangan ganjil');
end;  
readln;
end.
