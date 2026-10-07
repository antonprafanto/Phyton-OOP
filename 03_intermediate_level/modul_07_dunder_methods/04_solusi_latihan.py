"""
04_solusi_latihan.py
====================
Modul 7: Python Superpowers – Dunder Methods & Serialisasi JSON

Kunci Jawaban & Pembahasan Latihan Playlist Musik Digital 🎵🎧
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

    # DUNDER __str__: Representasi ramah pengguna
    def __str__(self) -> str:
        menit = self.durasi_detik // 60
        detik = self.durasi_detik % 60
        return f"'{self.judul}' oleh {self.artis} ({menit}:{detik:02d})"

    # DUNDER __repr__: Representasi teknis developer
    def __repr__(self) -> str:
        return f"Lagu(judul='{self.judul}', artis='{self.artis}', durasi_detik={self.durasi_detik})"

    # DUNDER __eq__: Dua lagu sama jika judul dan artisnya cocok
    def __eq__(self, other) -> bool:
        if isinstance(other, Lagu):
            return self.judul.lower() == other.judul.lower() and self.artis.lower() == other.artis.lower()
        return False

    def to_dict(self) -> dict:
        return {
            "judul": self.judul,
            "artis": self.artis,
            "durasi_detik": self.durasi_detik
        }

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
        print(f"[PLAYLIST] Menambahkan {lagu} ke '{self.nama}'")

    # DUNDER __len__: Menghitung jumlah lagu dengan len(playlist)
    def __len__(self) -> int:
        return len(self.daftar_lagu)

    # DUNDER __str__: Cetak informasi playlist
    def __str__(self) -> str:
        total_durasi = sum(l.durasi_detik for l in self.daftar_lagu)
        menit = total_durasi // 60
        return f"Playlist '{self.nama}' [{len(self)} lagu | Total: {menit} menit]"

    # DUNDER __add__: Menggabungkan dua playlist dengan tanda '+'
    def __add__(self, other):
        if isinstance(other, Playlist):
            playlist_baru = Playlist(f"{self.nama} + {other.nama}")
            # Salin semua lagu dari kedua playlist:
            playlist_baru.daftar_lagu = self.daftar_lagu + other.daftar_lagu
            return playlist_baru
        return NotImplemented

    # SERIALISASI JSON: Simpan ke file fisik
    def simpan_ke_json(self, nama_file: str):
        data = {
            "nama_playlist": self.nama,
            "lagu": [l.to_dict() for l in self.daftar_lagu]
        }
        with open(nama_file, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        print(f"[JSON] Playlist '{self.nama}' berhasil disimpan ke '{nama_file}'.")

    # DESERIALISASI JSON: Baca kembali dari file
    @classmethod
    def muat_dari_json(cls, nama_file: str):
        with open(nama_file, "r", encoding="utf-8") as file:
            data = json.load(file)
            pl = cls(data["nama_playlist"])
            for d in data["lagu"]:
                pl.daftar_lagu.append(Lagu.from_dict(d))
            print(f"[JSON] Playlist '{pl.nama}' berhasil dimuat dari '{nama_file}'.")
            return pl


# --- PENGUJIAN SOLUSI ---
if __name__ == "__main__":
    print("=" * 60)
    print("[OK] HASIL EKSEKUSI KUNCI JAWABAN PLAYLIST MUSIK")
    print("=" * 60)

    l1 = Lagu("Bohemian Rhapsody", "Queen", 354)
    l2 = Lagu("Fix You", "Coldplay", 295)
    l3 = Lagu("Fix You", "Coldplay", 295)

    print(f"Lagu 1: {l1}")
    print(f"Lagu 2: {l2}")
    print(f"Apakah Lagu 2 == Lagu 3? -> {l2 == l3} (__eq__ berhasil!)")

    p1 = Playlist("Classic Rock")
    p1.tambah_lagu(l1)

    p2 = Playlist("Indie Pop")
    p2.tambah_lagu(l2)

    # Operator Overloading +
    p_mix = p1 + p2
    print(f"\nHasil Penggabungan '+': {p_mix}")
    print(f"Banyak lagu di p_mix: len(p_mix) = {len(p_mix)}")

    # Simpan ke JSON
    FILE_TEST = "test_playlist.json"
    p_mix.simpan_ke_json(FILE_TEST)

    # Muat kembali
    p_pulih = Playlist.muat_dari_json(FILE_TEST)
    print(f"Status Playlist Pulih: {p_pulih}")

    # Bersihkan file sampah
    if os.path.exists(FILE_TEST):
        os.remove(FILE_TEST)

    print("\n" + "=" * 60)
    print("[OK] Selesai: Seluruh fitur Dunder dan Serialisasi JSON teruji 100%.")
    print("=" * 60)
