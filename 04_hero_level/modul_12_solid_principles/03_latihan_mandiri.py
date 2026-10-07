"""
================================================================================
MODUL 12: PRINSIP S.O.L.I.D UNTUK PEMULA
Berkas 03: Lembar Latihan Mandiri (Tantangan Refactoring Arsitektur E-Commerce)
================================================================================
STUDI KASUS: REFACTORING SISTEM PEMROSESAN PESANAN E-COMMERCE

Deskripsi Masalah:
Diberikan sebuah kode warisan (legacy code) yang buruk:
```python
class BadOrderManager:
    def process(self, order_id, amount, payment_type, notify_type):
        # 1. Melanggar OCP: If-elif pembayaran hardcoded
        if payment_type == "QRIS":
            print("Proses QRIS...")
        elif payment_type == "KARTU":
            print("Proses Kartu Kredit...")
            
        # 2. Melanggar SRP & DIP: Notifikasi & Database bercampur aduk
        if notify_type == "EMAIL":
            print("Kirim email...")
        print("Menyimpan ke MySQL database hardcoded...")
```

Tugas Anda:
Lakukan refactoring sistem di atas agar mematuhi seluruh prinsip S.O.L.I.D:

1. [S & D] Pisahkan Penyimpanan Database:
   - Buat interface `OrderRepository(ABC)` dengan method `simpan(order_id, amount)`.
   - Buat implementasi `DatabaseRepository(OrderRepository)`.

2. [O & L] Pisahkan Metode Pembayaran:
   - Buat interface `PaymentMethod(ABC)` dengan method `bayar(amount: int) -> bool`.
   - Buat implementasi `QRISPayment(PaymentMethod)` dan `CreditCardPayment(PaymentMethod)`.

3. [I] Pisahkan Layanan Notifikasi:
   - Buat interface `NotificationSender(ABC)` dengan method `kirim(penerima: str, pesan: str)`.
   - Buat implementasi `EmailNotifier(NotificationSender)` dan `SMSNotifier(NotificationSender)`.

4. [D & S] Buat High-Level Coordinator `OrderService`:
   - Menerima `repo: OrderRepository`, `payment: PaymentMethod`, dan `notifier: NotificationSender`
     melalui constructor (Dependency Injection).
   - Method `checkout(self, order_id: str, penerima: str, amount: int)`.

================================================================================
PETUNJUK:
Lengkapi blok kode dengan tanda [TODO] di bawah ini.
Setelah selesai, jalankan file ini. Jika output sesuai harapan, bandingkan
jawaban Anda dengan '04_solusi_latihan.py'.
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
        # [TODO 1]: Cetak pesan simpan ke database
        pass


# ==============================================================================
# 2. ABSTRAKSI & IMPLEMENTASI METODE PEMBAYARAN (OCP & LSP)
# ==============================================================================
class PaymentMethod(ABC):
    @abstractmethod
    def bayar(self, amount: int) -> bool:
        pass


class QRISPayment(PaymentMethod):
    def bayar(self, amount: int) -> bool:
        # [TODO 2]: Implementasikan pembayaran via QRIS
        pass


class CreditCardPayment(PaymentMethod):
    def bayar(self, amount: int) -> bool:
        # [TODO 3]: Implementasikan pembayaran via Kartu Kredit
        pass


# ==============================================================================
# 3. ABSTRAKSI & IMPLEMENTASI NOTIFIKASI (ISP & DIP)
# ==============================================================================
class NotificationSender(ABC):
    @abstractmethod
    def kirim(self, penerima: str, pesan: str):
        pass


class EmailNotifier(NotificationSender):
    def kirim(self, penerima: str, pesan: str):
        # [TODO 4]: Implementasikan pengiriman notifikasi Email
        pass


class SMSNotifier(NotificationSender):
    def kirim(self, penerima: str, pesan: str):
        # [TODO 5]: Implementasikan pengiriman notifikasi SMS
        pass


# ==============================================================================
# 4. KOORDINATOR BISNIS: ORDER SERVICE (DIP & SRP)
# ==============================================================================
class OrderService:
    def __init__(self, repo: OrderRepository, payment: PaymentMethod, notifier: NotificationSender):
        # [TODO 6]: Suntikkan (Inject) seluruh dependensi ke dalam instance
        pass

    def checkout(self, order_id: str, penerima: str, amount: int):
        # [TODO 7]: Jalankan pembayaran -> jika sukses simpan ke repo -> kirim notifikasi
        pass


# ==============================================================================
# AREA PENGUJIAN OTOMATIS
# ==============================================================================
if __name__ == "__main__":
    print("=" * 65)
    print("[UJI COBA] REFACTORING SISTEM E-COMMERCE BERBASIS SOLID")
    print("=" * 65)

    print("\nSilakan lengkapi kode di atas, lalu aktifkan kode pengujian di bawah ini:\n")

    # repo = DatabaseRepository()
    # bayar_qris = QRISPayment()
    # notif_email = EmailNotifier()

    # app = OrderService(repo=repo, payment=bayar_qris, notifier=notif_email)
    # app.checkout("ORD-991", "andi@mail.com", 250_000)
