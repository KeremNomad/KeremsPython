#C01_VeriTipiDonusturme.py

#Dairenin Alani
#Dairenin Cevresi
#Yari Capi Kullanicidan Alinan Bir Dairenin Alan ve Cevresini Hesaplayiniz

#Dairenin Alani: pi * (r**2)
#Daire Cevresi: pi * r * 21

r = int(input("Lutfen Dairenin Yari Capini Giriniz: ")) #5
pi = 3

daireninAlani = pi * (r**2)
daireCevresi = pi * r * 2

print("Yari Capi Kullanicidan " + str(r) + " Olarak Alinan Bir Dairenin Alani: " +  str(daireninAlani) ,
      "\nYari Capi Kullanicidan " + str(r) + " Olarak Alinan Bir Dairenin Cevresi: " +  str(daireCevresi))