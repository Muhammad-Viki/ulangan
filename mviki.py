penonton = int(input("Masukkan jumlah penonton yang ingin membeli tiket"))
total_keseluruhan = 0

tiket_anak = 30000
tiket_dewasa = 50000
tiket_lansia = 35000

for i in range(penonton):
    jumlah_tiket = int(input("masukkan jumlah tiket yang akan dibeli"))
    usia = int(input("Masukkan usia anda")) 


    if usia <= 12:
        harga_tiket = tiket_anak
    elif usia >= 12 and usia <= 60:
        harga_tiket = tiket_dewasa
    else:
        harga_tiket = tiket_lansia
           

    total_harga = harga_tiket * jumlah_tiket
    print(f"total pemebeli {i+1} harga tiket yang harus dibayar adalah {total_harga}")

    print(f"total harga keseluruhan adalah {total_harga}")

