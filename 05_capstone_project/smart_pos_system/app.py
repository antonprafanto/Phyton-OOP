# ==============================================================================
# SMARTPOS SYSTEM - INTERACTIVE TERMINAL APPLICATION (CAPSTONE)
# ==============================================================================
# File: app.py
# Deskripsi: Aplikasi kasir retail modern berbasis CLI yang menyatukan
#            seluruh 13 modul OOP ke dalam pengalaman pengguna yang hidup.
#
# CARA MENJALANKAN:
# 1. Mode Interaktif (Manual Kasir):
#    python 05_capstone_project/smart_pos_system/app.py
# 2. Mode Demo Otomatis (Simulasi Cepat):
#    python 05_capstone_project/smart_pos_system/app.py --demo
# ==============================================================================

import sys
import time
from typing import Optional

from models import Produk, Kasir, Manajer
from strategies import (
    StrategiDiskon, TanpaDiskon, DiskonMember, DiskonVoucherNominal
)
from payments import (
    PembayaranFactory, BayarTunai, BayarQRIS, BayarKartuDebit
)
from services import (
    Inventaris, KeranjangBelanja, LayananTransaksi, AuditLogger
)
from exceptions import POSError, StokHabisError, ProdukTidakDitemukanError

# Konfigurasi terminal agar output UTF-8 berjalan mulus di Windows PowerShell
if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass


