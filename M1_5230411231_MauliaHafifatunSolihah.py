# LUAS SEGITIGA (2D)

print("-"*10 + " MENGHITUNG LUAS SEGITIGA " + "-"*10)

def menghitung_luas_segitiga(alas, tinggi):
    luas = 0.5 * alas * tinggi
    return luas 

# input dan hitung
alas = float(input("Masukkan Alas Segitiga :"))
tinggi = float (input("Masukkan Tinggi Segitiga :"))

hitungluas = menghitung_luas_segitiga(alas, tinggi)

print(f"Luas Segitiga : {hitungluas}")

print("-"*16 + " TERIMA KASIH " + "-"*16)

# LUAS KUBUS (3D)

print("-"*10 + " MENGHITUNG LUAS KUBUS " + "-"*10)

def mengitung_luas_kubus(sisi):
    luas = 6 * (sisi ** 2)
    return luas

# input dan hitung
sisi = float(input("Masukkan Panjang Sisi Kubus : "))

hitungluas_kubus = mengitung_luas_kubus(sisi)

print(f"Luas Permukaan Kubus : {hitungluas_kubus}")

print("-"*15 + " TERIMA KASIH " + "-"*15)
