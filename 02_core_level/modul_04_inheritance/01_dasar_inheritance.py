"""
01_dasar_inheritance.py
=======================
Modul 4: Pilar 2 – Inheritance (Pewarisan Sifat & DRY)

File ini mendemonstrasikan:
1. Hubungan Parent Class dan Child Class (IS-A)
2. Pemanfaatan super().__init__() untuk inisialisasi DRY
3. Memperkaya method orang tua dengan super().method() (kasus Mobil Ambulans)
4. Pengecekan garis keturunan dengan isinstance() dan issubclass()
"""
import sys

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

print("=" * 60)
print("[DEMO] DASAR INHERITANCE (PEWARISAN KENDARAAN)")
print("=" * 60)

# ==============================================================
# 1. PARENT CLASS (KELAS INDUK)
# ==============================================================
class Kendaraan:
    def __init__(self, merk: str, warna: str, kapasitas_bensin: int):
        self.merk = merk
        self.warna = warna
        self.bensin = kapasitas_bensin
        self.kecepatan = 0

    def nyalakan_mesin(self):
        print(f"[{self.merk}] Mesin dinyalakan... Brum brum!")

    def klakson(self):
        print(f"[{self.merk}] Tiiin tiiin!")

    def isi_bensin(self, liter: int):
        self.bensin += liter
        print(f"[{self.merk}] Mengisi bensin +{liter}L. Total bensin: {self.bensin}L")


# ==============================================================
# 2. CHILD CLASS 1: MOBIL BIASA
# ==============================================================
class Mobil(Kendaraan):
    def __init__(self, merk: str, warna: str, kapasitas_bensin: int, jumlah_pintu: int):
        # Panggil tugas orang tua untuk mengisi data umum:
        super().__init__(merk, warna, kapasitas_bensin)
        self.jumlah_pintu = jumlah_pintu
        self.ac_menyala = False

    def nyalakan_ac(self):
        self.ac_menyala = True
        print(f"[{self.merk}] AC kabin dinyalakan. Sejuk!")


# ==============================================================
# 3. CHILD CLASS 2: AMBULANS (MEMPERKAYA METHOD super().klakson())
# ==============================================================
class Ambulans(Kendaraan):
    def klakson(self):
        # 1. Jalankan dulu bunyi klakson bawaan orang tua:
        super().klakson()
        # 2. Tambahkan aksi khusus milik ambulans di bawahnya:
        print(f"[{self.merk}] Wiuuu wiuuu! Sirine darurat dinyalakan!")


# ==============================================================
# 4. CHILD CLASS 3: SEPEDA MOTOR (OVERRIDE TOTAL)
# ==============================================================
class SepedaMotor(Kendaraan):
    def __init__(self, merk: str, warna: str, kapasitas_bensin: int, tipe_kopling: str):
        super().__init__(merk, warna, kapasitas_bensin)
        self.tipe_kopling = tipe_kopling

    # Overriding Total (Menimpa suara klakson bawaan dengan suara baru):
    def klakson(self):
        print(f"[{self.merk}] Tiit tiit! (Klakson motor cempreng)")


# --- PENGUJIAN ---
print("\n--- 1. Menguji Objek Mobil Biasa ---")
avanza = Mobil("Toyota Avanza", "Putih", 45, 4)
avanza.nyalakan_mesin()
avanza.klakson()
avanza.nyalakan_ac()

print("\n--- 2. Menguji Objek Ambulans (super().klakson()) ---")
amb = Ambulans("Toyota HiAce Ambulans", "Putih", 60)
amb.nyalakan_mesin()
amb.klakson()  # Menghasilkan suara klakson induk + sirine!

print("\n--- 3. Menguji Objek Sepeda Motor (Override Total) ---")
vespa = SepedaMotor("Vespa Matic", "Kuning", 7, "Otomatis")
vespa.klakson()

# --- PENGECEKAN SILSILAH KETURUNAN ---
print("\n--- 4. Pengecekan Silsilah Keturunan ---")
print(f"Apakah amb adalah Ambulans?  -> {isinstance(amb, Ambulans)}")
print(f"Apakah amb adalah Kendaraan? -> {isinstance(amb, Kendaraan)}")
print(f"Apakah Ambulans anak dari Kendaraan? -> {issubclass(Ambulans, Kendaraan)}")

print("\n" + "=" * 60)
print("[OK] Selesai: Konsep pewarisan dan super() bekerja sempurna.")
print("=" * 60)
