import random
import time


class Kumanda():

    def __init__ (self, tv_durum="kapalı", tv_ses=0, kanal_list="Trt"):

        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_list = kanal_list
       

    def tv_ac(self):

        if (self.tv_durum == "acik"):
            print("tv zaten acik.")
        else:
            print("tv aciliyor.")
            self.tv_durum = "acik"

    def tv_kapat(self):
        if (self.tv_durum == "kapali"):
            print("tv zaten kapali.")
        else:
            print("tv kapatiliyor.")
            self.tv_durum = "kapali"

    def ses_ayarlari(self):

        while True:
            cevap = input("sesi azalt:'<' \nsesi arttir:'>'\ncikis : exit ")

            if (cevap == '<'):
                if (self.tv_ses != 0):
                    self.tv_ses -= 1
                    print("Ses:", self.tv_ses)
            elif (cevap == '>'):
                if (self.tv_ses != 31):
                    self.tv_ses += 1
                    print("Ses", self.tv_ses)
            else:
                print("ses guncellendi.", self.tv_ses)
                break
    def kanal_ekle (self,kanal_ismi):
        print("kanal ekleniyor...")
        time.sleep(1)

        self.kanal_list.append(kanal_ismi)
        print("kanal eklendi...")

    def rastgele_kanal(self):
        rastgele = random.randint(0,len(self.kanal_list)-1)

        self.kanal =self.kanal_list(rastgele)
        print("simdiki kanal:", self.kanal)
        
        
    def __len__(self):
        return len(self.kanal_list)
    
    def __str__(self):
        return ("Tv durumu: {}\nTv ses: {}\nKanal list: {}\nSu anki kanal: {}\n".format(self.tv_durum,self.tv_ses,self.kanal_list,self.kanal))

kumanda = Kumanda()
        

print(" TV Uygulaması "
     " 1. Tv Ac"
     " 2. Tv Kapat"
     " 3. Ses Ayarları"
     " 4. Kanal Ekle"
     " Çıkmak için q ya bas.")
        
        
while True:
       islem = input("islem sec:")

       if(islem == "q"):
                print("prog.sonladirildi.")
                break
            
       if(islem == "1"):
                kumanda.tv_ac()
                
       elif(islem== "2"):
                kumanda.tv_kapat()
            
       elif(islem == "3"):
               kumanda.ses_ayarlari()
               
       elif(islem == "4"):
              kanal_ismi = input("kanal isimlerini ',' ile ayırarak girin.")
              
              kanal_list= kanal_ismi.split(',')
              
              for eklenecekler in kanal_list:
                  kumanda.kanal_ekle(eklenecekler)
              
       else:
                print("geçersiz işlem")
           

                

