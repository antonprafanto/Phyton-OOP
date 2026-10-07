"""
================================================================================
MODUL 9: CUSTOM EXCEPTION & ERROR HANDLING BERBASIS OBJEK
Berkas 04: Solusi Resmi & Pembahasan Tantangan PayVibe
================================================================================
STUDI KASUS: SISTEM TRANSAKSI E-WALLET "PAYVIBE"
================================================================================
"""

import sys

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass


# ==============================================================================
# 1. HIERARKI EXCEPTION DOMPET DIGITAL
# ==============================================================================
class PayVibeError(Exception):
    """Root error untuk semua permasalahan dalam aplikasi PayVibe."""
    def __init__(self, pesan: str, kode_error: str = "ERR_PAYVIBE_GENERAL"):
        super().__init__(pesan)
        self.kode_error = kode_error


class AkunNonaktifError(PayVibeError):
    """Dilempar ketika dompet digital berstatus tidak aktif atau dinonaktifkan sistem."""
    def __init__(self, nomor_hp: str):
        self.nomor_hp = nomor_hp
        pesan = f"Akses transaksi ditolak! Akun [{nomor_hp}] sedang dalam status nonaktif/dibekukan."
        super().__init__(pesan, kode_error="ERR_PAYVIBE_INACTIVE_ACCOUNT")


class SaldoTidakCukupError(PayVibeError):
    """Dilempar ketika saldo pengguna lebih kecil daripada nominal penarikan."""
    def __init__(self, saldo_saat_ini: int, nominal_diminta: int):
        self.saldo_saat_ini = saldo_saat_ini
        self.nominal_diminta = nominal_diminta
        self.kekurangan = nominal_diminta - saldo_saat_ini
        pesan = (
            f"Penarikan gagal! Saldo Anda saat ini Rp {saldo_saat_ini:,}, "
            f"meminta Rp {nominal_diminta:,} (Kekurangan: Rp {self.kekurangan:,})."
        )
        super().__init__(pesan, kode_error="ERR_PAYVIBE_INSUFFICIENT_BALANCE")


class BatasHarianTerlampauiError(PayVibeError):
    """Dilempar ketika akumulasi penarikan dalam sehari melewati batas plafon."""
    def __init__(self, limit_maksimal: int, total_terpakai: int, nominal_diminta: int):
        self.limit_maksimal = limit_maksimal
        self.total_terpakai = total_terpakai
        self.nominal_diminta = nominal_diminta
        self.sisa_kuota = max(0, limit_maksimal - total_terpakai)
        pesan = (
            f"Transaksi melebihi limit harian! Batas maksimal harian: Rp {limit_maksimal:,}. "
            f"Total terpakai hari ini: Rp {total_terpakai:,}. "
            f"Sisa kuota penarikan Anda: Rp {self.sisa_kuota:,}."
        )
        super().__init__(pesan, kode_error="ERR_PAYVIBE_DAILY_LIMIT_EXCEEDED")


# ==============================================================================
# 2. CLASS DOMPET DIGITAL
# ==============================================================================
class DompetDigital:
    def __init__(self, nomor_hp: str, saldo: int, limit_harian: int = 5_000_000):
        self.nomor_hp = nomor_hp
        self.saldo = saldo
        self.limit_harian = limit_harian
        self.total_penarikan_hari_ini = 0
        self.is_aktif = True

    def tarik_saldo(self, nominal: int) -> int:
        """
        Menarik saldo dengan 4 lapis validasi OOP.
        Mengembalikan sisa saldo terkini jika berhasil.
        """
        print(f"\n[REQUEST] Menarik saldo Rp {nominal:,} dari akun {self.nomor_hp}...")

        # Validasi 1: Validitas Angka Nominal
        if not isinstance(nominal, (int, float)) or nominal <= 0:
            raise ValueError(f"Nominal penarikan harus berupa angka positif! Diterima: {nominal}")

        # Validasi 2: Status Akun
        if not self.is_aktif:
            raise AkunNonaktifError(self.nomor_hp)

        # Validasi 3: Limit Harian
        if (self.total_penarikan_hari_ini + nominal) > self.limit_harian:
            raise BatasHarianTerlampauiError(
                limit_maksimal=self.limit_harian,
                total_terpakai=self.total_penarikan_hari_ini,
                nominal_diminta=nominal
            )

        # Validasi 4: Kecukupan Saldo
        if nominal > self.saldo:
            raise SaldoTidakCukupError(
                saldo_saat_ini=self.saldo,
                nominal_diminta=nominal
            )

        # Seluruh validasi lolos:
        self.saldo -= nominal
        self.total_penarikan_hari_ini += nominal
        print(f"[BERHASIL] Penarikan Rp {nominal:,} sukses!")
        print(f"  -> Sisa Saldo: Rp {self.saldo:,}")
        print(f"  -> Total Penarikan Hari Ini: Rp {self.total_penarikan_hari_ini:,} (Limit: Rp {self.limit_harian:,})")
        return self.saldo


# ==============================================================================
# 3. PENGUJIAN SKENARIO LENGKAP
# ==============================================================================
if __name__ == "__main__":
    print("=" * 65)
    print("[SOLUSI] PENGUJIAN LENGKAP DOMPET DIGITAL PAYVIBE")
    print("=" * 65)

    akun_anton = DompetDigital(nomor_hp="0812-9876-5432", saldo=2_500_000, limit_harian=3_000_000)

    # SKENARIO 1: Penarikan Sukses Pertama
    try:
        akun_anton.tarik_saldo(1_000_000)
    except PayVibeError as e:
        print(f"[ERROR] {e}")

    # SKENARIO 2: Penarikan Melebihi Saldo
    try:
        akun_anton.tarik_saldo(2_000_000)  # Saldo sisa 1.500.000
    except SaldoTidakCukupError as err:
        print(f"[DITOLAK] ⚠️ {err}")
        print(f"Kode Error   : {err.kode_error}")
        print(f"Solusi User  : Harap isi ulang saldo sebesar minimal Rp {err.kekurangan:,}")

    # SKENARIO 3: Penarikan Melebihi Limit Harian
    # Saldo saat ini 1.500.000, limit tersisa hanya 2.000.000 (dari 3.000.000).
    # Mari kita ubah limit_harian akun menjadi 1.200.000 untuk memicu limit sebelum saldo habis:
    akun_anton.limit_harian = 1_200_000
    try:
        akun_anton.tarik_saldo(500_000)  # Total hari ini sudah 1.000.000, +500.000 = 1.500.000 > limit 1.200.000
    except BatasHarianTerlampauiError as err:
        print(f"[DITOLAK] ⚠️ {err}")
        print(f"Kode Error   : {err.kode_error}")
        print(f"Maksimal yang bisa ditarik hari ini: Rp {err.sisa_kuota:,}")

    # SKENARIO 4: Akun Dinonaktifkan
    akun_anton.is_aktif = False
    try:
        akun_anton.tarik_saldo(50_000)
    except AkunNonaktifError as err:
        print(f"[DITOLAK] ⛔ {err}")
        print(f"Aksi CS      : Mengirim SMS verifikasi aktivasi ke {err.nomor_hp}...")

    # SKENARIO 5: Input Nominal Negatif
    try:
        akun_anton.tarik_saldo(-100_000)
    except ValueError as val_err:
        print(f"[INPUT INVALID] ❌ {val_err}")

    print("\n" + "=" * 65)
    print("[OK] Selesai: Seluruh skenario penanganan error teruji 100%.")
    print("=" * 65)
