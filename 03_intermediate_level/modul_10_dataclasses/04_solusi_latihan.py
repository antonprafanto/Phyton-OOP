"""
================================================================================
MODUL 10: MODERN PYTHON SHORTCUT (@dataclass) & TYPE HINTING
Berkas 04: Solusi Resmi & Pembahasan Model Data VibeStore
================================================================================
STUDI KASUS: SISTEM KERANJANG BELANJA "VIBESTORE"
================================================================================
"""

import sys
from dataclasses import dataclass, field, asdict

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass


# ==============================================================================
# MODEL DATA 1: PRODUK (FROZEN / READ-ONLY)
# ==============================================================================
@dataclass(frozen=True)
class Produk:
    sku: str
    nama: str
    harga: int
    kategori: str = "Umum"

    def __post_init__(self):
        if self.harga <= 0:
            raise ValueError(f"Harga produk '{self.nama}' harus positif! Diterima: {self.harga}")


# ==============================================================================
# MODEL DATA 2: ITEM KERANJANG
# ==============================================================================
@dataclass
class ItemKeranjang:
    produk: Produk
    jumlah: int
    subtotal: int = field(init=False)

    def __post_init__(self):
        if self.jumlah < 1:
            raise ValueError(f"Jumlah pesanan untuk '{self.produk.nama}' minimal 1! Diterima: {self.jumlah}")
        self.subtotal = self.produk.harga * self.jumlah


# ==============================================================================
# MODEL DATA 3: KERANJANG BELANJA
# ==============================================================================
@dataclass
class KeranjangBelanja:
    nama_pelanggan: str
    daftar_item: list[ItemKeranjang] = field(default_factory=list)

    def tambah_item(self, produk: Produk, jumlah: int = 1):
        item = ItemKeranjang(produk=produk, jumlah=jumlah)
        self.daftar_item.append(item)
        print(f"[KERANJANG] Menambahkan {jumlah}x '{produk.nama}' ke keranjang {self.nama_pelanggan}.")

    def hitung_total_belanja(self) -> int:
        return sum(item.subtotal for item in self.daftar_item)

    @staticmethod
    def format_rupiah(angka: int) -> str:
        return f"Rp {angka:,.0f}".replace(",", ".")

    def cetak_struk(self):
        print("\n+" + "=" * 54 + "+")
        print(f"|            STRUK BELANJA ONLINE VIBESTORE            |")
        print("+" + "=" * 54 + "+")
        print(f"| Pelanggan : {self.nama_pelanggan:<40} |")
        print("+" + "-" * 54 + "+")
        print(f"| {'Item':<22} | {'Qty':<4} | {'Subtotal':<20} |")
        print("+" + "-" * 54 + "+")

        for item in self.daftar_item:
            nama_ringkas = (item.produk.nama[:19] + "..") if len(item.produk.nama) > 21 else item.produk.nama
            subtotal_str = self.format_rupiah(item.subtotal)
            print(f"| {nama_ringkas:<22} | {item.jumlah:<4} | {subtotal_str:<20} |")

        total_str = self.format_rupiah(self.hitung_total_belanja())
        print("+" + "=" * 54 + "+")
        print(f"| TOTAL TAGIHAN : {total_str:<36} |")
        print("+" + "=" * 54 + "+\n")


# ==============================================================================
# PENGUJIAN DAN VERIFIKASI KUNCI JAWABAN
# ==============================================================================
if __name__ == "__main__":
    print("=" * 65)
    print("[SOLUSI] PENGUJIAN MODEL DATA E-COMMERCE VIBESTORE")
    print("=" * 65)

    # 1. Membuat Katalog Produk (Frozen / Kebal Modifikasi)
    p1 = Produk(sku="SKU-KBD-01", nama="Keyboard Mekanikal RGB", harga=650_000, kategori="Aksesoris")
    p2 = Produk(sku="SKU-MOU-02", nama="Mouse Gaming Wireless", harga=350_000, kategori="Aksesoris")
    p3 = Produk(sku="SKU-MON-03", nama="Monitor 27 Inch 165Hz", harga=2_400_000, kategori="Monitor")

    print(f"Produk 1 Terdaftar: {p1}")
    print(f"Produk 2 Terdaftar: {p2}")

    # Uji Kekebalan Produk (frozen=True)
    try:
        p1.harga = 100_000  # type: ignore
    except Exception as err:
        print(f"[PROTEKSI] Harga produk kebal perubahan tidak sah: {type(err).__name__}")

    # 2. Belanja dengan Keranjang
    keranjang_anton = KeranjangBelanja(nama_pelanggan="Anton Prafanto")
    keranjang_anton.tambah_item(p1, jumlah=1)
    keranjang_anton.tambah_item(p2, jumlah=2)
    keranjang_anton.tambah_item(p3, jumlah=1)

    # 3. Cetak Struk Belanja
    keranjang_anton.cetak_struk()

    # 4. Validasi Error jika Jumlah < 1
    print("--- Uji Validasi Aturan Bisnis ---")
    try:
        keranjang_anton.tambah_item(p1, jumlah=0)
    except ValueError as val_err:
        print(f"[VALIDASI BERHASIL] ❌ {val_err}")

    # 5. Konversi ke Dictionary (Siap Kirim ke API Payment)
    payload_keranjang = {
        "customer": keranjang_anton.nama_pelanggan,
        "total": keranjang_anton.hitung_total_belanja(),
        "items": [asdict(item) for item in keranjang_anton.daftar_item]
    }
    print(f"\nPayload Siap API (asdict): {payload_keranjang['customer']} belanja {len(payload_keranjang['items'])} item.")

    print("\n" + "=" * 65)
    print("[OK] Selesai: Model Data @dataclass berhasil diuji secara tuntas!")
    print("=" * 65)
