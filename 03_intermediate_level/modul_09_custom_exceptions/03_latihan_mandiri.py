"""
================================================================================
MODUL 9: CUSTOM EXCEPTION & ERROR HANDLING BERBASIS OBJEK
Berkas 03: Lembar Latihan Mandiri (Tantangan Sistem Dompet Digital PayVibe)
================================================================================
STUDI KASUS: SISTEM TRANSAKSI E-WALLET "PAYVIBE"

Deskripsi Tugas:
Anda diminta membangun sistem proteksi penarikan saldo e-wallet. Aplikasi tidak
boleh melempar 'Exception' umum saat terjadi masalah, melainkan harus melempar
Custom Exception yang tepat dengan metadata yang lengkap.

Struktur Hierarki Error yang Harus Dibuat:
1. `PayVibeError(Exception)`:
   - Root error aplikasi PayVibe.
   - Menerima `pesan: str` dan `kode_error: str`.
2. `AkunNonaktifError(PayVibeError)`:
   - Dilempar jika dompet digital dalam kondisi nonaktif/terblokir.
   - Menyimpan atribut: `nomor_hp`.
3. `SaldoTidakCukupError(PayVibeError)`:
   - Dilempar jika saldo kurang dari nominal yang ditarik.
   - Menyimpan atribut: `saldo_saat_ini`, `nominal_diminta`, `kekurangan`.
4. `BatasHarianTerlampauiError(PayVibeError)`:
   - Dilempar jika total penarikan hari ini melebihi limit harian.
   - Menyimpan atribut: `limit_maksimal`, `total_terpakai`, `sisa_kuota`.

Spesifikasi Class `DompetDigital`:
- Constructor: `__init__(self, nomor_hp: str, saldo: int, limit_harian: int = 5_000_000)`
  - Memiliki atribut `is_aktif = True` dan `total_penarikan_hari_ini = 0`.
- Method: `tarik_saldo(self, nominal: int) -> int`
  - Validasi 1: `nominal` harus > 0 (jika tidak, lempar ValueError).
  - Validasi 2: `self.is_aktif` harus True (jika False, lempar AkunNonaktifError).
  - Validasi 3: `self.total_penarikan_hari_ini + nominal <= self.limit_harian`
    (jika melebihi, lempar BatasHarianTerlampauiError).
  - Validasi 4: `nominal <= self.saldo`
    (jika saldo kurang, lempar SaldoTidakCukupError).
  - Jika lolos: kurangi saldo, tambahkan total_penarikan_hari_ini, dan kembalikan sisa saldo.

================================================================================
PETUNJUK:
Lengkapi blok kode dengan tanda [TODO] di bawah ini.
Setelah selesai, jalankan file ini. Jika output sesuai harapan, bandingkan
jawaban Anda dengan '04_solusi_latihan.py'.
================================================================================
"""

import sys

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass


# ==============================================================================
# HIERARKI EXCEPTION
# ==============================================================================
# [TODO 1]: Buat class PayVibeError yang mewarisi Exception
class PayVibeError(Exception):
    pass


# [TODO 2]: Buat class AkunNonaktifError yang mewarisi PayVibeError
class AkunNonaktifError(PayVibeError):
    pass


# [TODO 3]: Buat class SaldoTidakCukupError yang mewarisi PayVibeError
class SaldoTidakCukupError(PayVibeError):
    pass


# [TODO 4]: Buat class BatasHarianTerlampauiError yang mewarisi PayVibeError
class BatasHarianTerlampauiError(PayVibeError):
    pass


# ==============================================================================
# CLASS UTAMA: DOMPET DIGITAL
# ==============================================================================
class DompetDigital:
    def __init__(self, nomor_hp: str, saldo: int, limit_harian: int = 5_000_000):
        # [TODO 5]: Inisialisasi atribut objek
        pass

    def tarik_saldo(self, nominal: int) -> int:
        # [TODO 6]: Implementasikan 4 tahapan validasi dan lempar exception yang sesuai
        pass


# ==============================================================================
# AREA PENGUJIAN OTOMATIS
# ==============================================================================
if __name__ == "__main__":
    print("=" * 65)
    print("[UJI COBA] TANTANGAN DOMPET DIGITAL PAYVIBE")
    print("=" * 65)

    print("\nSilakan lengkapi kode di atas, lalu aktifkan kode pengujian di bawah ini:\n")

    # dompet = DompetDigital("08123456789", saldo=1_000_000, limit_harian=2_000_000)

    # 1. Uji Tarik Normal (Berhasil)
    # dompet.tarik_saldo(300_000)

    # 2. Uji Saldo Kurang
    # try:
    #     dompet.tarik_saldo(800_000)
    # except SaldoTidakCukupError as e:
    #     print(f"Tertangkap SaldoTidakCukupError: {e}")

    # 3. Uji Limit Harian
    # try:
    #     dompet.tarik_saldo(1_900_000)
    # except BatasHarianTerlampauiError as e:
    #     print(f"Tertangkap BatasHarianTerlampauiError: {e}")
