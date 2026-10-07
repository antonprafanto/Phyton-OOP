"""
01_masalah_prosedural.py
========================
Modul 0: Mengapa Kita Butuh OOP?

File ini mendemonstrasikan bagaimana koding gaya prosedural (tanpa objek)
menjadi mimpi buruk ketika data aplikasi mulai bertambah banyak.
"""
import sys

# Memastikan output terminal mendukung encoding UTF-8 di Windows
if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

print("=" * 60)
print("[!] SIMULASI KODE PROSEDURAL (VARIABEL TERCECER)")
print("=" * 60)

# Bayangkan kita mengelola 3 akun nasabah bank secara terpisah
nasabah_nama = ["Budi", "Siti", "Ahmad"]
nasabah_rekening = ["101", "102", "103"]
nasabah_saldo = [500_000, 1_200_000, 350_000]

def tampilkan_data():
    print("\n--- Data Nasabah Saat Ini ---")
    for i in range(len(nasabah_nama)):
        print(f"[{i}] {nasabah_nama[i]} (No: {nasabah_rekening[i]}) -> Saldo: Rp {nasabah_saldo[i]:,}")

tampilkan_data()

# --- MASALAH 1: Data Tidak Terikat (Desinkronisasi) ---
print("\n" + "-" * 60)
print("[PERINGATAN] SKENARIO BAHAYA 1: Hapus Nasabah Tapi Lupa Hapus Saldo")
print("-" * 60)
print("Kasus: Siti menutup akunnya (indeks ke-1 dihapus dari list nama)...")

# Programmer menghapus Siti dari list nama, tetapi lupa menghapus dari list rekening & saldo:
nasabah_nama.pop(1)  # Menghapus 'Siti'

print("\n[!] LIHAT APA YANG TERJADI PADA DATA KITA SEKARANG:")
tampilkan_data()
print("\n>>> BENCANA: Ahmad sekarang memegang saldo milik Siti (Rp 1.200.000)!")
print("    Karena data nama, nomor rekening, dan saldo tidak menempel jadi satu kesatuan!")

# --- MASALAH 2: Tidak Ada Proteksi Aturan ---
print("\n" + "-" * 60)
print("[PERINGATAN] SKENARIO BAHAYA 2: Saldo Diubah Sembarangan dari Luar")
print("-" * 60)
# Siapa saja bisa mengubah saldo secara ilegal tanpa lewat fungsi validasi:
nasabah_saldo[0] = -999_999_999  # Saldo Budi jadi minus sembarangan
print(f"Saldo Budi tiba-tiba menjadi: Rp {nasabah_saldo[0]:,}")
print(">>> Tidak ada benteng pelindung data!")
print("=" * 60)
