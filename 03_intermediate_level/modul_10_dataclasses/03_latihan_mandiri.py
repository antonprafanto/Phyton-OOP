"""
================================================================================
MODUL 10: MODERN PYTHON SHORTCUT (@dataclass) & TYPE HINTING
Berkas 03: Lembar Latihan Mandiri (Model Data E-Commerce VibeStore)
================================================================================
STUDI KASUS: SISTEM KERANJANG BELANJA "VIBESTORE"

Deskripsi Tugas:
Anda diminta membangun struktur data e-commerce modern menggunakan @dataclass.
Model data harus bersih, memiliki nilai default, kalkulasi otomatis, dan proteksi.

Spesifikasi yang Harus Dibuat:

1. `@dataclass(frozen=True)` `Produk`:
   - Field:
     * `sku: str` (Kode barang unik, misal 'PRD-001')
     * `nama: str`
     * `harga: int`
     * `kategori: str = "Umum"`
   - Di method `__post_init__`:
     * Validasi: harga harus > 0 (jika <= 0, lempar ValueError).

2. `@dataclass` `ItemKeranjang`:
   - Field:
     * `produk: Produk`
     * `jumlah: int`
     * `subtotal: int = field(init=False)`
   - Di method `__post_init__`:
     * Validasi: jumlah minimal 1 (jika < 1, lempar ValueError).
     * Hitung subtotal otomatis: `self.subtotal = self.produk.harga * self.jumlah`

3. `@dataclass` `KeranjangBelanja`:
   - Field:
     * `nama_pelanggan: str`
     * `daftar_item: list[ItemKeranjang] = field(default_factory=list)`
   - Method:
     * `tambah_item(self, produk: Produk, jumlah: int = 1)`:
       Membuat ItemKeranjang baru dan menambahkannya ke self.daftar_item.
     * `hitung_total_belanja(self) -> int`:
       Mengembalikan total seluruh subtotal belanjaan.
     * `cetak_struk(self)`:
       Menampilkan rincian daftar belanja beserta total akhir.

================================================================================
PETUNJUK:
Lengkapi blok kode dengan tanda [TODO] di bawah ini.
Setelah selesai, jalankan file ini. Jika output sesuai harapan, bandingkan
jawaban Anda dengan '04_solusi_latihan.py'.
================================================================================
"""

import sys
from dataclasses import dataclass, field

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass


# ==============================================================================
# MODEL DATA 1: PRODUK (FROZEN / READ-ONLY)
# ==============================================================================
# [TODO 1]: Pasang decorator @dataclass(frozen=True)
class Produk:
    sku: str
    nama: str
    harga: int
    kategori: str = "Umum"

    def __post_init__(self):
        # [TODO 2]: Validasi harga > 0
        pass


# ==============================================================================
# MODEL DATA 2: ITEM KERANJANG
# ==============================================================================
# [TODO 3]: Pasang decorator @dataclass
class ItemKeranjang:
    produk: Produk
    jumlah: int
    # [TODO 4]: Pasang subtotal dengan field(init=False)
    subtotal: int = 0

    def __post_init__(self):
        # [TODO 5]: Validasi jumlah >= 1 dan hitung subtotal otomatis
        pass


# ==============================================================================
# MODEL DATA 3: KERANJANG BELANJA
# ==============================================================================
# [TODO 6]: Pasang decorator @dataclass
class KeranjangBelanja:
    nama_pelanggan: str
    # [TODO 7]: Gunakan field(default_factory=list)
    daftar_item: list = []

    def tambah_item(self, produk: Produk, jumlah: int = 1):
        # [TODO 8]: Buat ItemKeranjang dan masukkan ke daftar_item
        pass

    def hitung_total_belanja(self) -> int:
        # [TODO 9]: Hitung total seluruh subtotal
        pass

    def cetak_struk(self):
        # [TODO 10]: Tampilkan struk kasir rapi
        pass


# ==============================================================================
# AREA PENGUJIAN OTOMATIS
# ==============================================================================
if __name__ == "__main__":
    print("=" * 65)
    print("[UJI COBA] MODEL DATA E-COMMERCE VIBESTORE")
    print("=" * 65)

    print("\nSilakan lengkapi kode di atas, lalu aktifkan kode pengujian di bawah ini:\n")

    # p1 = Produk("SKU-01", "Keyboard Mekanikal", 650_000, "Elektronik")
    # p2 = Produk("SKU-02", "Mouse Gaming", 250_000, "Elektronik")

    # keranjang = KeranjangBelanja("Anton P.")
    # keranjang.tambah_item(p1, jumlah=1)
    # keranjang.tambah_item(p2, jumlah=2)
    # keranjang.cetak_struk()
