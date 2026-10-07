"""
================================================================================
MODUL 12: PRINSIP S.O.L.I.D UNTUK PEMULA
Berkas 04: Solusi Resmi & Pembahasan Refactoring E-Commerce
================================================================================
STUDI KASUS: REFACTORING SISTEM PEMROSESAN PESANAN E-COMMERCE
================================================================================
"""

import sys
from abc import ABC, abstractmethod

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass


# ==============================================================================
# 1. ABSTRAKSI & IMPLEMENTASI REPOSITORY (SRP & DIP)
# ==============================================================================
class OrderRepository(ABC):
    @abstractmethod
    def simpan(self, order_id: str, amount: int):
        pass


class DatabaseRepository(OrderRepository):
    def simpan(self, order_id: str, amount: int):
        print(f"[DATABASE] Order #{order_id} (Rp {amount:,}) sukses dicatat ke tabel pesanan.")


class CloudCacheRepository(OrderRepository):
    def simpan(self, order_id: str, amount: int):
        print(f"[REDIS CACHE] Order #{order_id} (Rp {amount:,}) dicatat di cache memory.")


# ==============================================================================
# 2. ABSTRAKSI & IMPLEMENTASI METODE PEMBAYARAN (OCP & LSP)
# ==============================================================================
class PaymentMethod(ABC):
    @abstractmethod
    def nama_metode(self) -> str:
        pass

    @abstractmethod
    def bayar(self, amount: int) -> bool:
        pass


class QRISPayment(PaymentMethod):
    def nama_metode(self) -> str:
        return "QRIS ShopeePay/GoPay"

    def bayar(self, amount: int) -> bool:
        print(f"[PAYMENT - QRIS] Menampilkan dynamic QR Code untuk nominal Rp {amount:,}...")
        print("  -> Pembayaran QRIS berhasil diverifikasi instan.")
        return True


class CreditCardPayment(PaymentMethod):
    def __init__(self, nomor_kartu: str):
        self.nomor_kartu = nomor_kartu

    def nama_metode(self) -> str:
        return f"Kartu Kredit (**** {self.nomor_kartu[-4:]})"

    def bayar(self, amount: int) -> bool:
        print(f"[PAYMENT - CC] Meminta otorisasi 3D Secure ke Bank untuk {self.nama_metode()}...")
        print(f"  -> Transaksi Rp {amount:,} berhasil di-charge.")
        return True


# BUKTI OCP: Menambah metode baru tanpa mengubah 1 baris pun kode lama!
class VirtualAccountPayment(PaymentMethod):
    def nama_metode(self) -> str:
        return "BCA Virtual Account"

    def bayar(self, amount: int) -> bool:
        print(f"[PAYMENT - VA] Tagihan VA senilai Rp {amount:,} berhasil dilunasi.")
        return True


# ==============================================================================
# 3. ABSTRAKSI & IMPLEMENTASI NOTIFIKASI (ISP & DIP)
# ==============================================================================
class NotificationSender(ABC):
    @abstractmethod
    def kirim(self, penerima: str, pesan: str):
        pass


class EmailNotifier(NotificationSender):
    def kirim(self, penerima: str, pesan: str):
        print(f"[NOTIF EMAIL] Mengirim email konfirmasi ke '{penerima}':")
        print(f"  -> Pesan: {pesan}")


class SMSNotifier(NotificationSender):
    def kirim(self, penerima: str, pesan: str):
        print(f"[NOTIF SMS GSM] Mengirim SMS ke '{penerima}': {pesan}")


# ==============================================================================
# 4. KOORDINATOR BISNIS UTAMA: ORDER SERVICE (DIP & SRP)
# ==============================================================================
class OrderService:
    """
    Mematuhi SRP: Hanya bertugas mengoordinasikan alur bisnis checkout.
    Mematuhi DIP: Bergantung penuh pada kontrak abstraksi (Interface), bukan class konkret.
    """
    def __init__(self, repo: OrderRepository, payment: PaymentMethod, notifier: NotificationSender):
        self.repo = repo
        self.payment = payment
        self.notifier = notifier

    def checkout(self, order_id: str, penerima: str, amount: int):
        print(f"\n========================================================")
        print(f"[CHECKOUT START] Memulai proses order: #{order_id}")
        print(f"Metode Pembayaran : {self.payment.nama_metode()}")
        print(f"Total Belanja     : Rp {amount:,}")
        print(f"========================================================")

        # 1. Eksekusi Pembayaran
        sukses = self.payment.bayar(amount)
        if not sukses:
            print("[GAGAL] Pembayaran ditolak. Transaksi dibatalkan.")
            return False

        # 2. Simpan Transaksi ke Repository
        self.repo.simpan(order_id, amount)

        # 3. Kirim Notifikasi ke Pelanggan
        pesan_notif = f"Terima kasih! Pesanan #{order_id} senilai Rp {amount:,} telah berhasil diproses."
        self.notifier.kirim(penerima, pesan_notif)

        print(f"[CHECKOUT COMPLETE] Pesanan #{order_id} selesai 100%!\n")
        return True


# ==============================================================================
# BLOK PENGUJIAN DAN VERIFIKASI MULTI-SKENARIO
# ==============================================================================
if __name__ == "__main__":
    print("=" * 65)
    print("[SOLUSI] PENGUJIAN SISTEM E-COMMERCE ARSITEKTUR S.O.L.I.D")
    print("=" * 65)

    # Repository bersama
    db_utama = DatabaseRepository()

    # SKENARIO 1: Pelanggan A (Bayar QRIS, Notifikasi Email)
    order_app_1 = OrderService(
        repo=db_utama,
        payment=QRISPayment(),
        notifier=EmailNotifier()
    )
    order_app_1.checkout(
        order_id="TRX-QRIS-001",
        penerima="budi.santoso@gmail.com",
        amount=150_000
    )

    # SKENARIO 2: Pelanggan B (Bayar Kartu Kredit, Notifikasi SMS)
    # Bukti DIP & OCP: Komponen tinggal dicopot-pasang seperti balok Lego!
    order_app_2 = OrderService(
        repo=db_utama,
        payment=CreditCardPayment(nomor_kartu="4512-8899-2345-7788"),
        notifier=SMSNotifier()
    )
    order_app_2.checkout(
        order_id="TRX-CC-002",
        penerima="0812-9988-7766",
        amount=1_250_000
    )

    # SKENARIO 3: Pelanggan C (Metode Pembayaran Baru: Virtual Account)
    # Membuktikan Open/Closed Principle: Fitur baru berjalan mulus!
    order_app_3 = OrderService(
        repo=CloudCacheRepository(),
        payment=VirtualAccountPayment(),
        notifier=EmailNotifier()
    )
    order_app_3.checkout(
        order_id="TRX-VA-003",
        penerima="anton.prafanto@cloud.id",
        amount=3_500_000
    )

    print("=" * 65)
    print("[OK] Selesai: Sistem arsitektur S.O.L.I.D terverifikasi dan berjalan sempurna!")
    print("=" * 65)
