# ==============================================================================
# MODUL 13: DESIGN PATTERNS - SOLUSI LATIHAN RESMI
# ==============================================================================
# File: 04_solusi_latihan.py
# Deskripsi: Kunci jawaban lengkap dan teruji untuk latihan mandiri Modul 13.
#            Menerapkan Singleton, Strategy, dan Factory Method Pattern
#            dengan standar clean code arsitektur enterprise.
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
class AuditLogManager:
    """
    Singleton Logger terpusat untuk mencatat aktivitas sistem e-commerce.
    Menggunakan __new__ untuk alokasi memori tunggal dan guard flag
    agar __init__ tidak mereset data riwayat log.
    """
    _instance = None
    _terinisialisasi = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._terinisialisasi:
            self.log_list: List[str] = []
            AuditLogManager._terinisialisasi = True

    def catat_log(self, pesan: str):
        self.log_list.append(pesan)

    def ambil_semua_log(self) -> List[str]:
        return list(self.log_list)


# ==============================================================================
# TANTANGAN 2: STRATEGY PATTERN - STRATEGI DISKON FLEKSIBEL
# ==============================================================================
class StrategiDiskon(ABC):
    """Interface umum untuk seluruh formula perhitungan diskon."""
    @abstractmethod
    def hitung_diskon(self, total_belanja: int) -> int:
        pass


class DiskonPersentase(StrategiDiskon):
    """Strategi diskon berbasis persentase (misal: 10% atau 15%)."""
    def __init__(self, persen: float):
        if persen < 0 or persen > 100:
            raise ValueError("Persentase diskon harus berada di antara 0% dan 100%!")
        self.persen = persen

    def hitung_diskon(self, total_belanja: int) -> int:
        return int(total_belanja * (self.persen / 100.0))


class DiskonNominal(StrategiDiskon):
    """Strategi diskon dengan potongan nilai rupiah tetap."""
    def __init__(self, potongan_rupiah: int):
        if potongan_rupiah < 0:
            raise ValueError("Potongan nominal tidak boleh bernilai negatif!")
        self.potongan_rupiah = potongan_rupiah

    def hitung_diskon(self, total_belanja: int) -> int:
        # Potongan maksimal sebesar total belanja (tidak boleh minus)
        return min(self.potongan_rupiah, total_belanja)


class TransaksiBelanja:
    """Context yang membungkus transaksi penjualan dan memegang StrategiDiskon."""
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
class MetodePembayaran(ABC):
    """Interface untuk seluruh saluran gerbang pembayaran."""
    @abstractmethod
    def proses_bayar(self, nominal: int) -> str:
        pass


class BayarTransferBank(MetodePembayaran):
    def proses_bayar(self, nominal: int) -> str:
        return f"[TRANSFER BANK] Sukses bayar Rp {nominal:,} via Virtual Account."


class BayarEWallet(MetodePembayaran):
    def proses_bayar(self, nominal: int) -> str:
        return f"[E-WALLET] Sukses bayar Rp {nominal:,} via QRIS Instant."


class BayarKartuKredit(MetodePembayaran):
    def proses_bayar(self, nominal: int) -> str:
        return f"[KARTU KREDIT] Sukses bayar Rp {nominal:,} via Visa/MasterCard 3D Secure."


class PembayaranFactory:
    """
    Factory berarsitektur Registry Dictionary. Memungkinkan pendaftaran
    metode baru tanpa memodifikasi method pembuatan objek (OCP).
    """
    _registry: Dict[str, Type[MetodePembayaran]] = {}

    @classmethod
    def daftarkan(cls, kunci: str, kelas_pembayaran: Type[MetodePembayaran]):
        cls._registry[kunci.lower()] = kelas_pembayaran

    @classmethod
    def buat_pembayaran(cls, tipe: str) -> MetodePembayaran:
        kunci = tipe.lower()
        kelas_target = cls._registry.get(kunci)
        if not kelas_target:
            opsi_valid = ", ".join(cls._registry.keys())
            raise ValueError(
                f"Metode pembayaran '{tipe}' tidak dikenali! Opsi tersedia: [{opsi_valid}]"
            )
        return kelas_target()


# Daftarkan opsi pembayaran ke dalam Factory
PembayaranFactory.daftarkan("bank", BayarTransferBank)
PembayaranFactory.daftarkan("ewallet", BayarEWallet)
PembayaranFactory.daftarkan("cc", BayarKartuKredit)


# ==============================================================================
# INTEGRASI PENUH & PENGUJIAN OTOMATIS
# ==============================================================================
def jalankan_verifikasi():
    print("=" * 70)
    print("MENJALANKAN VERIFIKASI SOLUSI LATIHAN (MODUL 13)")
    print("=" * 70)

    # 1. Verifikasi Singleton
    print("-> 1. Verifikasi Singleton AuditLogManager...")
    logger_a = AuditLogManager()
    logger_b = AuditLogManager()
    assert logger_a is logger_b, "Logger A dan B harus merupakan objek fisik yang identik di RAM!"
    
    logger_a.catat_log("User 'anton' memulai checkout.")
    logger_b.catat_log("Transaksi TRX-2024 dibuat.")
    
    logs = logger_a.ambil_semua_log()
    assert len(logs) == 2, f"Total log harus 2, didapatkan {len(logs)}"
    print(f"  [OK] Singleton sukses! Total catatan log: {len(logs)}")

    # 2. Verifikasi Strategy
    print("\n-> 2. Verifikasi Strategy Pattern Diskon...")
    trx = TransaksiBelanja("TRX-2024", 200000, DiskonPersentase(20.0))
    total_bayar_persen = trx.hitung_total_akhir()
    assert total_bayar_persen == 160000, f"Harus 160.000, didapat {total_bayar_persen}"
    print(f"  [OK] Diskon Persentase 20% dari 200k = Rp {total_bayar_persen:,}")

    # Tukar strategi saat runtime
    trx.set_strategi_diskon(DiskonNominal(50000))
    total_bayar_nominal = trx.hitung_total_akhir()
    assert total_bayar_nominal == 150000, f"Harus 150.000, didapat {total_bayar_nominal}"
    print(f"  [OK] Diskon Nominal 50k dari 200k = Rp {total_bayar_nominal:,}")

    # 3. Verifikasi Factory Method
    print("\n-> 3. Verifikasi Factory Method Pembayaran...")
    metode_qris = PembayaranFactory.buat_pembayaran("ewallet")
    assert isinstance(metode_qris, BayarEWallet)
    pesan_qris = metode_qris.proses_bayar(total_bayar_nominal)
    print(f"  [OK] Hasil proses pembayaran: {pesan_qris}")

    metode_bank = PembayaranFactory.buat_pembayaran("bank")
    assert isinstance(metode_bank, BayarTransferBank)
    pesan_bank = metode_bank.proses_bayar(total_bayar_nominal)
    print(f"  [OK] Hasil proses pembayaran: {pesan_bank}")

    # Catat ke singleton logger
    logger_a.catat_log(f"Pembayaran berhasil diproses: {pesan_qris}")
    assert len(logger_b.ambil_semua_log()) == 3

    print("\n" + "=" * 70)
    print("STATUS: SELURUH PENGUJIAN SOLUSI MODUL 13 100% SUKSES DAN LOLOS!")
    print("=" * 70)


if __name__ == "__main__":
    jalankan_verifikasi()
