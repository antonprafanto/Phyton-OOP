"""
01_dasar_class_object.py
========================
Modul 1: Melahirkan Objek Pertama (Class, Object, Constructor, & self)

File ini mendemonstrasikan cara:
1. Mendefinisikan class
2. Menyiapkan atribut di dalam __init__
3. Membuat method (perilaku objek)
4. Melahirkan beberapa objek nyata di memori
"""
import sys

# Memastikan terminal Windows mendukung output dengan benar
if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

print("=" * 60)
print("[DEMO] DASAR MEMBUAT CLASS & MELAHIRKAN OBJEK")
print("=" * 60)

# 1. CETAKAN (CLASS)
class Kucing:
    """Cetak biru untuk menciptakan objek kucing."""
    
    def __init__(self, nama: str, warna_bulu: str, umur: int):
        # Data yang menempel pada tubuh masing-masing kucing (Instance Attributes)
        self.nama = nama
        self.warna_bulu = warna_bulu
        self.umur = umur
        self.energi = 50  # Semua kucing lahir dengan energi awal 50

    def perkenalan(self):
        """Method untuk memperkenalkan diri."""
        print(f"[KUCING] Halo! Aku {self.nama}, warna buluku {self.warna_bulu}, umurku {self.umur} tahun.")
        print(f"         Status energi saat ini: {self.energi}/100")

    def bersuara(self):
        """Method untuk mengeong."""
        print(f"[MEONG] {self.nama}: Meooong... purrrr~")

    def makan(self, porsi_makanan: str):
        """Method untuk makan dan menambah energi."""
        print(f"[MAKAN] {self.nama} sedang makan {porsi_makanan}...")
        self.energi = min(100, self.energi + 20)
        print(f"        Energi {self.nama} meningkat menjadi: {self.energi}/100")

    def lari(self):
        """Method untuk berlari dan menghabiskan energi."""
        if self.energi >= 15:
            self.energi -= 15
            print(f"[LARI] {self.nama} berlari keliling ruangan! (Sisa energi: {self.energi}/100)")
        else:
            print(f"[LEMAS] {self.nama} terlalu lelah untuk berlari. Butuh makan dulu!")


# 2. MELAHIRKAN DUA OBJEK BERBEDA DARI SATU CETAKAN
print("\n--- 1. Melahirkan Dua Kucing Berbeda ---")
kucing_a = Kucing("Mimi", "Oranye", 2)
kucing_b = Kucing("Blacky", "Hitam Legam", 3)

# 3. MEMANGGIL METHOD MASING-MASING OBJEK
print("\n--- 2. Memanggil Perkenalan ---")
kucing_a.perkenalan()
print()
kucing_b.perkenalan()

print("\n--- 3. Aksi Kucing A (Mimi) ---")
kucing_a.bersuara()
kucing_a.makan("Ikan Tongkol")
kucing_a.lari()

print("\n--- 4. Cek Kucing B (Blacky) ---")
print(f"Perhatikan: Energi Blacky tetap {kucing_b.energi}/100 (TIDAK terpengaruh oleh aksi Mimi!)")

print("\n" + "=" * 60)
print("[OK] Selesai: Objek-objek hidup mandiri di memori komputer.")
print("=" * 60)
