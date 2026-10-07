"""
================================================================================
MODUL 9: CUSTOM EXCEPTION & ERROR HANDLING BERBASIS OBJEK
Berkas 02: Membangun Pohon Hierarki Error & Multi-Catching Berbasis Objek
================================================================================
Tujuan Pembelajaran:
1. Membangun struktur hierarki exception bertingkat (Base Error -> Kategori Error -> Spesifik Error).
2. Membuktikan kekuatan polimorfisme saat menangkap error:
   - Menangkap error spesifik untuk penanganan presisi.
   - Menangkap error kategori untuk penanganan kelompok.
   - Menangkap error root aplikasi untuk fallback umum.
3. Mengonversi objek exception menjadi format dictionary/JSON untuk keperluan logging server.
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


# ==============================================================================
# 1. POHON HIERARKI EXCEPTION PERBANKAN MODERN
# ==============================================================================
class BankCoreError(Exception):
    """
    Root Exception untuk seluruh error yang terjadi pada sistem Bank.
    Semua sub-error otomatis mewarisi kode_error dan timestamp.
    """
    def __init__(self, pesan: str, kode_error: str = "ERR_BANK_GENERAL"):
        super().__init__(pesan)
        self.kode_error = kode_error
        self.waktu_kejadian = datetime.now()

    def to_log_entry(self) -> dict:
        """Mengubah objek error menjadi format dictionary siap-kirim ke sistem log server."""
        return {
            "error_type": self.__class__.__name__,
            "kode_error": self.kode_error,
            "pesan": str(self),
            "timestamp": self.waktu_kejadian.strftime("%Y-%m-%d %H:%M:%S")
        }


# --- Kategori 1: Error Keamanan / Otentikasi ---
class OtentikasiError(BankCoreError):
    """Kategori error yang berhubungan dengan PIN, Password, dan Akses."""
    def __init__(self, pesan: str, kode_error: str = "ERR_AUTH"):
        super().__init__(pesan, kode_error)


class PINSalahError(OtentikasiError):
    """Dilempar saat pengguna salah memasukkan 6 digit PIN ATM."""
    def __init__(self, sisa_percobaan: int):
        self.sisa_percobaan = sisa_percobaan
        pesan = f"PIN yang Anda masukkan salah! Sisa kesempatan mencoba: {sisa_percobaan} kali."
        super().__init__(pesan, kode_error="ERR_AUTH_PIN_INVALID")


class RekeningDibekukanError(OtentikasiError):
    """Dilempar saat nasabah terindikasi transaksi mencurigakan atau salah PIN 3x."""
    def __init__(self, nomor_rekening: str, alasan: str):
        self.nomor_rekening = nomor_rekening
        self.alasan = alasan
        pesan = f"Rekening [{nomor_rekening}] dibekukan demi keamanan. Alasan: {alasan}."
        super().__init__(pesan, kode_error="ERR_AUTH_ACCOUNT_FROZEN")


# --- Kategori 2: Error Finansial / Transaksi ---
class TransaksiFinansialError(BankCoreError):
    """Kategori error yang berhubungan dengan mutasi saldo, limit, dan penarikan."""
    def __init__(self, pesan: str, kode_error: str = "ERR_TRX"):
        super().__init__(pesan, kode_error)


class SaldoTidakCukupError(TransaksiFinansialError):
    """Dilempar saat nominal transaksi melebihi saldo yang tersedia."""
    def __init__(self, saldo_tersedia: int, nominal_tarik: int):
        self.saldo_tersedia = saldo_tersedia
        self.nominal_tarik = nominal_tarik
        self.kekurangan = nominal_tarik - saldo_tersedia
        pesan = (
            f"Saldo tidak cukup! Saldo Anda: Rp {saldo_tersedia:,}, "
            f"Penarikan: Rp {nominal_tarik:,} (Kurang: Rp {self.kekurangan:,})."
        )
        super().__init__(pesan, kode_error="ERR_TRX_INSUFFICIENT_FUNDS")


class BatasLimitHarianError(TransaksiFinansialError):
    """Dilempar saat total transaksi hari ini melewati batas kartu nasabah."""
    def __init__(self, limit_maks: int, total_sekarang: int):
        self.limit_maks = limit_maks
        self.total_sekarang = total_sekarang
        pesan = (
            f"Transaksi ditolak! Total transaksi hari ini (Rp {total_sekarang:,}) "
            f"melebihi batas maksimal harian kartu Anda (Rp {limit_maks:,})."
        )
        super().__init__(pesan, kode_error="ERR_TRX_LIMIT_EXCEEDED")


# ==============================================================================
# 2. SIMULASI ENGINE PERBANKAN
# ==============================================================================
class RekeningNasabah:
    def __init__(self, nomor_rek: str, nama: str, saldo: int, pin: str, limit_harian: int = 10_000_000):
        self.nomor_rek = nomor_rek
        self.nama = nama
        self.saldo = saldo
        self.pin = pin
        self.limit_harian = limit_harian
        self.total_terpakai_hari_ini = 0
        self.salah_pin_count = 0
        self.is_dibekukan = False

    def tarik_tunai(self, nominal: int, input_pin: str):
        print(f"\n[ATM] Memproses penarikan tunai Rp {nominal:,} untuk '{self.nama}'...")

        # 1. Cek status rekening
        if self.is_dibekukan:
            raise RekeningDibekukanError(self.nomor_rek, "Terlalu sering salah PIN atau laporan nasabah")

        # 2. Verifikasi PIN
        if input_pin != self.pin:
            self.salah_pin_count += 1
            sisa = 3 - self.salah_pin_count
            if sisa <= 0:
                self.is_dibekukan = True
                raise RekeningDibekukanError(self.nomor_rek, "Salah PIN 3 kali berturut-turut")
            raise PINSalahError(sisa_percobaan=sisa)

        # PIN benar -> reset counter salah pin
        self.salah_pin_count = 0

        # 3. Cek Limit Harian
        if self.total_terpakai_hari_ini + nominal > self.limit_harian:
            raise BatasLimitHarianError(self.limit_harian, self.total_terpakai_hari_ini + nominal)

        # 4. Cek Saldo
        if nominal > self.saldo:
            raise SaldoTidakCukupError(self.saldo, nominal)

        # Jika lolos semua validasi:
        self.saldo -= nominal
        self.total_terpakai_hari_ini += nominal
        print(f"[BERHASIL] Uang tunai Rp {nominal:,} keluar. Sisa saldo: Rp {self.saldo:,}")


# ==============================================================================
# 3. PENGUJIAN & PENANGANAN POLIMORFISME ERROR
# ==============================================================================
if __name__ == "__main__":
    print("=" * 65)
    print("[DEMO] HIERARKI EXCEPTION & PENANGANAN ERROR MULTI-LEVEL")
    print("=" * 65)

    akun_budi = RekeningNasabah("REK-88123", "Budi Santoso", saldo=500_000, pin="123456", limit_harian=2_000_000)

    # SKENARIO 1: Salah PIN 1x (Tertangkap PINSalahError)
    try:
        akun_budi.tarik_tunai(100_000, input_pin="999999")
    except PINSalahError as err:
        print(f"[UI ATM] ⚠️ {err}")
        print(f"Log Server: {err.to_log_entry()}")

    # SKENARIO 2: Saldo Kurang (Tertangkap SaldoTidakCukupError)
    try:
        akun_budi.tarik_tunai(800_000, input_pin="123456")
    except SaldoTidakCukupError as err:
        print(f"[UI ATM] ⚠️ {err}")
        print(f"Saran Aplikasi: Silakan lakukan Top-Up sebesar minimal Rp {err.kekurangan:,}!")

    # SKENARIO 3: Menangkap lewat Class Kategori (TransaksiFinansialError)
    # Ini membuktikan polimorfisme: cukup 1 block except untuk semua masalah finansial!
    print("\n--- Uji Coba Penangkapan Lewat Kategori 'TransaksiFinansialError' ---")
    try:
        # Menarik 1.500.000 (melebihi saldo)
        akun_budi.tarik_tunai(1_500_000, input_pin="123456")
    except TransaksiFinansialError as trx_err:
        print(f"[KASIR FINANSIAL] Transaksi keuangan terhambat: {trx_err}")
        print(f"Kode Error Sistem: {trx_err.kode_error}")

    # SKENARIO 4: Salah PIN berturut-turut hingga rekening dibekukan
    print("\n--- Uji Coba Blokir Rekening Otomatis ---")
    try:
        akun_budi.tarik_tunai(100_000, input_pin="000000")  # Salah ke-1
    except BankCoreError as e:
        print(f"[NOTIF 1] {e}")

    try:
        akun_budi.tarik_tunai(100_000, input_pin="111111")  # Salah ke-2
    except BankCoreError as e:
        print(f"[NOTIF 2] {e}")

    try:
        akun_budi.tarik_tunai(100_000, input_pin="222222")  # Salah ke-3 -> RekeningDibekukanError!
    except RekeningDibekukanError as e:
        print(f"[NOTIF DARURAT BLOKIR] ⛔ {e}")
        print(f"Audit Log Blokir: {e.to_log_entry()}")
    except BankCoreError as e:
        print(f"[NOTIF UMUM] {e}")

    print("\n" + "=" * 65)
    print("[OK] Selesai: Hierarki error dan penanganan polimorfis berhasil dibuktikan.")
    print("=" * 65)
