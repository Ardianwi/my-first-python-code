"""
Semua sintaksis dasar Bahasa pemrograman terdiri dari:
1. sekuensial: langkah berurutan
2. Percabangan: langkah melompat jika kondisi terpenuhi
3. Perulangan: mengulang langkah yang semua berkali-kali selama/sampai kondisi terpenuhi
"""

# Sekuensial
print('ibu menyuruh"pergi ke toko membeli telur dan susu"')
print('Budi menjawab,"Baik, apa yang saya lakukan di toko?"')
print('ibu menjawa, "Beli 1 botol susu, dan jika ada telur 6"')
print('Maka Budi berangkat sekarang')
print('Budi mulai berelanja')
print('Budi membeli susu 6')

# Percabangan

jumlah_botol_susu =100
jumlah_telur =183
print(f'jumlah botol susu {jumlah_botol_susu} botol')
print(f'jumlah telur {jumlah_telur} Butir')

if jumlah_botol_susu>0:
    print('Budi mengecek harga botol susu')
    if jumlah_telur==0:
        print('Budi membeli 1 botol susu')
    else:
        print('Budi mebeli 6 botol susu')


else:
    print('Budi tidak jadi membeli botol susu')

print('Anak Pulang Ke Rumah')
print('Budi menyerahkan hasil ke Mama')

# Sequential

print('Ibu Berkata"Nak Beli ke toko dan beli susu 6 dan 1 wortel ya"')
print('Anak Berkata"OK!"')
print('Budi pergi ke toko dan membeli 6 botol susu dan 1 wortel')
print('Budi Pergi ke rumah')
print('Budi Menyerahkan hasil pembeliaannya')