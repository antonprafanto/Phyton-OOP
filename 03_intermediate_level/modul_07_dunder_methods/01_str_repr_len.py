"""
01_str_repr_len.py
==================
Modul 7: Python Superpowers – Dunder Methods & Serialisasi JSON

File ini mendemonstrasikan:
1. Perbedaan __str__ (untuk user) vs __repr__ (untuk programmer/debug)
2. Mekanisme fallback: apa yang terjadi jika __str__ tidak ada
3. Mengaktifkan fungsi bawaan len() dengan __len__
"""
import sys

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

print("=" * 60)
print("[DEMO] DUNDER METHODS: __str__, __repr__, & __len__")
print("=" * 60)

class Buku:
    def __init__(self, judul: str, penulis: str, tahun: int):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun

    # 1. UNTUK PENGGUNA (PRINT / UI): Ramah manusia
    def __str__(self) -> str:
        return f"'{self.judul}' karya {self.penulis} ({self.tahun})"

    # 2. UNTUK PROGRAMMER (LOGGING / DEBUG): Format kode Python asli
    def __repr__(self) -> str:
        return f"Buku(judul='{self.judul}', penulis='{self.penulis}', tahun={self.tahun})"


class RakPerpustakaan:
    def __init__(self, nama_rak: str):
        self.nama_rak = nama_rak
        self.daftar_buku = []

    def simpan_buku(self, buku: Buku):
        self.daftar_buku.append(buku)
        print(f"[RAK] Buku {buku} berhasil ditambahkan ke '{self.nama_rak}'.")

    # 3. MENGAKTIFKAN FUNGSI len(rak):
    def __len__(self) -> int:
        return len(self.daftar_buku)

    def __str__(self) -> str:
        return f"Rak '{self.nama_rak}' berisi {len(self)} buku"


# --- PENGUJIAN ---
b1 = Buku("Laskar Pelangi", "Andrea Hirata", 2005)
b2 = Buku("Filosofi Teras", "Henry Manampiring", 2018)

print("\n--- 1. Uji Coba __str__ vs __repr__ pada Objek Buku ---")
print(f"Menggunakan str()  : {str(b1)}")
print(f"Menggunakan print(): {b1}")
print(f"Menggunakan repr() : {repr(b1)}")

print("\n--- 2. Uji Coba __len__ pada Rak Perpustakaan ---")
rak_novel = RakPerpustakaan("Koleksi Sastra & Self-Help")
print(f"Jumlah awal buku di rak : len(rak_novel) = {len(rak_novel)}")

rak_novel.simpan_buku(b1)
rak_novel.simpan_buku(b2)

print(f"Jumlah akhir buku di rak: len(rak_novel) = {len(rak_novel)}")
print(f"Informasi Rak: {rak_novel}")

print("\n" + "=" * 60)
print("[OK] Selesai: Objek sekarang berbicara dalam bahasa alami Python.")
print("=" * 60)
