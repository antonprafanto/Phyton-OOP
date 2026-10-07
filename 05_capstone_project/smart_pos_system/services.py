# ==============================================================================
# SMARTPOS SYSTEM - CORE SERVICES & ENGINE (MODUL 7, 11, 12, 13)
# ==============================================================================
# File: services.py
# Deskripsi: Layanan bisnis terpusat: AuditLogger (Singleton), Inventaris,
#            KeranjangBelanja (Komposisi & Dunder), serta LayananTransaksi (Facade).
# ==============================================================================

from typing import Dict, List, Any, Optional
from datetime import datetime
from models import Produk, Kasir, ItemKeranjang, ItemStruk
from strategies import StrategiDiskon, TanpaDiskon
from payments import MetodePembayaran, BayarTunai
from exceptions import ProdukTidakDitemukanError, StokHabisError, POSError


# ------------------------------------------------------------------------------
# 1. AUDIT LOGGER (SINGLETON PATTERN)
# ------------------------------------------------------------------------------
class AuditLogger:
    """
    Singleton Logger terpusat.
    Mencatat jejak audit seluruh peristiwa penting di toko (pembayaran, restock, error).
    """
    _instance = None
    _terinisialisasi = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._terinisialisasi:
            self._riwayat_log: List[str] = []
            AuditLogger._terinisialisasi = True

    def catat(self, pesan: str):
        waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{waktu}] {pesan}"
        self._riwayat_log.append(entry)

    def ambil_riwayat(self) -> List[str]:
        return list(self._riwayat_log)

    def cetak_semua_log(self):
        print("\n" + "=" * 65)
        print("          JEJAK AUDIT SISTEM TOKO (AUDIT LOG)")
        print("=" * 65)
        if not self._riwayat_log:
            print("(Belum ada catatan log tersimpan)")
        else:
            for log in self._riwayat_log:
                print(log)
        print("=" * 65)


# ------------------------------------------------------------------------------
# 2. INVENTARIS TOKO (MANAJEMEN KATALOG & STOK)
# ------------------------------------------------------------------------------
class Inventaris:
    """Mengelola perbendaharaan katalog produk di toko."""
    def __init__(self):
        self._katalog: Dict[str, Produk] = {}

    def daftarkan_produk(self, produk: Produk):
        self._katalog[produk.sku] = produk

    def cari_produk(self, sku: str) -> Produk:
        kunci = sku.strip().upper()
        if kunci not in self._katalog:
            raise ProdukTidakDitemukanError(sku)
        return self._katalog[kunci]

    def semua_produk(self) -> List[Produk]:
        return list(self._katalog.values())


# ------------------------------------------------------------------------------
# 3. KERANJANG BELANJA (KOMPOSISI DENGAN ITEMKERANJANG & DUNDER METHODS)
# ------------------------------------------------------------------------------
class KeranjangBelanja:
    """
    Wadah sementara belanjaan pelanggan di meja kasir.
    Menerapkan hubungan Komposisi dengan ItemKeranjang dan Dunder Methods.
    """
    def __init__(self):
        self._items: Dict[str, ItemKeranjang] = {}

    def tambah_produk(self, produk: Produk, jumlah: int = 1):
        if jumlah <= 0:
            raise ValueError("Jumlah barang harus minimal 1!")

        sku = produk.sku
        saat_ini = self._items[sku].jumlah if sku in self._items else 0
        total_dibutuhkan = saat_ini + jumlah

        if total_dibutuhkan > produk.stok:
            raise StokHabisError(produk.nama, produk.stok, total_dibutuhkan)

        if sku in self._items:
            self._items[sku].jumlah += jumlah
        else:
            self._items[sku] = ItemKeranjang(produk=produk, jumlah=jumlah)

    def hapus_produk(self, sku: str):
        kunci = sku.strip().upper()
        if kunci in self._items:
            del self._items[kunci]

    def kosongkan(self):
        self._items.clear()

    @property
    def total_kotor(self) -> int:
        return sum(item.subtotal for item in self._items.values())

    def __len__(self) -> int:
        """Dunder method untuk menghitung total kuantitas fisik barang."""
        return sum(item.jumlah for item in self._items.values())

    def __iter__(self):
        """Membuat keranjang bisa di-loop langsung: for item in keranjang."""
        return iter(self._items.values())

    def hitung_rincian(self, strategi_diskon: StrategiDiskon) -> Dict[str, Any]:
        kotor = self.total_kotor
        potongan = strategi_diskon.hitung_diskon(kotor)
        bersih = max(0, kotor - potongan)
        return {
            "total_kotor": kotor,
            "diskon": potongan,
            "total_bersih": bersih,
            "deskripsi_diskon": strategi_diskon.deskripsi()
        }


