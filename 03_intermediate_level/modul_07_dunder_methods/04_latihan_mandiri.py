"""
04_latihan_mandiri.py
=====================
Modul 7: Python Superpowers – Dunder Methods & Serialisasi JSON

TANTANGAN PRAKTEK: APLIKASI PLAYLIST MUSIK DIGITAL 🎵🎧

Skenario:
Anda sedang membangun fitur pemutar musik (seperti Spotify mini).
Setiap 'Playlist' berisi kumpulan objek 'Lagu', bisa dihitung panjangnya,
bisa digabungkan dua playlist dengan tanda '+', dan bisa disimpan ke file JSON!

KETENTUAN YANG HARUS ANDA BUAT:

1. KELAS 'Lagu':
   - __init__(judul: str, artis: str, durasi_detik: int)
   - __str__(): Mengembalikan teks "Judul - Artis (X detik)"
   - __eq__(): Dua lagu dianggap SAMA jika judul dan artisnya sama persis!
   - to_dict(): Mengembalikan kamus {"judul": ..., "artis": ..., "durasi_detik": ...}
   - @classmethod from_dict(cls, data): Mengembalikan objek Lagu baru

2. KELAS 'Playlist':
   - __init__(nama: str)
   - tambah_lagu(lagu: Lagu): Menambahkan lagu ke list self.daftar_lagu
   - __len__(): Mengembalikan jumlah lagu yang ada di dalam playlist
   - __str__(): Mengembalikan "Playlist '{nama}' ({jumlah_lagu} lagu)"
   - __add__(other): Menggabungkan dua objek Playlist menjadi satu Playlist baru bernama
                     "{self.nama} + {other.nama}" yang memuat seluruh lagu dari kedua playlist!
   - simpan_ke_json(nama_file: str): Menyimpan seluruh lagu ke file JSON
   - @classmethod muat_dari_json(cls, nama_file: str): Membaca file JSON dan mengembalikan objek Playlist

Instruksi:
Lengkapi bagian TODO di bawah ini. Kunci jawaban tersedia di '04_solusi_latihan.py'.
"""
import sys
import json
import os

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# ==============================================================
# 1. KELAS LAGU
# ==============================================================
class Lagu:
    def __init__(self, judul: str, artis: str, durasi_detik: int):
        self.judul = judul
        self.artis = artis
        self.durasi_detik = durasi_detik

    def __str__(self) -> str:
        # TODO 1: Kembalikan format string ramah pengguna
        pass

    def __eq__(self, other) -> bool:
        # TODO 2: Bandingkan kesamaan judul dan artis
        pass

    def to_dict(self) -> dict:
        return {"judul": self.judul, "artis": self.artis, "durasi_detik": self.durasi_detik}

    @classmethod
    def from_dict(cls, d: dict):
        return cls(d["judul"], d["artis"], d["durasi_detik"])


# ==============================================================
# 2. KELAS PLAYLIST
# ==============================================================
class Playlist:
    def __init__(self, nama: str):
        self.nama = nama
        self.daftar_lagu = []

    def tambah_lagu(self, lagu: Lagu):
        self.daftar_lagu.append(lagu)

    def __len__(self) -> int:
        # TODO 3: Kembalikan jumlah lagu di self.daftar_lagu
        pass

    def __str__(self) -> str:
        # TODO 4: Kembalikan representasi string playlist
        pass

    def __add__(self, other):
        # TODO 5: Gabungkan dua playlist menjadi objek Playlist baru!
        pass

    def simpan_ke_json(self, nama_file: str):
        # TODO 6: Simpan daftar lagu (dalam format dict) ke file JSON
        pass

    @classmethod
    def muat_dari_json(cls, nama_file: str):
        # TODO 7: Baca file JSON dan kembalikan objek Playlist baru
        pass


# --- PENGUJIAN KODE ANDA ---
if __name__ == "__main__":
    print("=" * 60)
    print("[TEST] MENGUJI PLAYLIST MUSIK DENGAN DUNDER & JSON")
    print("=" * 60)

    l1 = Lagu("Bohemian Rhapsody", "Queen", 354)
    l2 = Lagu("Fix You", "Coldplay", 295)
    l3 = Lagu("Fix You", "Coldplay", 295)  # Lagu kembar

    print(f"Lagu 1: {l1}")
    print(f"Apakah Lagu 2 sama dengan Lagu 3? -> {l2 == l3}")

    p_rock = Playlist("Koleksi Rock")
    p_rock.tambah_lagu(l1)

    p_chill = Playlist("Santai Sore")
    p_chill.tambah_lagu(l2)

    print(f"\n{p_rock} (Panjang: {len(p_rock)})")
    print(f"{p_chill} (Panjang: {len(p_chill)})")

    # Operator Overloading '+':
    p_mix = p_rock + p_chill
    print(f"\nGabungan: {p_mix} (Panjang: {len(p_mix)})")
    print("=" * 60)
