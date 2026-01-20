#C01_DegiskenTanimlama.py
pantolon = 100
t_shirt = 50
ayakkabi = 200

vergi = 0.2

#vergiDahilPantolonFiyati = 100 * 0.2 + 100
#vergiDahilT_shirtFiyati = 50 * 0.2 + 50
#vergiDahilAyakkabiFiyati = 200 * 0.2 + 200

vergiDahilPantolonFiyati = pantolon * vergi + pantolon
vergiDahilT_shirtFiyati = t_shirt * vergi + t_shirt
vergiDahilAyakkabiFiyati = ayakkabi * vergi + ayakkabi

print(vergiDahilAyakkabiFiyati)