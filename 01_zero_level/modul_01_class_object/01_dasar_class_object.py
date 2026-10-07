"""
01_dasar_class_object.py
========================
Modul 1: Melahirkan Objek Pertama (Class, Object, Constructor, & self)

File ini mendemonstrasikan cara:
1. Mendefinisikan class & constructor dengan DEFAULT PARAMETERS
2. Membaca & mengubah atribut langsung (dot notation '.')
3. Membuat method (perilaku objek)
4. Melahirkan beberapa objek nyata di memori & membuktikan isolasi memori dengan id()
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

# 1. CETAKAN (CLASS) DENGAN DEFAULT PARAMETER
class Kucing:
    """Cetak biru untuk menciptakan objek kucing."""
    
    # Nilai default: jika warna tidak diisi -> "Putih", umur tidak diisi -> 1
    def __init__(self, nama: str, warna_bulu: str = "Putih", umur: int = 1):
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


# 2. MELAHIRKAN DUA OBJEK BERBEDA
print("\n--- 1. Melahirkan Dua Kucing Berbeda ---")
# Kucing 1: Semua data diisi lengkap
kucing_a = Kucing("Mimi", "Oranye", 2)

# Kucing 2: Memanfaatkan Default Parameter (hanya isi nama, warna & umur otomatis)
kucing_b = Kucing("Snowy")

# 3. MEMANGGIL METHOD MASING-MASING OBJEK
print("\n--- 2. Memanggil Perkenalan ---")
kucing_a.perkenalan()
print()
kucing_b.perkenalan()

# 4. MEMBACA & MENGUBAH ATRIBUT LANGSUNG DENGAN TITIK (.)
print("\n--- 3. Mengubah Atribut Langsung ---")
print(f"Nama lama kucing_a: {kucing_a.nama}")
kucing_a.nama = "Mimi Si Manis"
print(f"Nama baru kucing_a: {kucing_a.nama}")

# 5. PEMBUKTIAN ALAMAT MEMORI DENGAN id()
print("\n--- 4. Pembuktian Isolasi Memori di RAM Komputer ---")
print(f"Alamat fisik memori kucing_a : {id(kucing_a)}")
print(f"Alamat fisik memori kucing_b : {id(kucing_b)}")
print(f"Apakah kucing_a dan kucing_b adalah objek yang sama di RAM? -> {kucing_a is kucing_b}")

print("\n--- 5. Interaksi Mandiri Objek ---")
kucing_a.makan("Ikan Tongkol")
kucing_a.lari()
print(f"Energi kucing_b tetap {kucing_b.energi}/100 (Tidak ikut berkurang!).")

print("\n" + "=" * 60)
print("[OK] Selesai: Objek-objek hidup mandiri di memori komputer.")
print("=" * 60)
