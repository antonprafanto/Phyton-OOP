# ==============================================================================
# SMARTPOS SYSTEM - AUTOMATED INTEGRATION & UNIT TESTS
# ==============================================================================
# File: test_pos.py
# Deskripsi: Skrip pengujian otomatis menyeluruh untuk memverifikasi kebenaran
#            seluruh pilar OOP, Dunder methods, Exceptions, dan Design Patterns.
# ==============================================================================

import sys
from models import Produk, Kasir, Manajer, ItemStruk
from strategies import TanpaDiskon, DiskonMember, DiskonVoucherNominal
from payments import PembayaranFactory, BayarTunai, BayarQRIS, BayarKartuDebit
from services import Inventaris, KeranjangBelanja, LayananTransaksi, AuditLogger
from exceptions import StokHabisError, SaldoKasirKurangError, PembayaranGagalError, POSError

# Konfigurasi terminal agar output UTF-8 berjalan mulus di Windows PowerShell
if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass


def test_semua_komponen():
    print("=" * 70)
    print("MEMULAI PENGUJIAN OTOMATIS: SMARTPOS SYSTEM")
    print("=" * 70)

    # --------------------------------------------------------------------------
    # 1. PENGUJIAN PRODUK & ENCAPSULATION
    # --------------------------------------------------------------------------
    print("\n[1/8] Menguji Entitas Produk & Proteksi Stok...")
    kopi = Produk("KOP-01", "Kopi Susu Gula Aren", 18000, 20, "Minuman")
    assert kopi.stok == 20
    kopi.kurangi_stok(5)
    assert kopi.stok == 15
    kopi.tambah_stok(10)
    assert kopi.stok == 25

    # Uji deteksi stok habis
    error_stok_tertangkap = False
    try:
        kopi.kurangi_stok(30)
    except StokHabisError:
        error_stok_tertangkap = True
    assert error_stok_tertangkap, "GAGAL: StokHabisError harus dilempar ketika stok tidak cukup!"
    print("      [PASSED] Encapsulation stok & StokHabisError berfungsi sempurna.")

    # --------------------------------------------------------------------------
    # 2. PENGUJIAN HIRARKI PENGGUNA (INHERITANCE) & KASIR
    # --------------------------------------------------------------------------
    print("\n[2/8] Menguji Hirarki Pengguna & Keamanan Saldo Kasir...")
    kasir = Kasir("KSR-01", "Siti Aminah", modal_laci_awal=200000)
    manajer = Manajer("MGR-01", "Budi Santoso")
    assert kasir.bisa_otorisasi("transaksi_jual") is True
    assert kasir.bisa_otorisasi("void_transaksi") is False
    assert manajer.bisa_otorisasi("void_transaksi") is True

    # Uji laci kasir
    kasir.terima_uang_tunai(50000)
    assert kasir.saldo_laci == 250000
    kasir.beri_kembalian(20000)
    assert kasir.saldo_laci == 230000

    error_laci_tertangkap = False
    try:
        kasir.beri_kembalian(300000)
    except SaldoKasirKurangError:
        error_laci_tertangkap = True
    assert error_laci_tertangkap, "GAGAL: SaldoKasirKurangError harus dilempar jika uang laci kurang!"
    print("      [PASSED] Inheritance pengguna & perlindungan laci kasir valid.")

    # --------------------------------------------------------------------------
    # 3. PENGUJIAN IMMUTABILITY DATACLASS (ITEMSTRUK)
    # --------------------------------------------------------------------------
    print("\n[3/8] Menguji Kekebalan Dataclass (@dataclass frozen=True)...")
    item_struk = ItemStruk("KOP-01", "Kopi Susu", 18000, 2, 36000)
    error_frozen_tertangkap = False
    try:
        item_struk.harga_satuan = 10000  # Mencoba memanipulasi bukti struk
    except Exception:
        error_frozen_tertangkap = True
    assert error_frozen_tertangkap, "GAGAL: ItemStruk harus kebal manipulasi atribut!"
    print("      [PASSED] Dataclass ItemStruk terbukti aman dari perubahan tidak sah.")

    # --------------------------------------------------------------------------
    # 4. PENGUJIAN STRATEGY PATTERNS (DISKON)
    # --------------------------------------------------------------------------
    print("\n[4/8] Menguji Ragam Algoritma Strategi Diskon...")
    total_belanja = 100000
    strat_reguler = TanpaDiskon()
    strat_gold = DiskonMember("gold")  # 15%
    strat_silver = DiskonMember("silver")  # 10%
    strat_voucher = DiskonVoucherNominal("HEMAT20", 20000, minimal_belanja=50000)

    assert strat_reguler.hitung_diskon(total_belanja) == 0
    assert strat_gold.hitung_diskon(total_belanja) == 15000
    assert strat_silver.hitung_diskon(total_belanja) == 10000
    assert strat_voucher.hitung_diskon(total_belanja) == 20000
    print("      [PASSED] Seluruh formula diskon Strategy Pattern terhitung tepat.")

    # --------------------------------------------------------------------------
    # 5. PENGUJIAN FACTORY METHOD & SALURAN PEMBAYARAN
    # --------------------------------------------------------------------------
    print("\n[5/8] Menguji Factory Method & Eksekusi Pembayaran...")
    bayar_tunai = PembayaranFactory.buat_metode("tunai")
    bayar_qris = PembayaranFactory.buat_metode("qris")
    bayar_debit = PembayaranFactory.buat_metode("debit")

    assert isinstance(bayar_tunai, BayarTunai)
    assert isinstance(bayar_qris, BayarQRIS)
    assert isinstance(bayar_debit, BayarKartuDebit)

    # Uji pembayaran tunai cukup & kembalian
    hasil_tunai = bayar_tunai.proses_bayar(80000, uang_diterima=100000)
    assert hasil_tunai["kembalian"] == 20000

    # Uji pembayaran tunai kurang
    error_bayar_kurang = False
    try:
        bayar_tunai.proses_bayar(80000, uang_diterima=50000)
    except PembayaranGagalError:
        error_bayar_kurang = True
    assert error_bayar_kurang, "GAGAL: Uang tunai kurang harus melempar PembayaranGagalError!"

    # Uji debit dengan PIN salah
    error_pin = False
    try:
        bayar_debit.proses_bayar(80000, nomor_kartu="12345678", pin="123")  # PIN hanya 3 digit
    except PembayaranGagalError:
        error_pin = True
    assert error_pin, "GAGAL: PIN kurang dari 6 digit harus ditolak!"
    print("      [PASSED] Factory Method & validasi gerbang pembayaran berjalan sempurna.")

    # --------------------------------------------------------------------------
    # 6. PENGUJIAN KERANJANG BELANJA (KOMPOSISI & DUNDER METHODS)
    # --------------------------------------------------------------------------
    print("\n[6/8] Menguji Keranjang Belanja & Dunder Methods (__len__, __iter__)...")
    inv = Inventaris()
    roti = Produk("ROT-01", "Roti Cokelat Keju", 12000, 15, "Makanan")
    inv.daftarkan_produk(kopi)
    inv.daftarkan_produk(roti)

    keranjang = KeranjangBelanja()
    keranjang.tambah_produk(kopi, 2)   # 2 x 18000 = 36000
    keranjang.tambah_produk(roti, 3)   # 3 x 12000 = 36000
    assert len(keranjang) == 5, f"GAGAL: Total fisik barang harus 5, didapat {len(keranjang)}"
    assert keranjang.total_kotor == 72000

    # Uji iterasi langsung (duck typing iter)
    total_hitung_manual = sum(item.subtotal for item in keranjang)
    assert total_hitung_manual == 72000
    print("      [PASSED] Dunder method __len__ dan __iter__ pada Keranjang sukses.")

    # --------------------------------------------------------------------------
    # 7. PENGUJIAN FULL TRANSAKSI CHECKOUT & PEMOTONGAN STOK
    # --------------------------------------------------------------------------
    print("\n[7/8] Menguji Alur Penuh Layanan Checkout (LayananTransaksi Facade)...")
    stok_kopi_sebelum = kopi.stok
    stok_roti_sebelum = roti.stok
    saldo_laci_sebelum = kasir.saldo_laci

    layanan = LayananTransaksi(kasir, inv)
    checkout_res = layanan.proses_checkout(
        keranjang=keranjang,
        strategi_diskon=strat_silver,  # Diskon 10% dari 72000 = 7200 -> Total = 64800
        metode_pembayaran=bayar_tunai,
        uang_diterima=70000
    )

    assert checkout_res["rincian"]["total_bersih"] == 64800
    assert checkout_res["pembayaran"]["kembalian"] == 5200
    # Pastikan stok terpotong
    assert kopi.stok == stok_kopi_sebelum - 2
    assert roti.stok == stok_roti_sebelum - 3
    # Pastikan kasir bertambah uang bersihnya (+64800)
    assert kasir.saldo_laci == saldo_laci_sebelum + 64800
    # Pastikan keranjang telah kosong
    assert len(keranjang) == 0
    # Pastikan teks struk tercetak
    assert "SMART POS RETAIL STORE" in checkout_res["struk_teks"]
    print("      [PASSED] Checkout terpadu sukses: stok terpotong & laci kasir tersinkron.")

    # --------------------------------------------------------------------------
    # 8. PENGUJIAN SINGLETON AUDIT LOGGER
    # --------------------------------------------------------------------------
    print("\n[8/8] Menguji Keutuhan Singleton AuditLogger...")
    logger_1 = AuditLogger()
    logger_2 = AuditLogger()
    assert logger_1 is logger_2, "GAGAL: Logger 1 dan 2 harus menunjuk ke fisik memori yang sama!"
    riwayat = logger_1.ambil_riwayat()
    assert len(riwayat) >= 1, "GAGAL: Harus ada jejak transaksi tercatat di audit logger!"
    print(f"      [PASSED] Singleton terverifikasi! Catatan log tersimpan: {len(riwayat)}")

    print("\n" + "=" * 70)
    print("STATUS KELULUSAN: 100% SUKSES! SELURUH 8 PENGUJIAN MODULAR LOLOS SEMPURNA!")
    print("=" * 70)


if __name__ == "__main__":
    test_semua_komponen()