# ------------------------------------------------------------------------------
# 4. ENGINE LAYANAN TRANSAKSI (FACADE PATTERN)
# ------------------------------------------------------------------------------
class LayananTransaksi:
    """
    Fasad utama yang mengoordinasikan Kasir, Keranjang, Promo, dan Pembayaran
    menjadi satu alur transaksi utuh yang aman.
    """
    _counter_invoice: int = 1000  # Class attribute untuk nomor nota otomatis

    def __init__(self, kasir: Kasir, inventaris: Inventaris):
        self.kasir = kasir
        self.inventaris = inventaris
        self.logger = AuditLogger()

    def proses_checkout(
        self,
        keranjang: KeranjangBelanja,
        strategi_diskon: StrategiDiskon,
        metode_pembayaran: MetodePembayaran,
        **kwargs_bayar
    ) -> Dict[str, Any]:
        """
        Mengeksekusi alur checkout secara atomik:
        1. Cek isi keranjang
        2. Hitung diskon dan total bersih
        3. Proses pembayaran via gateway
        4. Potong stok produk di inventaris
        5. Update saldo kasir jika bayar tunai
        6. Catat audit log & terbitkan struk
        """
        if len(keranjang) == 0:
            raise POSError("Keranjang belanja kosong! Tidak bisa melakukan checkout.", "ERR-EMPTY-CART")

        # 1. Kalkulasi Keuangan
        rincian = keranjang.hitung_rincian(strategi_diskon)
        total_bersih = rincian["total_bersih"]

        # 2. Proses Pembayaran
        hasil_bayar = metode_pembayaran.proses_bayar(total_bersih, **kwargs_bayar)

        # 3. Potong Stok Inventaris
        snapshot_struk: List[ItemStruk] = []
        for item in keranjang:
            item.produk.kurangi_stok(item.jumlah)
            snapshot_struk.append(ItemStruk(
                sku=item.produk.sku,
                nama_barang=item.produk.nama,
                harga_satuan=item.produk.harga,
                kuantitas=item.jumlah,
                subtotal=item.subtotal
            ))

        # 4. Sinkronisasi Kasir jika uang tunai
        if isinstance(metode_pembayaran, BayarTunai):
            self.kasir.terima_uang_tunai(hasil_bayar["uang_diterima"])
            if hasil_bayar["kembalian"] > 0:
                self.kasir.beri_kembalian(hasil_bayar["kembalian"])

        # 5. Terbitkan Nomor Invoice
        LayananTransaksi._counter_invoice += 1
        no_invoice = f"INV-{datetime.now().strftime('%Y%m%d')}-{LayananTransaksi._counter_invoice}"

        # 6. Catat Log Audit
        self.logger.catat(
            f"Transaksi {no_invoice} SUKSES senilai Rp {total_bersih:,} via {metode_pembayaran.nama_metode()} oleh Kasir '{self.kasir.nama}'"
        )

        # 7. Format Struk Resmi
        struk_teks = self._format_struk(no_invoice, snapshot_struk, rincian, hasil_bayar)

        # Kosongkan keranjang setelah sukses
        keranjang.kosongkan()

        return {
            "invoice": no_invoice,
            "rincian": rincian,
            "pembayaran": hasil_bayar,
            "struk_teks": struk_teks
        }

    def _format_struk(
        self,
        invoice: str,
        items: List[ItemStruk],
        rincian: Dict[str, Any],
        pembayaran: Dict[str, Any]
    ) -> str:
        garis = "=" * 52
        garis_tipis = "-" * 52
        waktu = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        baris = [
            garis,
            "             SMART POS RETAIL STORE",
            "         Jl. Malioboro No. 88, Yogyakarta",
            garis,
            f"No. Nota : {invoice}",
            f"Kasir    : {self.kasir.nama} ({self.kasir.id_user})",
            f"Waktu    : {waktu}",
            garis_tipis,
            f"{'Barang':<24}{'Qty':<6}{'Harga':<10}{'Subtotal':>12}",
            garis_tipis
        ]

        for itm in items:
            nama_pendek = itm.nama_barang[:22]
            baris.append(f"{nama_pendek:<24}{itm.kuantitas:<6}{itm.harga_satuan:<10,}{itm.subtotal:>12,}")

        baris.append(garis_tipis)
        baris.append(f"{'Total Kotor':<38} Rp {rincian['total_kotor']:>10,}")
        if rincian['diskon'] > 0:
            baris.append(f"{'Diskon (' + rincian['deskripsi_diskon'] + ')':<38}-Rp {rincian['diskon']:>10,}")
        baris.append(f"{'TOTAL TAGIHAN':<38} Rp {rincian['total_bersih']:>10,}")
        baris.append(garis_tipis)
        baris.append(f"Metode Bayar : {pembayaran['metode']}")
        baris.append(f"Referensi    : {pembayaran['referensi']}")
        baris.append(f"Diterima     : Rp {pembayaran['uang_diterima']:,}")
        baris.append(f"Kembalian    : Rp {pembayaran['kembalian']:,}")
        baris.append(garis)
        baris.append("    Terima Kasih Telah Berbelanja di Toko Kami!    ")
        baris.append("      Barang yang dibeli tidak dapat ditukar.      ")
        baris.append(garis)

        return "\n".join(baris)
