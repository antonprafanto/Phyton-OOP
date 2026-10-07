"""
================================================================================
MODUL 12: PRINSIP S.O.L.I.D UNTUK PEMULA
Berkas 01: Praktik Bagian 1 - S (SRP), O (OCP), dan L (LSP)
================================================================================
Tujuan Pembelajaran:
1. Memecah 'God Object' menjadi class spesifik berfokus tunggal (SRP).
2. Menghindari rantai if-elif diskon dengan strategi polimorfis terbuka (OCP).
3. Mencegah error subclass yang merusak ekspektasi kontrak parent class (LSP).
================================================================================
"""

import sys
from abc import ABC, abstractmethod

# Konfigurasi terminal agar kompatibel dengan encoding Windows / UTF-8
if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass


# ==============================================================================
# 1. [S] - SINGLE RESPONSIBILITY PRINCIPLE (SRP)
# ==============================================================================
class Invoice:
    """HANYA bertanggung jawab menyimpan data transaksi dan kalkulasi total."""
    def __init__(self, id_invoice: str, subtotal: int):
        self.id_invoice = id_invoice
        self.subtotal = subtotal

    def hitung_pajak(self, persen: int = 11) -> int:
        return int(self.subtotal * (persen / 100))

    def hitung_total_akhir(self) -> int:
        return self.subtotal + self.hitung_pajak()


class InvoicePrinter:
    """HANYA bertanggung jawab memformat dan menampilkan struk ke layar."""
    @staticmethod
    def cetak(invoice: Invoice):
        print(f"\n[STRUK] Invoice #{invoice.id_invoice}")
        print(f"  - Subtotal : Rp {invoice.subtotal:,}")
        print(f"  - PPN (11%): Rp {invoice.hitung_pajak():,}")
        print(f"  - TOTAL    : Rp {invoice.hitung_total_akhir():,}")


class InvoiceRepository:
    """HANYA bertanggung jawab menyimpan data invoice ke media penyimpanan/database."""
    @staticmethod
    def simpan_ke_db(invoice: Invoice):
        print(f"[DATABASE] Berhasil menyimpan invoice #{invoice.id_invoice} ke tabel transaksi.")


# ==============================================================================
# 2. [O] - OPEN/CLOSED PRINCIPLE (OCP)
# Terbuka untuk penambahan tipe diskon baru, tertutup dari pengubahan kode lama.
# ==============================================================================
class AturanDiskon(ABC):
    @abstractmethod
    def hitung_potongan(self, subtotal: int) -> int:
        pass


class DiskonReguler(AturanDiskon):
    def hitung_potongan(self, subtotal: int) -> int:
        return int(subtotal * 0.05)  # Diskon 5%


class DiskonVIP(AturanDiskon):
    def hitung_potongan(self, subtotal: int) -> int:
        return int(subtotal * 0.15)  # Diskon 15%


# Menambah diskon baru? CUKUP BUAT CLASS BARU tanpa menyentuh kode di atas!
class DiskonFlashSale(AturanDiskon):
    def hitung_potongan(self, subtotal: int) -> int:
        return int(subtotal * 0.30)  # Diskon 30%


class KasirPembayaran:
    @staticmethod
    def proses(subtotal: int, strategi_diskon: AturanDiskon) -> int:
        potongan = strategi_diskon.hitung_potongan(subtotal)
        total_bayar = subtotal - potongan
        print(f"[KASIR] Subtotal: Rp {subtotal:,} | Potongan: Rp {potongan:,} -> Bayar: Rp {total_bayar:,}")
        return total_bayar


# ==============================================================================
# 3. [L] - LISKOV SUBSTITUTION PRINCIPLE (LSP)
# Subclass harus bisa menggantikan parent class tanpa menimbulkan error crash.
# ==============================================================================
class Burung(ABC):
    def __init__(self, nama: str):
        self.nama = nama

    @abstractmethod
    def bersuara(self) -> str:
        pass


class BurungBisaTerbang(Burung):
    """Sub-kategori khusus untuk burung yang memiliki kemampuan terbang."""
    @abstractmethod
    def terbang(self) -> str:
        pass


class Merpati(BurungBisaTerbang):
    def bersuara(self) -> str:
        return "Kukuruyuuu / Coo coo!"

    def terbang(self) -> str:
        return f"{self.nama} mengepakkan sayap dan meluncur di udara."


class BurungUnta(Burung):
    """BurungUnta adalah Burung, tapi BUKAN BurungBisaTerbang!"""
    def bersuara(self) -> str:
        return "Boom boom hiss!"

    def lari_cepat(self) -> str:
        return f"{self.nama} berlari kencang dengan kecepatan 70 km/jam!"


def simulasi_migrasi_udara(daftar_penerbang: list[BurungBisaTerbang]):
    print("\n--- Simulasi Formasi Terbang di Langit ---")
    for penerbang in daftar_penerbang:
        # Dijamin 100% AMAN! Tidak akan ada crash NotImplementedError
        print(f"  -> {penerbang.terbang()}")


# ==============================================================================
# BLOK PENGUJIAN
# ==============================================================================
if __name__ == "__main__":
    print("=" * 65)
    print("[DEMO 1] SINGLE RESPONSIBILITY PRINCIPLE (SRP)")
    print("=" * 65)

    inv = Invoice("INV-2026-001", subtotal=500_000)
    InvoicePrinter.cetak(inv)
    InvoiceRepository.simpan_ke_db(inv)

    print("\n" + "=" * 65)
    print("[DEMO 2] OPEN/CLOSED PRINCIPLE (OCP)")
    print("=" * 65)

    belanjaan = 1_000_000
    KasirPembayaran.proses(belanjaan, DiskonReguler())
    KasirPembayaran.proses(belanjaan, DiskonVIP())
    KasirPembayaran.proses(belanjaan, DiskonFlashSale())

    print("\n" + "=" * 65)
    print("[DEMO 3] LISKOV SUBSTITUTION PRINCIPLE (LSP)")
    print("=" * 65)

    merpati_pos = Merpati("Merpati Pos Jakarta")
    elang_jawa = Merpati("Elang Jawa Langka")  # Subtipe terbang
    unta_afrika = BurungUnta("Unta Savana")

    print(f"Suara Burung Unta : {unta_afrika.bersuara()}")
    print(f"Aksi Burung Unta  : {unta_afrika.lari_cepat()}")

    # Fungsi migrasi udara HANYA menerima BurungBisaTerbang
    kawanan_terbang = [merpati_pos, elang_jawa]
    simulasi_migrasi_udara(kawanan_terbang)

    print("\n" + "=" * 65)
    print("[OK] Selesai: Tiga pilar pertama SOLID (SRP, OCP, LSP) teruji sempurna.")
    print("=" * 65)
