#C02_String.py

ad, soyad, yas, ulke = "Ahmet", "Guclu", 16, "Danmark"

tanitma = f"Benim adim {ad} {soyad} yasim {yas} memleketim {ulke}"
print(tanitma)

# ahmet guclu ismindeki a ve g harflerini buyuk harf yapiniz
isim = "ahmet guclu"
isim = "A" + isim[1:6] + "G" + isim[7:]
print(isim)

print(tanitma.title())