# LUAS SEGITIGA

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