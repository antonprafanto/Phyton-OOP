"""
01_dasar_inheritance.py
=======================
Modul 4: Pilar 2 – Inheritance (Pewarisan Sifat & DRY)

File ini mendemonstrasikan:
1. Hubungan Parent Class dan Child Class (IS-A)
2. Pemanfaatan super().__init__() untuk kode DRY (Don't Repeat Yourself)
3. Pengecekan garis keturunan dengan isinstance() dan issubclass()
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
# 2. CHILD CLASS 1: MOBIL (MEWARISI KENDARAAN)
# ==============================================================
class Mobil(Kendaraan):
    def __init__(self, merk: str, warna: str, kapasitas_bensin: int, jumlah_pintu: int):
        # Panggil tugas orang tua untuk mengisi merk, warna, dan bensin:
        super().__init__(merk, warna, kapasitas_bensin)
        
        # Fitur khusus mobil:
        self.jumlah_pintu = jumlah_pintu
        self.ac_menyala = False

    def nyalakan_ac(self):
        self.ac_menyala = True
        print(f"[{self.merk}] AC kabin dinyalakan. Sejuk!")


# ==============================================================
# 3. CHILD CLASS 2: MOTOR (MEWARISI KENDARAAN)
# ==============================================================
class SepedaMotor(Kendaraan):
    def __init__(self, merk: str, warna: str, kapasitas_bensin: int, tipe_kopling: str):
        super().__init__(merk, warna, kapasitas_bensin)
        self.tipe_kopling = tipe_kopling

    # Overriding (Menimpa suara klakson agar lebih cempreng):
    def klakson(self):
        print(f"[{self.merk}] Tiit tiit! (Klakson motor cempreng)")

    def atraksi_wheelie(self):
        print(f"[{self.merk}] Mengangkat roda depan (Wheelie)! Hati-hati jatuh!")


# --- PENGUJIAN ---
print("\n--- 1. Menguji Objek Mobil ---")
avanza = Mobil("Toyota Avanza", "Putih", 45, 4)
avanza.nyalakan_mesin()      # Warisan dari Kendaraan
avanza.klakson()             # Warisan dari Kendaraan
avanza.nyalakan_ac()         # Fitur khusus Mobil
avanza.isi_bensin(10)        # Warisan dari Kendaraan

print("\n--- 2. Menguji Objek Sepeda Motor ---")
vespa = SepedaMotor("Vespa Matic", "Kuning", 7, "Otomatis")
vespa.nyalakan_mesin()       # Warisan dari Kendaraan
vespa.klakson()              # Suara khusus motor (Overridden)
vespa.atraksi_wheelie()      # Fitur khusus Sepeda Motor

# --- PENGECEKAN SILSILAH KETURUNAN ---
print("\n--- 3. Pengecekan Silsilah Keturunan ---")
print(f"Apakah avanza adalah Mobil?       -> {isinstance(avanza, Mobil)}")
print(f"Apakah avanza adalah Kendaraan?   -> {isinstance(avanza, Kendaraan)}")
print(f"Apakah avanza adalah SepedaMotor? -> {isinstance(avanza, SepedaMotor)}")

print(f"\nApakah Mobil anak dari Kendaraan?       -> {issubclass(Mobil, Kendaraan)}")
print(f"Apakah SepedaMotor anak dari Kendaraan? -> {issubclass(SepedaMotor, Kendaraan)}")
print(f"Apakah Kendaraan anak dari Mobil?       -> {issubclass(Kendaraan, Mobil)}")

print("\n" + "=" * 60)
print("[OK] Selesai: Konsep pewarisan berjalan efisien tanpa duplikasi kode.")
print("=" * 60)
