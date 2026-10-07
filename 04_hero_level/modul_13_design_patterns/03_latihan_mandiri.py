# ==============================================================================
# MODUL 13: DESIGN PATTERNS - LATIHAN MANDIRI
# ==============================================================================
# File: 03_latihan_mandiri.py
# Deskripsi: Lembar kerja latihan penerapan Singleton, Factory Method,
#            dan Strategy Pattern dalam arsitektur sistem e-commerce.
#
# PETUNJUK:
# 1. Baca skenario dan panduan arsitektur pada setiap bagian [TODO].
# 2. Lengkapi kode di bagian yang ditandai dengan [TODO 1], [TODO 2], dan [TODO 3].
# 3. Jalankan file ini menggunakan terminal:
#    python 04_hero_level/modul_13_design_patterns/03_latihan_mandiri.py
# 4. Pastikan seluruh blok pengujian mandiri di bagian bawah lolos (Passed)!
# ==============================================================================

import sys
from abc import ABC, abstractmethod
from typing import Dict, List, Type

# Konfigurasi terminal agar output UTF-8 berjalan mulus di Windows PowerShell
if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass


# ==============================================================================
# TANTANGAN 1: SINGLETON PATTERN - AUDIT LOG MANAGER
# ==============================================================================
# Kebutuhan:
# Sistem membutuhkan pencatat log transaksi terpusat `AuditLogManager`.
# Syarat:
# 1. Gunakan __new__(cls) agar hanya ada SATU instance di seluruh memori.
# 2. Tambahkan flag _terinisialisasi agar __init__ tidak mereset list log saat
#    dipanggil berulang kali.
# 3. Method: catat_log(pesan: str) -> menambahkan pesan bertanggal/berurutan ke self.log_list
# 4. Method: ambil_semua_log() -> List[str]

class AuditLogManager:
    _instance = None
    _terinisialisasi = False

    def __new__(cls):
        # [TODO 1A]: Implementasikan logika __new__ untuk Singleton
        raise NotImplementedError("TODO 1A: Lengkapi implementasi __new__ untuk Singleton")

    def __init__(self):
        # [TODO 1B]: Cegah inisialisasi ulang menggunakan self._terinisialisasi
        if not self._terinisialisasi:
            self.log_list: List[str] = []
            AuditLogManager._terinisialisasi = True

    def catat_log(self, pesan: str):
        # [TODO 1C]: Tambahkan pesan ke self.log_list
        raise NotImplementedError("TODO 1C: Lengkapi penambahan pesan ke log_list")

    def ambil_semua_log(self) -> List[str]:
        return self.log_list


# ==============================================================================
# TANTANGAN 2: STRATEGY PATTERN - STRATEGI DISKON FLEKSIBEL
# ==============================================================================
# Kebutuhan:
# Kasir e-commerce dapat menerapkan promo diskon yang berbeda-beda.
# Buatlah interface StrategiDiskon dan 2 implementasi konkret:
# 1. DiskonPersentase(persen: float):
#    Contoh: persen=10.0 -> diskon 10% dari total_belanja.
# 2. DiskonNominal(potongan_rupiah: int):
#    Contoh: potongan=25000 -> memotong langsung Rp 25.000.
#    (Catatan: potongan tidak boleh melebihi total belanja).

class StrategiDiskon(ABC):
    @abstractmethod
    def hitung_diskon(self, total_belanja: int) -> int:
        """Mengembalikan nilai potongan harga dalam Rupiah (integer)."""
        pass


class DiskonPersentase(StrategiDiskon):
    def __init__(self, persen: float):
        self.persen = persen

    def hitung_diskon(self, total_belanja: int) -> int:
        # [TODO 2A]: Hitung nilai diskon persen (dibulatkan ke integer)
        raise NotImplementedError("TODO 2A: Lengkapi perhitungan DiskonPersentase")


class DiskonNominal(StrategiDiskon):
    def __init__(self, potongan_rupiah: int):
        self.potongan_rupiah = potongan_rupiah

    def hitung_diskon(self, total_belanja: int) -> int:
        # [TODO 2B]: Potong sesuai nominal flat (maksimal sebesar total_belanja)
        raise NotImplementedError("TODO 2B: Lengkapi perhitungan DiskonNominal")


class TransaksiBelanja:
    """Context yang menggunakan StrategiDiskon."""
    def __init__(self, id_transaksi: str, total_belanja: int, strategi_diskon: StrategiDiskon):
        self.id_transaksi = id_transaksi
        self.total_belanja = total_belanja
        self.strategi_diskon = strategi_diskon

    def set_strategi_diskon(self, strategi_baru: StrategiDiskon):
        self.strategi_diskon = strategi_baru

    def hitung_total_akhir(self) -> int:
        potongan = self.strategi_diskon.hitung_diskon(self.total_belanja)
        return max(0, self.total_belanja - potongan)


