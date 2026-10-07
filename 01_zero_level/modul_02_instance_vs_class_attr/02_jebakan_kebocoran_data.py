"""
02_jebakan_kebocoran_data.py
============================
Modul 2: Variabel Milik Siapa? (Instance vs Class Attributes)

File ini mendemonstrasikan KEBOCORAN DATA (DATA LEAK) yang terjadi
ketika pemula salah meletakkan tipe data yang bisa berubah (seperti list/dict)
di level Class, bukan di level Instance.
"""
import sys

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

print("=" * 60)
print("[BEDAH KASUS] BENCANA KEBOCORAN KERANJANG BELANJA")
print("=" * 60)

# ==============================================================
# 1. CARA YANG SALAH (KERANJANG JADI CLASS ATTRIBUTE)
# ==============================================================
print("\n[SKENARIO SALAH] Keranjang ditaruh di level Class:")

class UserSalah:
    keranjang = []  # <-- SALAH BESAR! List ini menjadi milik bersama!

    def __init__(self, nama: str):
        self.nama = nama

    def beli(self, barang: str):
        self.keranjang.append(barang)

user1 = UserSalah("Anton")
user2 = UserSalah("Budi")

print("1. Anton membeli 'Laptop Asus Rog':")
user1.beli("Laptop Asus Rog")

print(f"   Keranjang Anton : {user1.keranjang}")
print(f"   Keranjang Budi  : {user2.keranjang}")
print("   >>> PERINGATAN: Keranjang Budi ikut terisi belanjaan Anton!")

# ==============================================================
# 2. CARA YANG BENAR (KERANJANG JADI INSTANCE ATTRIBUTE)
# ==============================================================
print("\n" + "-" * 60)
print("[SKENARIO BENAR] Keranjang dibuat baru di dalam __init__:")

class UserBenar:
    def __init__(self, nama: str):
        self.nama = nama
        # Setiap kali user mendaftar, buatkan wadah list BARU milik pribadi:
        self.keranjang = []

    def beli(self, barang: str):
        self.keranjang.append(barang)

pembeli_anton = UserBenar("Anton")
pembeli_budi = UserBenar("Budi")

print("1. Anton membeli 'Smartphone Pixel':")
pembeli_anton.beli("Smartphone Pixel")

print("2. Budi membeli 'Headphone Sony':")
pembeli_budi.beli("Headphone Sony")

print(f"\n   Keranjang Anton : {pembeli_anton.keranjang}")
print(f"   Keranjang Budi  : {pembeli_budi.keranjang}")
print("   >>> AMAN: Belanjaan Anton dan Budi benar-benar terisolasi mandiri!")

print("\n" + "=" * 60)
print("[ATURAN EMAS] Jika datanya adalah koleksi pribadi (list/dict/set),")
print("SELALU buat di dalam __init__ menggunakan 'self.variabel = []'!")
print("=" * 60)
