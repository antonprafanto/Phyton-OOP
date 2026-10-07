# ==============================================================================
# SMARTPOS SYSTEM - STRATEGY PATTERNS (MODUL 13)
# ==============================================================================
# File: strategies.py
# Deskripsi: Keluarga algoritma perhitungan promo & diskon belanja.
#            Dapat ditukar-pasang secara fleksibel tanpa merusak kode keranjang.
# ==============================================================================

from abc import ABC, abstractmethod


class StrategiDiskon(ABC):
    """Interface dasar untuk seluruh strategi kalkulasi promo."""
    @abstractmethod
    def hitung_diskon(self, total_kotor: int) -> int:
        """Mengembalikan nominal potongan harga dalam Rupiah (integer)."""
        pass

    @abstractmethod
    def deskripsi(self) -> str:
        """Label penjelasan promo untuk dicetak di struk."""
        pass


class TanpaDiskon(StrategiDiskon):
    """Strategi standar ketika pelanggan tidak memiliki voucher/kartu member."""
    def hitung_diskon(self, total_kotor: int) -> int:
        return 0

    def deskripsi(self) -> str:
        return "Non-Promo / Reguler"


class DiskonMember(StrategiDiskon):
    """
    Strategi diskon persentase berdasarkan tingkatan kartu loyalitas member:
    - Gold: 15%
    - Silver: 10%
    - Bronze: 5%
    """
    TIER_RATES = {
        "gold": 0.15,
        "silver": 0.10,
        "bronze": 0.05
    }

    def __init__(self, tier: str = "bronze"):
        kunci = tier.lower()
        if kunci not in self.TIER_RATES:
            raise ValueError(f"Tier member '{tier}' tidak valid! Pilihan: [gold, silver, bronze]")
        self.tier = kunci
        self.rate = self.TIER_RATES[kunci]

    def hitung_diskon(self, total_kotor: int) -> int:
        return int(total_kotor * self.rate)

    def deskripsi(self) -> str:
        persen = int(self.rate * 100)
        return f"Member {self.tier.capitalize()} ({persen}%)"


class DiskonVoucherNominal(StrategiDiskon):
    """
    Strategi diskon dengan kupon potongan tetap (misal voucher belanja Rp 20.000)
    dengan syarat minimal belanja tertentu.
    """
    def __init__(self, kode_voucher: str, potongan_rupiah: int, minimal_belanja: int = 50000):
        self.kode_voucher = kode_voucher.upper()
        self.potongan_rupiah = potongan_rupiah
        self.minimal_belanja = minimal_belanja

    def hitung_diskon(self, total_kotor: int) -> int:
        if total_kotor >= self.minimal_belanja:
            return min(self.potongan_rupiah, total_kotor)
        return 0

    def deskripsi(self) -> str:
        return f"Voucher '{self.kode_voucher}' (Potongan Rp {self.potongan_rupiah:,})"
