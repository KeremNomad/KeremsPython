#C02_String.py

isim = "Osman"
soyisim = "Ayhan"
memleket = "Urfa"

tanitma = "Ismim " + isim + ", Soyismim " + soyisim + ", Memleketim " + memleket
len = len(tanitma)

print(tanitma)
print(len)
print(tanitma[6])

print(tanitma[6:11])
print(tanitma[:11])
print(tanitma[13:])
#
print(tanitma[::2])  #default degerler [0:len+1:1]
print(tanitma[::-1]) #afrU mitekelmeM ,nahyA mimsiyoS ,namsO mimsI
print(tanitma[1:1])