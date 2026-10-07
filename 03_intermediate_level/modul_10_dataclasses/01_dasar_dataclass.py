"""
================================================================================
MODUL 10: MODERN PYTHON SHORTCUT (@dataclass) & TYPE HINTING
Berkas 01: Dasar Pembuatan @dataclass & Penghematan Boilerplate
================================================================================
Tujuan Pembelajaran:
1. Membuktikan bagaimana dekorator @dataclass memangkas puluhan baris kode manual.
2. Memverifikasi 3 superpower otomatis:
   - Constructor __init__ otomatis
   - Representasi teks __repr__ otomatis
   - Perbandingan isi nilai __eq__ (==) otomatis
3. Mengonversi objek dataclass ke dictionary (asdict) dan tuple (astuple).
================================================================================
"""

import sys
from dataclasses import dataclass, asdict, astuple

# Konfigurasi terminal agar kompatibel dengan encoding Windows / UTF-8
if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass


# ==============================================================================
# 1. PERBANDINGAN: CARA LAMA (MANUAL) VS CARA MODERN (@dataclass)
# ==============================================================================

# --- A. CARA KONVENSIONAL (15 Baris Kode Membosankan) ---
class BukuManual:
    def __init__(self, judul: str, penulis: str, harga: int):
        self.judul = judul
        self.penulis = penulis
        self.harga = harga

    def __repr__(self) -> str:
        return f"BukuManual(judul='{self.judul}', penulis='{self.penulis}', harga={self.harga})"

    def __eq__(self, other) -> bool:
        if isinstance(other, BukuManual):
            return (self.judul, self.penulis, self.harga) == (other.judul, other.penulis, other.harga)
        return False


# --- B. CARA MODERN DENGAN @dataclass (CUKUP 5 BARIS!) ---
@dataclass
class BukuModern:
    judul: str
    penulis: str
    harga: int
    kategori: str = "Umum"  # Nilai default opsional


# ==============================================================================
# 2. PENGUJIAN DAN DEMONSTRASI LANGSUNG
# ==============================================================================
if __name__ == "__main__":
    print("=" * 65)
    print("[DEMO] KEAJAIBAN OTOMATISASI DENGAN @dataclass")
    print("=" * 65)

    # 1. Constructor Otomatis
    buku_a = BukuModern(
        judul="Atomic Habits",
        penulis="James Clear",
        harga=120_000,
        kategori="Self-Improvement"
    )
    buku_b = BukuModern(
        judul="Atomic Habits",
        penulis="James Clear",
        harga=120_000,
        kategori="Self-Improvement"
    )
    buku_c = BukuModern(
        judul="Clean Code",
        penulis="Robert C. Martin",
        harga=350_000
        # kategori akan otomatis default: "Umum"
    )

    print("\n--- 1. Uji __repr__ Otomatis (Tampilan Objek Cantik) ---")
    print(f"Buku A : {buku_a}")
    print(f"Buku C : {buku_c} (kategori otomatis terisi default)")

    print("\n--- 2. Uji __eq__ Otomatis (Perbandingan Nilai Data) ---")
    print(f"Apakah Buku A == Buku B? -> {buku_a == buku_b} (True karena data sama persis!)")
    print(f"Apakah Buku A == Buku C? -> {buku_a == buku_c} (False karena data berbeda)")
    print(f"Apakah Buku A is Buku B? -> {buku_a is buku_b} (False karena alamat memori RAM berbeda)")

    print("\n--- 3. Konversi Cepat ke Dictionary (asdict) & Tuple (astuple) ---")
    # Sangat berguna untuk integrasi API JSON atau database
    kamus_buku = asdict(buku_a)
    print(f"Hasil asdict()  : {kamus_buku}")
    print(f"Tipe Data       : {type(kamus_buku)}")

    tuple_buku = astuple(buku_c)
    print(f"\nHasil astuple() : {tuple_buku}")
    print(f"Tipe Data       : {type(tuple_buku)}")

    print("\n" + "=" * 65)
    print("[OK] Selesai: @dataclass sukses memangkas boilerplate code!")
    print("=" * 65)
