program CaesarChiper;
uses crt;
const
  MAX_CHAR = 26;

var
  Kalimat: string;
  Geser, i: Integer;

begin  
clrscr;
  
  writeln(' Nama : Feruziakinta Syakira');
  writeln(' NIM  : 2310431008');
  writeln(' Shift: 1');
  writeln(' Tugas: Modul V');
  writeln(' ');                  
  
  writeln('Masukkan sebuah kalimat:');
  readln(Kalimat);

  write('Masukkan jumlah geser:');
  readln(Geser);

  for i := 1 to Length(kalimat) do
  begin
    if (kalimat[i] >= 'A') and (kalimat[i] <= 'Z') then
      kalimat[i] := Chr(((Ord(kalimat[i]) - Ord('A') + Geser) mod MAX_CHAR) + Ord('A'))
    else if (kalimat[i] >= 'a') and (kalimat[i] <= 'z') then
      kalimat[i] := Chr(((Ord(kalimat[i]) - Ord('a') + Geser) mod MAX_CHAR) + Ord('a'));
  end;

  writeln('Kalimat setelah digeser:');
  writeln(Kalimat);
readln;
end.
