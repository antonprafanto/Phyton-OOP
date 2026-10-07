"""
================================================================================
MODUL 8: METODE SPESIAL
Berkas 02: Pola Desain Alternative Constructor Menggunakan @classmethod
================================================================================
Tujuan Pembelajaran:
1. Memahami mengapa Python hanya mengizinkan SATU fungsi __init__.
2. Menguasai cara melahirkan objek dari berbagai format data mentah:
   - String CSV / Baris teks ("username,email,tahun")
   - Dictionary JSON / API Payload
   - Timestamp waktu UNIX
3. Membuktikan keunggulan penggunaan 'cls' dibanding nama Class eksplisit saat
   bekerja dengan pewarisan (Inheritance).
================================================================================
"""

import sys
from datetime import datetime

# Konfigurasi terminal agar kompatibel dengan encoding Windows / UTF-8
if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass


class Pengguna:
    """
    Blueprint Pengguna Sistem.
    Constructor utama (__init__) menghendaki parameter terpisah:
    username, email, dan tahun_lahir.
    """

    def __init__(self, username: str, email: str, tahun_lahir: int):
        self.username = username
        self.email = email
        self.tahun_lahir = tahun_lahir

    def hitung_usia(self, tahun_sekarang: int = 2026) -> int:
        return tahun_sekarang - self.tahun_lahir

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} user='{self.username}', email='{self.email}', tahun={self.tahun_lahir}>"

    # ==========================================================================
    # ALTERNATIVE CONSTRUCTOR 1: Melahirkan Objek dari String Format CSV
    # Masukan: "andi99, andi@gmail.com, 1998"
    # ==========================================================================
    @classmethod
    def dari_string_csv(cls, baris_teks: str):
        """
        Membaca sebaris teks CSV, membersihkan spasi,
        lalu melahirkan objek dengan cetakan 'cls'.
        """
        bagian = baris_teks.split(",")
        if len(bagian) != 3:
            raise ValueError(f"Format teks tidak valid! Diharapkan 3 kolom, diterima: {len(bagian)}")

        username = bagian[0].strip()
        email = bagian[1].strip()
        tahun_lahir = int(bagian[2].strip())

        # KUNCI UTAMA: Gunakan 'cls(...)', JANGAN 'Pengguna(...)'
        return cls(username=username, email=email, tahun_lahir=tahun_lahir)

    # ==========================================================================
    # ALTERNATIVE CONSTRUCTOR 2: Melahirkan Objek dari Dictionary (JSON API)
    # Masukan: {"user_id": "rudi_id", "email_address": "rudi@web.id", "birth_year": 2001}
    # ==========================================================================
    @classmethod
    def dari_payload_api(cls, payload: dict):
        """
        Memetakan nama field dari API eksternal ke parameter constructor kita.
        """
        return cls(
            username=payload["user_id"],
            email=payload["email_address"],
            tahun_lahir=int(payload["birth_year"])
        )

    # ==========================================================================
    # ALTERNATIVE CONSTRUCTOR 3: Melahirkan Objek dari UNIX Epoch Timestamp
    # ==========================================================================
    @classmethod
    def dari_timestamp_lahir(cls, username: str, email: str, epoch_detik: int):
        """
        Mengonversi detik UNIX timestamp menjadi angka tahun kelahiran.
        """
        waktu = datetime.fromtimestamp(epoch_detik)
        return cls(username=username, email=email, tahun_lahir=waktu.year)


# ==============================================================================
# SUBKELAS UNTUK MEMBUKTIKAN KEKUATAN 'cls' PADA INHERITANCE
# ==============================================================================
class Administrator(Pengguna):
    """Subkelas khusus admin sistem dengan status otorisasi."""
    def __init__(self, username: str, email: str, tahun_lahir: int, level_akses: int = 1):
        super().__init__(username, email, tahun_lahir)
        self.level_akses = level_akses

    def aksi_hapus_database(self):
        print(f"[AKSI ADMIN] {self.username} (Level {self.level_akses}) melakukan audit sistem!")


# ==============================================================================
# BLOK PENGUJIAN DAN DEMONSTRASI
# ==============================================================================
if __name__ == "__main__":
    print("=" * 65)
    print("[DEMO] ALTERNATIVE CONSTRUCTORS MENGGUNAKAN @classmethod")
    print("=" * 65)

    # 1. Cara Standar: Memanggil __init__ langsung
    user_standar = Pengguna("budi_santoso", "budi@mail.com", 1995)
    print(f"1. Instansiasi Standar       : {user_standar}")
    print(f"   Usia (tahun 2026)         : {user_standar.hitung_usia()} tahun\n")

    # 2. Alternative Constructor dari String CSV
    data_csv = "  citra_ayu , citra@kantor.co.id , 2000  "
    user_csv = Pengguna.dari_string_csv(data_csv)
    print(f"2. Dari String CSV          : {user_csv}")
    print(f"   Usia (tahun 2026)         : {user_csv.hitung_usia()} tahun\n")

    # 3. Alternative Constructor dari Payload Dictionary (API JSON)
    payload_json = {
        "user_id": "dewi_lestari",
        "email_address": "dewi@kreatif.id",
        "birth_year": 1992
    }
    user_api = Pengguna.dari_payload_api(payload_json)
    print(f"3. Dari Dictionary API      : {user_api}")
    print(f"   Usia (tahun 2026)         : {user_api.hitung_usia()} tahun\n")

    # 4. Alternative Constructor dari UNIX Timestamp
    # Contoh timestamp: 788918400 (Sekitar 1 Januari 1995)
    user_timestamp = Pengguna.dari_timestamp_lahir("eko_prasetyo", "eko@cloud.io", 788918400)
    print(f"4. Dari UNIX Timestamp      : {user_timestamp}")
    print(f"   Tahun Lahir Terhitung     : {user_timestamp.tahun_lahir}\n")

    # ==========================================================================
    # PEMBUKTIAN KRUSIAL: Mengapa kita memakai 'cls' dan BUKAN 'Pengguna'?
    # ==========================================================================
    print("=" * 65)
    print("[PEMBUKTIAN] Pewarisan (Inheritance) & Pola 'cls'")
    print("=" * 65)

    admin_csv = "super_admin, admin@root.org, 1988"
    # Kita memanggil method dari class Administrator!
    admin_objek = Administrator.dari_string_csv(admin_csv)

    print(f"Objek yang dihasilkan: {admin_objek}")
    print(f"Tipe objek sebenarnya: {type(admin_objek)}")
    print(f"Apakah benar objek bertipe Administrator? {isinstance(admin_objek, Administrator)}")

    # Karena 'cls' merujuk ke Administrator, method milik Administrator langsung ada!
    admin_objek.aksi_hapus_database()

    print("\n" + "=" * 65)
    print("[OK] Selesai: Alternative constructor berhasil dipahami dan dibuktikan.")
    print("=" * 65)
