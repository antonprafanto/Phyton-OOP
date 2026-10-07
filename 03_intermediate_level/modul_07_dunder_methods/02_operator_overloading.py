"""
02_operator_overloading.py
==========================
Modul 7: Python Superpowers – Dunder Methods & Serialisasi JSON

File ini mendemonstrasikan:
1. Mengapa secara default 'objek1 == objek2' membandingkan alamat RAM
2. Mengajari Python membandingkan isi sebenarnya dengan __eq__
3. Operator Overloading: Menjumlahkan objek dengan operator '+' (__add__)
"""
import sys

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

print("=" * 60)
print("[DEMO] OPERATOR OVERLOADING: __eq__ (==) & __add__ (+)")
print("=" * 60)

# ==============================================================
# 1. KASUS PERBANDINGAN NILAI DENGAN __eq__
# ==============================================================
class RekeningID:
    def __init__(self, kode_bank: str, nomor: str):
        self.kode_bank = kode_bank
        self.nomor = nomor

    # DUNDER __eq__: Menentukan kapan dua rekening dianggap SAMA
    def __eq__(self, other) -> bool:
        if isinstance(other, RekeningID):
            return self.kode_bank == other.kode_bank and self.nomor == other.nomor
        return False

rek1 = RekeningID("BCA", "12345678")
rek2 = RekeningID("BCA", "12345678")  # Datanya sama persis
rek3 = RekeningID("BRI", "12345678")

print("\n--- 1. Pengujian Perbandingan Nilai (__eq__) ---")
print(f"Apakah rek1 == rek2? -> {rek1 == rek2} (True karena data sama persis!)")
print(f"Apakah rek1 == rek3? -> {rek1 == rek3} (False karena beda bank)")
print(f"Apakah rek1 is rek2? -> {rek1 is rek2} (False karena dua alamat RAM berbeda!)")


# ==============================================================
# 2. OPERATOR OVERLOADING PENJUMLAHAN DENGAN __add__
# ==============================================================
class Dompet:
    def __init__(self, saldo: int):
        self.saldo = saldo

    # DUNDER __add__: Menentukan apa yang terjadi saat tanda '+' dipakai
    def __add__(self, other):
        if isinstance(other, Dompet):
            # Dompet + Dompet = Dompet baru dengan total saldo gabungan
            return Dompet(self.saldo + other.saldo)
        elif isinstance(other, (int, float)):
            # Dompet + Angka = Dompet baru
            return Dompet(self.saldo + int(other))
        return NotImplemented

    def __str__(self) -> str:
        return f"Dompet(Saldo: Rp {self.saldo:,})"


print("\n--- 2. Pengujian Operator Overloading Penjumlahan (__add__) ---")
dompet_pribadi = Dompet(150_000)
dompet_tabungan = Dompet(500_000)

print(f"Dompet Pribadi  : {dompet_pribadi}")
print(f"Dompet Tabungan : {dompet_tabungan}")

# 1. Menjumlahkan dua objek Dompet:
dompet_gabungan = dompet_pribadi + dompet_tabungan
print(f"\nHasil: dompet_pribadi + dompet_tabungan = {dompet_gabungan}")

# 2. Menjumlahkan Dompet dengan angka biasa (uang kaget):
dompet_bonus = dompet_gabungan + 50_000
print(f"Hasil: dompet_gabungan + Rp 50,000      = {dompet_bonus}")

print("\n" + "=" * 60)
print("[OK] Selesai: Operator '==' dan '+' sekarang bekerja alami pada objek kita.")
print("=" * 60)