# ==============================================================================
# TANTANGAN 3: FACTORY METHOD PATTERN - METODE PEMBAYARAN GATEWAY
# ==============================================================================
# Kebutuhan:
# Saat checkout, user memilih jenis pembayaran. Kita ingin memisahkan proses
# instansiasi kelas pembayaran menggunakan Factory Method dengan Registry Dict.
#
# Buat Interface MetodePembayaran:
# - proses_bayar(nominal: int) -> str
# Kelas Konkret:
# 1. BayarTransferBank: mengembalikan f"[TRANSFER BANK] Sukses bayar Rp {nominal:,}"
# 2. BayarEWallet: mengembalikan f"[E-WALLET] Sukses bayar Rp {nominal:,}"
# 3. BayarKartuKredit: mengembalikan f"[KARTU KREDIT] Sukses bayar Rp {nominal:,}"
#
# Kelas PembayaranFactory:
# - _registry: Dict[str, Type[MetodePembayaran]]
# - daftarkan(kunci: str, cls: Type[MetodePembayaran])
# - buat_pembayaran(kunci: str) -> MetodePembayaran

class MetodePembayaran(ABC):
    @abstractmethod
    def proses_bayar(self, nominal: int) -> str:
        pass


class BayarTransferBank(MetodePembayaran):
    def proses_bayar(self, nominal: int) -> str:
        return f"[TRANSFER BANK] Sukses bayar Rp {nominal:,}"


class BayarEWallet(MetodePembayaran):
    def proses_bayar(self, nominal: int) -> str:
        return f"[E-WALLET] Sukses bayar Rp {nominal:,}"


class BayarKartuKredit(MetodePembayaran):
    def proses_bayar(self, nominal: int) -> str:
        return f"[KARTU KREDIT] Sukses bayar Rp {nominal:,}"


class PembayaranFactory:
    _registry: Dict[str, Type[MetodePembayaran]] = {}

    @classmethod
    def daftarkan(cls, kunci: str, kelas_pembayaran: Type[MetodePembayaran]):
        cls._registry[kunci.lower()] = kelas_pembayaran

    @classmethod
    def buat_pembayaran(cls, tipe: str) -> MetodePembayaran:
        # [TODO 3]: Ambil class dari cls._registry berdasarkan tipe (case-insensitive)
        # Jika tipe tidak ditemukan, lemparkan ValueError dengan pesan deskriptif.
        # Kembalikan instance dari class yang ditemukan.
        raise NotImplementedError("TODO 3: Lengkapi implementasi buat_pembayaran")


# Pendaftaran default
PembayaranFactory.daftarkan("bank", BayarTransferBank)
PembayaranFactory.daftarkan("ewallet", BayarEWallet)
PembayaranFactory.daftarkan("cc", BayarKartuKredit)


# ==============================================================================
# BLOK PENGUJIAN OTOMATIS (JANGAN UBAH DI BAWAH INI)
# ==============================================================================
def jalankan_pengujian():
    print("=" * 70)
    print("MENJALANKAN VERIFIKASI LATIHAN DESIGN PATTERNS")
    print("=" * 70)

    try:
        # 1. Uji Singleton
        print("-> Menguji Singleton AuditLogManager...")
        logger1 = AuditLogManager()
        logger2 = AuditLogManager()
        assert logger1 is logger2, "GAGAL: logger1 dan logger2 harus merupakan objek yang sama di RAM!"
        
        logger1.catat_log("User login: anton")
        logger2.catat_log("User checkout TRX-01")
        logs = logger1.ambil_semua_log()
        assert len(logs) == 2, f"GAGAL: Seharusnya ada 2 log, ditemukan {len(logs)}"
        print("  [OK] Singleton terbukti identik dan sinkron.")

        # 2. Uji Strategy
        print("\n-> Menguji Strategy Pattern Diskon...")
        trx = TransaksiBelanja("TRX-101", 100000, DiskonPersentase(15.0))
        assert trx.hitung_total_akhir() == 85000, f"GAGAL: 100k diskon 15% harus 85000, dapat {trx.hitung_total_akhir()}"
        
        # Ganti strategi saat runtime
        trx.set_strategi_diskon(DiskonNominal(30000))
        assert trx.hitung_total_akhir() == 70000, f"GAGAL: 100k diskon flat 30k harus 70000, dapat {trx.hitung_total_akhir()}"
        print("  [OK] Strategy Pattern bekerja fleksibel saat runtime.")

        # 3. Uji Factory Method
        print("\n-> Menguji Factory Method Pembayaran...")
        bayar_ewallet = PembayaranFactory.buat_pembayaran("ewallet")
        assert isinstance(bayar_ewallet, BayarEWallet), "GAGAL: Factory harus menghasilkan instance BayarEWallet"
        hasil_teks = bayar_ewallet.proses_bayar(50000)
        assert "[E-WALLET]" in hasil_teks, "GAGAL: Output pesan pembayaran tidak sesuai"

        # Uji validasi input tak dikenal
        sukses_error = False
        try:
            PembayaranFactory.buat_pembayaran("crypto")
        except ValueError:
            sukses_error = True
        assert sukses_error, "GAGAL: Factory harus melempar ValueError jika tipe pembayaran tidak terdaftar"
        print("  [OK] Factory Method sukses memproduksi objek sesuai konfigurasi.")

        print("\n" + "=" * 70)
        print("SELAMAT! SELURUH TANTANGAN DESIGN PATTERNS BERHASIL DISELESAIKAN!")
        print("=" * 70)

    except NotImplementedError as e:
        print(f"\n[BELUM SELESAI] Silakan lengkapi TODO: {e}")
    except AssertionError as e:
        print(f"\n[ASSERTION ERROR] {e}")


if __name__ == "__main__":
    jalankan_pengujian()