class SmartPOSApp:
    """
    Kelas pengendali antarmuka aplikasi Kasir SmartPOS.
    Mengatur navigasi menu dan orkestrasi layanan bisnis.
    """
    def __init__(self):
        self.inventaris = Inventaris()
        self.kasir = Kasir(id_user="KSR-101", nama="Siti Rahma", modal_laci_awal=250000)
        self.manajer = Manajer(id_user="MGR-001", nama="Budi Santoso")
        self.layanan_transaksi = LayananTransaksi(self.kasir, self.inventaris)
        self.logger = AuditLogger()
        self._isi_data_awal()

    def _isi_data_awal(self):
        """Memasukkan produk awal ke dalam katalog toko."""
        katalog_awal = [
            Produk("KOP-01", "Kopi Hitam Tubruk", 10000, 30, "Minuman"),
            Produk("KOP-02", "Kopi Susu Aren Spesial", 18000, 25, "Minuman"),
            Produk("ROT-01", "Roti Bakar Cokelat", 15000, 20, "Makanan"),
            Produk("ROT-02", "Croissant French Butter", 22000, 15, "Makanan"),
            Produk("AIR-01", "Air Mineral 600ml", 5000, 50, "Minuman"),
            Produk("SNA-01", "Kentang Goreng Keju", 16000, 18, "Camilan")
        ]
        for p in katalog_awal:
            self.inventaris.daftarkan_produk(p)
        self.logger.catat(f"Sistem SmartPOS diinisialisasi dengan {len(katalog_awal)} produk katalog.")

    def tampilkan_header(self):
        print("\n" + "=" * 65)
        print("          SMART POS RETAIL - TOKO SERBA ADA MODERN")
        print(f" Kasir Aktif : {self.kasir.nama} ({self.kasir.id_user}) | Saldo Laci: Rp {self.kasir.saldo_laci:,}")
        print("=" * 65)

    def menu_lihat_katalog(self):
        print("\n--- KATALOG PRODUK & ETALASE STOK ---")
        print(f"{'SKU':<10}{'Nama Produk':<26}{'Kategori':<12}{'Harga':<10}{'Stok':<6}")
        print("-" * 65)
        for p in self.inventaris.semua_produk():
            status_stok = f"{p.stok} unit" if p.stok > 0 else "HABIS!"
            print(f"{p.sku:<10}{p.nama:<26}{p.kategori:<12}Rp {p.harga:<7,}{status_stok:<6}")
        print("-" * 65)

    def menu_transaksi_kasir(self):
        print("\n" + "=" * 65)
        print("                 MEJA TRANSAKSI KASIR BARU")
        print("=" * 65)

        keranjang = KeranjangBelanja()

        while True:
            self.menu_lihat_katalog()
            print(f"\nKeranjang saat ini: {len(keranjang)} unit | Total: Rp {keranjang.total_kotor:,}")
            sku = input("\nMasukkan SKU Produk (atau ketik 'SELESAI' untuk bayar, 'BATAL' untuk keluar): ").strip().upper()

            if sku == "BATAL":
                print("[Kasir] Transaksi dibatalkan.")
                return
            if sku == "SELESAI":
                if len(keranjang) == 0:
                    print("[Peringatan] Keranjang masih kosong! Silakan tambahkan minimal 1 barang.")
                    continue
                break

            try:
                produk = self.inventaris.cari_produk(sku)
                qty_input = input(f"Jumlah '{produk.nama}' yang dibeli [Default 1]: ").strip()
                qty = int(qty_input) if qty_input else 1
                keranjang.tambah_produk(produk, qty)
                print(f"[OK] Berhasil menambahkan {qty}x {produk.nama} ke keranjang!")
            except (POSError, ValueError) as err:
                print(f"[GAGAL] {err}")

        # 1. Pilih Strategi Diskon
        strategi_diskon = self._pilih_strategi_diskon()

        # 2. Pilih Metode Pembayaran & Jalankan Checkout
        self._proses_pembayaran_dan_cetak(keranjang, strategi_diskon)

    def _pilih_strategi_diskon(self) -> StrategiDiskon:
        print("\n--- PILIH STRATEGI PROMO / DISKON ---")
        print("1. Tanpa Promo (Harga Normal)")
        print("2. Member Gold (Diskon 15%)")
        print("3. Member Silver (Diskon 10%)")
        print("4. Voucher Belanja 'HEMAT10K' (Potongan Rp 10.000, Min. Belanja 30k)")
        pilihan = input("Pilihan promo [1-4, Default: 1]: ").strip()

        if pilihan == "2":
            return DiskonMember("gold")
        elif pilihan == "3":
            return DiskonMember("silver")
        elif pilihan == "4":
            return DiskonVoucherNominal("HEMAT10K", 10000, 30000)
        return TanpaDiskon()

    def _proses_pembayaran_dan_cetak(self, keranjang: KeranjangBelanja, strategi: StrategiDiskon):
        rincian = keranjang.hitung_rincian(strategi)
        tagihan = rincian["total_bersih"]

        print("\n--- PILIH METODE PEMBAYARAN ---")
        print(f"Total yang wajib dibayar: Rp {tagihan:,}")
        print("1. Uang Tunai (Cash)")
        print("2. QRIS (Digital Scan)")
        print("3. Kartu Debit (Mesin EDC)")
        opsi = input("Pilih metode bayar [1-3, Default: 1]: ").strip()

        try:
            if opsi == "2":
                metode = PembayaranFactory.buat_metode("qris")
                kwargs = {}
            elif opsi == "3":
                metode = PembayaranFactory.buat_metode("debit")
                no_kartu = input("Masukkan nomor kartu debit (min 4 digit): ").strip() or "6011-8899"
                pin = input("Masukkan PIN EDC 6 digit: ").strip() or "123456"
                kwargs = {"nomor_kartu": no_kartu, "pin": pin}
            else:
                metode = PembayaranFactory.buat_metode("tunai")
                nominal_str = input(f"Masukkan nominal uang tunai diterima [Min Rp {tagihan:,}]: ").strip()
                nominal = int(nominal_str) if nominal_str else tagihan
                kwargs = {"uang_diterima": nominal}

            # Eksekusi via Facade
            hasil = self.layanan_transaksi.proses_checkout(
                keranjang=keranjang,
                strategi_diskon=strategi,
                metode_pembayaran=metode,
                **kwargs
            )

            print("\n" + hasil["struk_teks"])
            print("\n[TRANSAKSI SUKSES] Bukti pembayaran telah dicetak dan stok telah diperbarui.")

        except (POSError, ValueError) as err:
            print(f"\n[TRANSAKSI GAGAL] {err}")
            self.logger.catat(f"Transaksi GAGAL: {err}")

    def menu_restock_inventaris(self):
        print("\n--- RESTOCK INVENTARIS TOKO ---")
        sku = input("Masukkan SKU produk yang ingin ditambah stoknya: ").strip().upper()
        try:
            produk = self.inventaris.cari_produk(sku)
            qty = int(input(f"Masukkan jumlah unit penambahan stok untuk '{produk.nama}': ").strip())
            produk.tambah_stok(qty)
            self.logger.catat(f"Restock: SKU {sku} ({produk.nama}) ditambah {qty} unit. Stok baru: {produk.stok}")
            print(f"[SUKSES] Stok '{produk.nama}' berhasil ditambah! Stok sekarang: {produk.stok}")
        except (POSError, ValueError) as err:
            print(f"[GAGAL] {err}")

    def menu_audit_dan_laci(self):
        print("\n" + "=" * 65)
        print("             INFORMASI KEUANGAN & AUDIT LOG")
        print("=" * 65)
        print(f"Nama Kasir Bertugas : {self.kasir.nama} ({self.kasir.id_user})")
        print(f"Saldo Kas Laci Saat Ini : Rp {self.kasir.saldo_laci:,}")
        self.logger.cetak_semua_log()

    def jalankan_demo_otomatis(self):
        """Menjalankan simulasi skenario nyata kasir secara terprogram tanpa input keyboard."""
        print("=" * 70)
        print("          MEMULAI SIMULASI OTOMATIS SMARTPOS (--DEMO)")
        print("=" * 70)

        # 1. Buka keranjang baru
        print("\n[Langkah 1] Pelanggan datang dan Kasir 'Siti' membuka transaksi...")
        keranjang = KeranjangBelanja()
        p1 = self.inventaris.cari_produk("KOP-02")  # Kopi Susu Aren Rp 18.000
        p2 = self.inventaris.cari_produk("ROT-02")  # Croissant Butter Rp 22.000

        print(f"-> Menambahkan 2x {p1.nama} (Rp {p1.harga:,})")
        keranjang.tambah_produk(p1, 2)
        print(f"-> Menambahkan 1x {p2.nama} (Rp {p2.harga:,})")
        keranjang.tambah_produk(p2, 1)

        print(f"-> Total fisik barang di keranjang: {len(keranjang)} unit")
        print(f"-> Subtotal kotor belanjaan       : Rp {keranjang.total_kotor:,}")

        # 2. Pelanggan menunjukkan kartu Member Gold
        print("\n[Langkah 2] Pelanggan menunjukkan Member Gold (Diskon 15%)...")
        diskon_gold = DiskonMember("gold")
        rincian = keranjang.hitung_rincian(diskon_gold)
        print(f"-> Potongan diskon 15%            : Rp {rincian['diskon']:,}")
        print(f"-> Total bersih tagihan           : Rp {rincian['total_bersih']:,}")

        # 3. Pelanggan membayar dengan Uang Tunai Rp 60.000
        print("\n[Langkah 3] Pelanggan membayar uang tunai Rp 60.000...")
        metode_bayar = PembayaranFactory.buat_metode("tunai")

        saldo_laci_awal = self.kasir.saldo_laci
        hasil_trx = self.layanan_transaksi.proses_checkout(
            keranjang=keranjang,
            strategi_diskon=diskon_gold,
            metode_pembayaran=metode_bayar,
            uang_diterima=60000
        )

        print("\n--- STRUK HASIL SIMULASI ---")
        print(hasil_trx["struk_teks"])

        print(f"\n[Status Kasir] Saldo laci kasir bertambah dari Rp {saldo_laci_awal:,} menjadi Rp {self.kasir.saldo_laci:,}")
        print(f"[Status Stok] Sisa stok '{p1.nama}': {p1.stok} unit")
        print(f"[Status Stok] Sisa stok '{p2.nama}': {p2.stok} unit")

        # 4. Tampilkan catatan audit log
        print("\n[Langkah 4] Memeriksa catatan Singleton AuditLogger...")
        self.logger.cetak_semua_log()

        print("\n" + "=" * 70)
        print("SIMULASI DEMO SMARTPOS SELESAI DENGAN STATUS 100% SUKSES!")
        print("=" * 70)

    def mulai(self):
        """Memulai loop menu utama aplikasi interaktif."""
        while True:
            self.tampilkan_header()
            print("1. 📋 Lihat Katalog Produk & Stok Etalase")
            print("2. 🛒 Buka Meja Kasir / Transaksi Belanja Baru")
            print("3. 📦 Manajemen Inventaris Toko (Restock Barang)")
            print("4. 💵 Informasi Laci Kasir & Jejak Audit Logger")
            print("5. 🚪 Keluar dari Aplikasi")
            pilihan = input("\nSilakan pilih menu [1-5]: ").strip()

            if pilihan == "1":
                self.menu_lihat_katalog()
                input("\nTekan Enter untuk kembali ke menu utama...")
            elif pilihan == "2":
                self.menu_transaksi_kasir()
                input("\nTekan Enter untuk kembali ke menu utama...")
            elif pilihan == "3":
                self.menu_restock_inventaris()
                input("\nTekan Enter untuk kembali ke menu utama...")
            elif pilihan == "4":
                self.menu_audit_dan_laci()
                input("\nTekan Enter untuk kembali ke menu utama...")
            elif pilihan == "5":
                print("\n[Sistem] Menutup aplikasi kasir SmartPOS. Selamat beristirahat!")
                break
            else:
                print("[Peringatan] Pilihan tidak valid, silakan ketik angka 1 sampai 5.")


if __name__ == "__main__":
    app = SmartPOSApp()
    if "--demo" in sys.argv or "--simulasi" in sys.argv:
        app.jalankan_demo_otomatis()
    else:
        app.mulai()
