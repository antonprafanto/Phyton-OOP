# ==============================================================================
# SMARTPOS SYSTEM - DOMAIN MODELS (MODUL 1, 2, 3, 4, 8, 10)
# ==============================================================================
# File: models.py
# Deskripsi: Entitas inti bisnis: Produk (Encapsulation), Pengguna & Kasir (Inheritance),
#            serta dataclass ItemKeranjang dan ItemStruk (Dataclass Immutable).
# ==============================================================================

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, Any
from exceptions import StokHabisError, SaldoKasirKurangError, AksesDitolakError


# ------------------------------------------------------------------------------
# 1. ENTITAS PRODUK (ENCAPSULATION & CLASS METHOD)
# ------------------------------------------------------------------------------
class Produk:
    """
    Entitas barang dagangan.
    Menerapkan Encapsulation ketat agar stok tidak bisa diubah langsung
    menjadi bilangan minus.
    """
    _total_macam_produk: int = 0  # Class attribute untuk menghitung katalog unik

    def __init__(self, sku: str, nama: str, harga: int, stok_awal: int, kategori: str = "Umum"):
        if harga < 0:
            raise ValueError(f"Harga produk '{nama}' tidak boleh negatif!")
        if stok_awal < 0:
            raise ValueError(f"Stok awal produk '{nama}' tidak boleh negatif!")

        self.sku = sku.strip().upper()
        self.nama = nama.strip()
        self.harga = harga
        self._stok = stok_awal
        self.kategori = kategori
        Produk._total_macam_produk += 1

    @property
    def stok(self) -> int:
        """Getter nilai stok yang terlindungi."""
        return self._stok

    def kurangi_stok(self, kuantitas: int):
        """Memotong stok dengan validasi batas aman."""
        if kuantitas <= 0:
            raise ValueError("Kuantitas pengurangan stok harus lebih dari 0!")
        if kuantitas > self._stok:
            raise StokHabisError(self.nama, self._stok, kuantitas)
        self._stok -= kuantitas

    def tambah_stok(self, kuantitas: int):
        """Menambah stok barang (Restock)."""
        if kuantitas <= 0:
            raise ValueError("Kuantitas penambahan stok harus lebih dari 0!")
        self._stok += kuantitas

    @classmethod
    def dari_dict(cls, data: Dict[str, Any]) -> "Produk":
        """Alternative constructor untuk melahirkan Produk dari dictionary / JSON."""
        return cls(
            sku=data["sku"],
            nama=data["nama"],
            harga=int(data["harga"]),
            stok_awal=int(data.get("stok", 0)),
            kategori=data.get("kategori", "Umum")
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialisasi produk ke dictionary murni."""
        return {
            "sku": self.sku,
            "nama": self.nama,
            "harga": self.harga,
            "stok": self._stok,
            "kategori": self.kategori
        }

    def __str__(self) -> str:
        return f"[{self.sku}] {self.nama} - Rp {self.harga:,} (Stok: {self._stok})"

    def __repr__(self) -> str:
        return f"Produk(sku='{self.sku}', nama='{self.nama}', harga={self.harga}, stok={self._stok})"


# ------------------------------------------------------------------------------
# 2. HIRARKI PENGGUNA TOKO (INHERITANCE & ABSTRACTION)
# ------------------------------------------------------------------------------
class Pengguna(ABC):
    """Kelas abstrak dasar untuk seluruh pegawai toko."""
    def __init__(self, id_user: str, nama: str, role: str):
        self.id_user = id_user
        self.nama = nama
        self.role = role

    @abstractmethod
    def bisa_otorisasi(self, aksi: str) -> bool:
        """Mengecek hak izin akses terhadap suatu tindakan sistem."""
        pass

    def __str__(self) -> str:
        return f"{self.nama} ({self.role} - ID: {self.id_user})"


class Kasir(Pengguna):
    """
    Staf kasir garis depan yang mengelola laci uang tunai (*cash drawer*).
    """
    def __init__(self, id_user: str, nama: str, modal_laci_awal: int = 200000):
        super().__init__(id_user, nama, role="Kasir")
        self._saldo_laci = modal_laci_awal

    @property
    def saldo_laci(self) -> int:
        return self._saldo_laci

    def terima_uang_tunai(self, nominal: int):
        if nominal <= 0:
            raise ValueError("Nominal setoran tunai harus lebih dari 0!")
        self._saldo_laci += nominal

    def beri_kembalian(self, nominal: int):
        if nominal < 0:
            raise ValueError("Kembalian tidak boleh negatif!")
        if nominal > self._saldo_laci:
            raise SaldoKasirKurangError(self._saldo_laci, nominal)
        self._saldo_laci -= nominal

    def bisa_otorisasi(self, aksi: str) -> bool:
        # Kasir hanya boleh melayani transaksi reguler
        aksi_diizinkan = {"transaksi_jual", "cek_harga", "tutup_kasir"}
        return aksi in aksi_diizinkan


class Manajer(Pengguna):
    """
    Pimpinan cabang yang memiliki wewenang administratif penuh (Supervisor).
    """
    def __init__(self, id_user: str, nama: str):
        super().__init__(id_user, nama, role="Manajer")

    def bisa_otorisasi(self, aksi: str) -> bool:
        # Manajer berhak atas segala tindakan termasuk void dan diskon kustom
        return True


# ------------------------------------------------------------------------------
# 3. MODERN DATACLASS (MODUL 10)
# ------------------------------------------------------------------------------
@dataclass
class ItemKeranjang:
    """Objek pembungkus item belanjaan di dalam kasir."""
    produk: Produk
    jumlah: int

    @property
    def subtotal(self) -> int:
        return self.produk.harga * self.jumlah

    def __str__(self) -> str:
        return f"{self.produk.nama} x{self.jumlah} @ Rp {self.produk.harga:,} = Rp {self.subtotal:,}"


@dataclass(frozen=True)
class ItemStruk:
    """
    Data snapshot struk belanja yang tidak dapat diubah (immutable).
    Menjamin keabsahan catatan akuntansi saat dicetak.
    """
    sku: str
    nama_barang: str
    harga_satuan: int
    kuantitas: int
    subtotal: int
