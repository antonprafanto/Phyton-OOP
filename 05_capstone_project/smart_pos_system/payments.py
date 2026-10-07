# ==============================================================================
# SMARTPOS SYSTEM - PAYMENT FACTORY & METHODS (MODUL 6 & 13)
# ==============================================================================
# File: payments.py
# Deskripsi: Abstraksi gerbang pembayaran dan Factory Method modern dengan
#            mekanisme Registry Dictionary.
# ==============================================================================

from abc import ABC, abstractmethod
from typing import Dict, Any, Type
from exceptions import PembayaranGagalError


class MetodePembayaran(ABC):
    """Interface gerbang pembayaran yang wajib ditaati seluruh saluran bayar."""
    @abstractmethod
    def proses_bayar(self, total_tagihan: int, **kwargs) -> Dict[str, Any]:
        """
        Memproses transaksi dan mengembalikan kamus detail bukti pelunasan.
        Melenyapkan error PembayaranGagalError jika transaksi bermasalah.
        """
        pass

    @abstractmethod
    def nama_metode(self) -> str:
        """Nama formal metode pembayaran untuk dicetak di struk."""
        pass


class BayarTunai(MetodePembayaran):
    """Pembayaran menggunakan uang fisik / tunai di kasir."""
    def proses_bayar(self, total_tagihan: int, **kwargs) -> Dict[str, Any]:
        uang_diterima = kwargs.get("uang_diterima", 0)
        if uang_diterima < total_tagihan:
            kekurangan = total_tagihan - uang_diterima
            raise PembayaranGagalError(
                f"Uang tunai tidak cukup! Tagihan: Rp {total_tagihan:,}, Diterima: Rp {uang_diterima:,} (Kurang Rp {kekurangan:,})"
            )
        kembalian = uang_diterima - total_tagihan
        return {
            "status": "SUKSES",
            "metode": self.nama_metode(),
            "total_tagihan": total_tagihan,
            "uang_diterima": uang_diterima,
            "kembalian": kembalian,
            "referensi": "CASH-DESK"
        }

    def nama_metode(self) -> str:
        return "Uang Tunai (Cash)"


class BayarQRIS(MetodePembayaran):
    """Pembayaran digital tanpa uang fisik via QRIS Instant Settlement."""
    def proses_bayar(self, total_tagihan: int, **kwargs) -> Dict[str, Any]:
        # Simulasi gateway QRIS
        import random
        ref_id = f"QRIS-{random.randint(100000, 999999)}"
        return {
            "status": "SUKSES",
            "metode": self.nama_metode(),
            "total_tagihan": total_tagihan,
            "uang_diterima": total_tagihan,
            "kembalian": 0,
            "referensi": ref_id
        }

    def nama_metode(self) -> str:
        return "QRIS Digital Payment"


class BayarKartuDebit(MetodePembayaran):
    """Pembayaran melalui mesin EDC Kartu Debit."""
    def proses_bayar(self, total_tagihan: int, **kwargs) -> Dict[str, Any]:
        nomor_kartu = str(kwargs.get("nomor_kartu", "")).strip()
        pin = str(kwargs.get("pin", "")).strip()

        if len(nomor_kartu) < 4:
            raise PembayaranGagalError("Nomor kartu debit tidak valid!")
        if len(pin) != 6 or not pin.isdigit():
            raise PembayaranGagalError("PIN EDC tidak valid! PIN harus 6 digit angka.")

        kartu_sensor = f"****-****-****-{nomor_kartu[-4:]}"
        return {
            "status": "SUKSES",
            "metode": self.nama_metode(),
            "total_tagihan": total_tagihan,
            "uang_diterima": total_tagihan,
            "kembalian": 0,
            "referensi": f"EDC-{kartu_sensor}"
        }

    def nama_metode(self) -> str:
        return "Kartu Debit (EDC)"


class PembayaranFactory:
    """
    Factory pembuat objek pembayaran berbasis dictionary registry.
    Sesuai Open/Closed Principle (OCP).
    """
    _registry: Dict[str, Type[MetodePembayaran]] = {}

    @classmethod
    def daftarkan(cls, kode: str, kelas_metode: Type[MetodePembayaran]):
        cls._registry[kode.lower()] = kelas_metode

    @classmethod
    def buat_metode(cls, kode: str) -> MetodePembayaran:
        kunci = kode.lower()
        kelas_target = cls._registry.get(kunci)
        if not kelas_target:
            opsi = ", ".join(cls._registry.keys())
            raise ValueError(f"Saluran pembayaran '{kode}' tidak dikenal! Opsi: [{opsi}]")
        return kelas_target()


# Daftarkan metode default
PembayaranFactory.daftarkan("tunai", BayarTunai)
PembayaranFactory.daftarkan("qris", BayarQRIS)
PembayaranFactory.daftarkan("debit", BayarKartuDebit)
