# ==============================================================================
# MODUL 13: DESIGN PATTERNS - BAGIAN 1: SINGLETON PATTERN
# ==============================================================================
# File: 01_singleton_pattern.py
# Deskripsi: Memahami dan mengimplementasikan Singleton Pattern di Python
#            menggunakan dunder method __new__(), lengkap dengan penjagaan init.
# ==============================================================================

import sys

# Konfigurasi terminal agar output UTF-8 berjalan mulus di Windows PowerShell
if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass


# ------------------------------------------------------------------------------
# 1. KASUS SEDERHANA: SINGLETON DENGAN __new__()
# ------------------------------------------------------------------------------
print("=" * 70)
print("1. PEMBUKTIAN OBJEK TUNGGAL (SINGLETON PATTERN)")
print("=" * 70)

class KonfigurasiAplikasi:
    """
    Kelas Singleton untuk menyimpan pengaturan global aplikasi.
    Di mana pun dipanggil, ia selalu mengembalikan objek yang sama.
    """
    _instance = None  # Variabel class untuk menyimpan objek tunggal

    def __new__(cls, *args, **kwargs):
        # __new__ bertugas mengalokasikan memori fisik objek
        if cls._instance is None:
            print("[System] Membuat objek KonfigurasiAplikasi pertama kali di RAM...")
            cls._instance = super().__new__(cls)
            # Inisialisasi default hanya sekali
            cls._instance.nama_aplikasi = "Sistem Retail POS Super"
            cls._instance.versi = "1.0.0"
            cls._instance.mode_debug = False
        else:
            print("[System] Objek sudah ada di RAM! Mengembalikan objek yang lama...")
        return cls._instance


# Mari kita uji pembuatan 2 variabel konfigurasi
cfg1 = KonfigurasiAplikasi()
cfg2 = KonfigurasiAplikasi()

print("\n--- Uji Identitas Objek ---")
print(f"ID Memori cfg1 : {id(cfg1)}")
print(f"ID Memori cfg2 : {id(cfg2)}")
print(f"Apakah cfg1 is cfg2? {cfg1 is cfg2}")

# Buktikan bahwa mengubah di cfg1 langsung berdampak pada cfg2
print("\n--- Uji Sinkronisasi Data Antar Referensi ---")
print(f"Nilai mode_debug di cfg2 awal: {cfg2.mode_debug}")
print("-> Mengubah cfg1.mode_debug menjadi True...")
cfg1.mode_debug = True
print(f"Nilai mode_debug di cfg2 sekarang: {cfg2.mode_debug}")
print(f"Kesimpulan: cfg1 dan cfg2 adalah benda fisik yang PERSIS SAMA.")


# ------------------------------------------------------------------------------
# 2. JEBAKAN KHUSUS PYTHON: PENJAGAAN __init__() DI SINGLETON
# ------------------------------------------------------------------------------
print("\n" + "=" * 70)
print("2. JEBAKAN PEMULA: MENJAGA __init__() AGAR TIDAK TERPANGGIL BERULANG")
print("=" * 70)

class DatabaseConnectionPool:
    """
    Singleton Database Pool yang aman dari reset inisialisasi ulang.
    
    Catatan Arsitektur:
    Di Python, jika __new__ mengembalikan instance dari class yang sama,
    Python akan SECARA OTOMATIS memanggil __init__ setiap kali kita mengetik
    DatabaseConnectionPool(). Tanpa flag penjaga (_terinisialisasi),
    koneksi akan di-reset setiap kali instansiasi dipanggil!
    """
    _instance = None
    _terinisialisasi = False

    def __new__(cls, host: str = "localhost", port: int = 5432):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, host: str = "localhost", port: int = 5432):
        # Penjaga agar __init__ hanya jalan SATU KALI sepanjang usia aplikasi
        if not self._terinisialisasi:
            self.host = host
            self.port = port
            self.koneksi_aktif = 10
            self.riwayat_query = []
            DatabaseConnectionPool._terinisialisasi = True
            print(f"[DB Pool] Terbuka koneksi pool ke {self.host}:{self.port} (10 slots)")

    def eksekusi_query(self, query: str):
        self.riwayat_query.append(query)
        print(f"[DB Query] Menjalankan: '{query}' (Total riwayat: {len(self.riwayat_query)})")


# Simulasi: Modul Otentikasi membuka DB
print("\n--- Modul Auth Meminta Koneksi DB ---")
db_auth = DatabaseConnectionPool("192.168.1.100", 5432)
db_auth.eksekusi_query("SELECT * FROM users WHERE username='budi'")

# Simulasi: Modul Transaksi membuka DB di tempat lain
print("\n--- Modul Transaksi Meminta Koneksi DB (Parameter Berbeda diabaikan) ---")
db_transaksi = DatabaseConnectionPool("localhost", 3306)
db_transaksi.eksekusi_query("INSERT INTO orders (id, total) VALUES (101, 50000)")

print("\n--- Bukti Riwayat Query Terpusat Pada Satu Database Pool ---")
print(f"Riwayat DB di referensi Auth     : {db_auth.riwayat_query}")
print(f"Riwayat DB di referensi Transaksi: {db_transaksi.riwayat_query}")
print(f"Host pool tetap                  : {db_transaksi.host}:{db_transaksi.port}")
print(f"Apakah db_auth is db_transaksi?  : {db_auth is db_transaksi}")

print("\n" + "=" * 70)
print("SELESAI: Singleton menjamin efisiensi memori dan konsistensi data!")
print("=" * 70)
