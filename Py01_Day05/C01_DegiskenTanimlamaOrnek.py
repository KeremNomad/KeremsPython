#C01_DegiskenTanimlamaOrnek.py

# Verilen 3 siparisin toplamini degiskenler olusturarak
# hesaplayip yazdiriniz

#   Siparis 1 = 510tl + Vergi
#   Siparis 2 = 2070.82tl + Vergi
#   Siparis 3 = 730tl + Vergi

#   Vergi oranlari %8 hesaplanacaktir

#3 siparisin degiskenlerinin olusturulmasi
siparis01 = 510
siparis02 = 2070.82
siparis03 = 730

#vergi degiskeninin olusturulmasi
vergi = 0.08

#vergi dahil fiyatlar icin degisken olusturma
vergiDahilSiparis01 = siparis01 * vergi + siparis01
vergiDahilSiparis02 = siparis02 * vergi + siparis02
vergiDahilSiparis03 = siparis03 * vergi + siparis03


#toplam icin degisken olusturma
toplam = vergiDahilSiparis03 + vergiDahilSiparis02 + vergiDahilSiparis01

print("Fiyatlari verilen 3 siparisin vergiler dahil toplam fiyati: ", (toplam))