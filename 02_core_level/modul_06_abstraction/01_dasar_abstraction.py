"""
01_dasar_abstraction.py
=======================
Modul 6: Pilar 4 – Abstraction (Menyembunyikan Kerumitan dengan abc)

File ini mendemonstrasikan:
1. Pembuatan Abstract Base Class (ABC) dengan decorator @abstractmethod
2. Perpaduan Method Konkret (sudah ada isi) dan Method Abstrak (kontrak wajib)
3. Pembuatan Concrete Class (Kelas Konkret) yang mematuhi kontrak
4. Simulasi penolakan Python (TypeError) saat kontrak dilanggar
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
# 1. KELAS ABSTRAK DENGAN METHOD KONKRET & METHOD ABSTRAK
# ==============================================================
class DriverDatabase(ABC):
    """
    Kelas Abstrak: Tidak boleh dilahirkan sebagai objek.
    Berfungsi sebagai standar kontrak wajib bagi seluruh driver database.
    """
    def __init__(self, nama_driver: str):
        self.nama_driver = nama_driver

    # A. METHOD KONKRET (Fitur bawaan yang siap dipakai semua anak):
    def catat_log(self, pesan: str):
        print(f"[AUDIT LOG {self.nama_driver}]: {pesan}")

    # B. METHOD ABSTRAK (Kontrak wajib yang HARUS diisi setiap anak):
    @abstractmethod
    def konek(self):
        pass

    @abstractmethod
    def eksekusi_query(self, query: str):
        pass

    @abstractmethod
    def putus_koneksi(self):
        pass


# ==============================================================
# 2. CONCRETE CLASS 1: MYSQL (PATUH 100% PADA KONTRAK)
# ==============================================================
class MySQLDriver(DriverDatabase):
    def __init__(self, host: str, user: str):
        super().__init__("MySQL")
        self.host = host
        self.user = user

    def konek(self):
        # Memanfaatkan method konkret warisan orang tua:
        self.catat_log("Membuka sambungan TCP...")
        print(f"[MySQL] Terhubung ke {self.host} sebagai '{self.user}' pada port 3306.")

    def eksekusi_query(self, query: str):
        self.catat_log(f"Menjalankan query: {query}")
        print(f"[MySQL] Hasil dieksekusi: 10 baris data dikembalikan.")

    def putus_koneksi(self):
        self.catat_log("Menutup sesi koneksi.")
        print("[MySQL] Koneksi ditutup dengan aman.")


# ==============================================================
# 3. KELAS YANG MELANGGAR KONTRAK (LUPA SATU METHOD)
# ==============================================================
class DriverMalas(DriverDatabase):
    def __init__(self):
        super().__init__("Malas")

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
    # Catatan: Linter IDE (seperti Pyrefly) secara cerdas mendeteksi bahwa kelas ini abstrak
    # sebelum program dijalankan. Kita gunakan type ignore untuk keperluan demonstrasi runtime:
    kelas_target: type = DriverDatabase
    objek_abstrak = kelas_target("Dummy")  # type: ignore
except TypeError as err:
    print(f"[DITOLAK PYTHON] Pesan Error:\n>>> {err}")
    print("Alasan: Kelas abstrak adalah ide/konsep, tidak boleh ada wujud fisiknya!")

print("\n--- 3. Eksperimen: Mencoba Melahirkan Driver yang Lupa 1 Kontrak ---")
try:
    kelas_cacat: type = DriverMalas
    driver_cacat = kelas_cacat()  # type: ignore
except TypeError as err:
    print(f"[DITOLAK PYTHON] Pesan Error:\n>>> {err}")
    print("Alasan: Python mendeteksi bahwa DriverMalas lupa menulis method 'putus_koneksi'!")

print("\n" + "=" * 60)
print("[OK] Selesai: Abstraksi berhasil menjamin standardisasi kode tim.")
print("=" * 60)
