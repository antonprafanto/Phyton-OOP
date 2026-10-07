"""
01_dasar_abstraction.py
=======================
Modul 6: Pilar 4 – Abstraction (Menyembunyikan Kerumitan dengan abc)

File ini mendemonstrasikan:
1. Pembuatan Abstract Base Class (ABC) dan decorator @abstractmethod
2. Pembuatan Concrete Class (Kelas Konkret) yang mematuhi kontrak
3. Simulasi penolakan Python (TypeError) saat kontrak dilanggar
"""
import sys
from abc import ABC, abstractmethod

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

print("=" * 60)
print("[DEMO] ABSTRACTION & KONTRAK KERJA BAKU DENGAN MODUL ABC")
print("=" * 60)

# ==============================================================
# 1. KELAS ABSTRAK (SURAT KONTRAK KERJA INDUK)
# ==============================================================
class DriverDatabase(ABC):
    """
    Kelas Abstrak: Tidak boleh dilahirkan sebagai objek.
    Berfungsi sebagai standar kontrak wajib bagi seluruh driver database.
    """
    @abstractmethod
    def konek(self):
        """Wajib diimplementasikan oleh setiap anak!"""
        pass

    @abstractmethod
    def eksekusi_query(self, query: str):
        """Wajib diimplementasikan oleh setiap anak!"""
        pass

    @abstractmethod
    def putus_koneksi(self):
        """Wajib diimplementasikan oleh setiap anak!"""
        pass


# ==============================================================
# 2. CONCRETE CLASS 1: MYSQL (PATUH 100% PADA KONTRAK)
# ==============================================================
class MySQLDriver(DriverDatabase):
    def __init__(self, host: str, user: str):
        self.host = host
        self.user = user

    def konek(self):
        print(f"[MySQL] Terhubung ke server {self.host} sebagai '{self.user}' pada port 3306.")

    def eksekusi_query(self, query: str):
        print(f"[MySQL] Menjalankan: '{query}' -> Berhasil!")

    def putus_koneksi(self):
        print("[MySQL] Sesi koneksi ditutup dengan tertib.")


# ==============================================================
# 3. KELAS YANG MELANGGAR KONTRAK (LUPA SATU METHOD)
# ==============================================================
class DriverMalas(DriverDatabase):
    def konek(self):
        print("[Malas] Konek...")

    def eksekusi_query(self, query: str):
        print(f"[Malas] Eksekusi {query}...")

    # LUPA MENULIS: putus_koneksi() !


# --- PENGUJIAN ---
print("\n--- 1. Menjalankan Driver yang Patuh Kontrak (MySQL) ---")
db = MySQLDriver("localhost", "root")
db.konek()
db.eksekusi_query("SELECT * FROM users WHERE status = 'active'")
db.putus_koneksi()

print("\n--- 2. Eksperimen: Mencoba Melahirkan Objek Langsung dari Kelas Abstrak ---")
try:
    objek_abstrak = DriverDatabase()
except TypeError as err:
    print(f"[DITOLAK PYTHON] Pesan Error:\n>>> {err}")
    print("Alasan: Kelas abstrak adalah ide/konsep, tidak boleh ada wujud fisiknya!")

print("\n--- 3. Eksperimen: Mencoba Melahirkan Driver yang Lupa 1 Kontrak ---")
try:
    driver_cacat = DriverMalas()
except TypeError as err:
    print(f"[DITOLAK PYTHON] Pesan Error:\n>>> {err}")
    print("Alasan: Python mendeteksi bahwa DriverMalas lupa menulis method 'putus_koneksi'!")

print("\n" + "=" * 60)
print("[OK] Selesai: Abstraksi berhasil menjamin standardisasi kode tim.")
print("=" * 60)
