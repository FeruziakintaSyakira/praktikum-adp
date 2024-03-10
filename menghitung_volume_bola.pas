program menghitung_volume_bola;
uses crt;
var
  r,phi,volume:real;
 begin
  clrscr;
  writeln('Nama : Feruziakinta Syakira');
  Writeln('NIM  : 2310431008');
  writeln('Shift: 1');
  writeln('');
  
  phi:=22/7;
  write('Jari-jari = ');
  readln(r);
  volume:=(4*phi*r*r*r)/3;
  writeln('Volume    = ',volume);
  readln;
end.
