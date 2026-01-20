#C03_InputOrnek.py
siparis1 =int(input("lutfen birinci siparisin fiyatini giriniz"))
siparis2 =int(input("lutfen ikinci siparisin fiyatini giriniz"))
siparis3 =int(input("lutfen ucuncu siparisin fiyatini giriniz"))

vergi =float(input("vergi oranini giriniz"))

vergiDahilSiparis1 = siparis1 * vergi +  siparis1
vergiDahilSiparis2 = siparis2 * vergi +  siparis2
vergiDahilSiparis3 = siparis3 * vergi +  siparis3


toplam= vergiDahilSiparis1 + vergiDahilSiparis2 + vergiDahilSiparis3
print("fiyatlari verilen 3 siparisin vergiler dahil toplam fiyati" + str(toplam))
