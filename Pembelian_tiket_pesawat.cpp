include <iostream>
using namespace std;
string nama,umur,JK,tujuan,maskapai;
int kursi,pilih_tujuan,pilih_maskapai;
int harga,total_harga;

int main(){
    cout<<"Nama : Feruziakinta Syakira|"<<endl;
    cout<<"NIM  : 2310431008          |"<<endl;
    cout<<"Tugas: Modul II            |"<<endl;
    cout<<"----------------------------"<<endl;
    cout<<"\n";
    
    cout<<"Pembelian tiket pesawat Eagle"<<endl;
    cout<<"\n";
    cout<<"SELAMAT DATANG"<<endl;
    cout<<"SILAHKAN ISI (tanpa spasi)"<<endl;
    cout<<"\n";
    
    cout<<"Nama         :";cin>>nama;
    cout<<"Umur         :";cin>>umur;
    cout<<"Jenis kelamin:";cin>>JK;
    cout<<"\n";
    cout<<"Pembelian tiket pesawat eagle \n\n";
    cout<<"\n";
    
    cout<<"|====================|"<<endl;
    cout<<"|Tujuan keberangkatan|"<<endl;
    cout<<"|1. Jakarta          |"<<endl;
    cout<<"|2. Yogyakarta       |"<<endl;
    cout<<"|3. Bandung          |"<<endl;
    cout<<"|====================|"<<endl;
    cout<<"\n";
    cout<<"pilih tujuan : ";cin>>pilih_tujuan;

    if(pilih_tujuan==1){
        cout<<"Jakarta"<<endl;
        if(pilih_tujuan==1){
            tujuan="Jakarta";
        }
    }
    if(pilih_tujuan==2){
        cout<<"Yogyakarta"<<endl;
        if(pilih_tujuan==2){
            tujuan="Yogyakarta";
        }
    }
     if(pilih_tujuan==3){
        cout<<"Bandung"<<endl;
        if(pilih_tujuan==3){
            tujuan="Bandung";
        }
    }
    cout<<"\n";
    cout<<"|==============|"<<endl;
    cout<<"|Jenis maskapai|"<<endl;
    cout<<"|1. Ekonomi    |"<<endl;
    cout<<"|2. Business   |"<<endl;
    cout<<"|3. First Class|"<<endl;
    cout<<"|==============|"<<endl;
    cout<<"\n";
    cout<<"Pilih maskapai : ";cin>>pilih_maskapai;

    if(pilih_maskapai==1){
        cout<<"Ekonomi"<<endl;
        if(pilih_maskapai==1){
            maskapai="Ekonomi";
        }
    }
    if(pilih_maskapai==2){
        cout<<"Business"<<endl;
        if(pilih_maskapai==2){
            maskapai="Business";
        }
    }
     if(pilih_maskapai==3){
        cout<<"First Class"<<endl;
        if(pilih_maskapai==3){
            maskapai="First Class";
        }
    }
    cout<<"\n";
     if((pilih_tujuan==1)&&(pilih_maskapai==1)){
         harga=1500000;
    }
     if((pilih_tujuan==1)&&(pilih_maskapai==2)){
         harga=2500000;
    }
     if((pilih_tujuan==1)&&(pilih_maskapai==3)){
         harga=3500000;
    }
     if((pilih_tujuan==2)&&(pilih_maskapai==1)){
         harga=1200000;
    }
     if((pilih_tujuan==2)&&(pilih_maskapai==2)){
         harga=2200000;
    }
     if((pilih_tujuan==2)&&(pilih_maskapai==3)){
         harga=3200000;
    }
     if((pilih_tujuan==3)&&(pilih_maskapai==1)){
         harga=1000000;
    }
     if((pilih_tujuan==3)&&(pilih_maskapai==2)){
         harga=2000000;
    }
     if((pilih_tujuan==3)&&(pilih_maskapai==3)){
         harga=3000000;
    }
    cout<<"Jumlah Kursi : ";cin>>kursi;
    if(kursi>3){
        total_harga=((harga*kursi)-(0.25*(harga*kursi)));
        if(kursi>3){
        cout<<"Diskon 25%"<<endl;
        }
    }
    if (kursi<=3){
        total_harga=harga*kursi;
    }
    cout<<"Total Harga = "<<total_harga<<endl;
    cout<<"\n";

    cout<<"====================================="<<endl;
    cout<<"         Struk pembelian   "<<endl;
    cout<<"Nama         : "<<nama<<endl;
    cout<<"Umur         : "<<umur<<endl;
    cout<<"Jenis Kelamin: "<<JK<<endl;
    cout<<"-------------------------------------"<<endl;
    cout<<"Tujuan       : "<<tujuan<<endl;
    cout<<"Maskapai     : "<<maskapai<<endl;
    cout<<"Jumlah Kursi : "<<kursi<<endl;
    cout<<"Total Harga  : "<<total_harga<<endl;
    cout<<"         TERIMA KASIH"<<endl;
    cout<<"======================================";

return 0;
}
