"""
================================================================================
MODUL 12: PRINSIP S.O.L.I.D UNTUK PEMULA
Berkas 02: Praktik Bagian 2 - I (ISP) dan D (DIP)
================================================================================
Tujuan Pembelajaran:
1. Memecah antarmuka raksasa menjadi interface ramping yang spesifik (ISP).
2. Membebaskan modul bisnis dari ketergantungan kaku pada detail teknis konkret (DIP).
3. Menerapkan pola Dependency Injection (DI) yang mudah diuji (testable).
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
# 1. [I] - INTERFACE SEGREGATION PRINCIPLE (ISP)
# Memisahkan interface besar menjadi antarmuka kecil yang relevan.
# ==============================================================================
class Pencetak(ABC):
    @abstractmethod
    def cetak_dokumen(self, dokumen: str):
        pass


class Pemindai(ABC):
    @abstractmethod
    def pindai_dokumen(self) -> str:
        pass


class MesinFaks(ABC):
    @abstractmethod
    def kirim_faks(self, nomor: str, dokumen: str):
        pass


# Perangkat 1: Printer Murah (Hanya bisa mencetak)
class PrinterRumahan(Pencetak):
    def cetak_dokumen(self, dokumen: str):
        print(f"[PRINTER RUMAHAN] Mencetak selembar: '{dokumen}'")


# Perangkat 2: Mesin Kantor Canggih All-in-One (Bisa Cetak & Pindai)
class MesinAllInOneKantor(Pencetak, Pemindai):
    def cetak_dokumen(self, dokumen: str):
        print(f"[OFFICE MULTI] Mencetak kecepatan tinggi: '{dokumen}'")

    def pindai_dokumen(self) -> str:
        hasil_scan = "Scan_Berkas_Laporan_Tahunan.pdf"
        print(f"[OFFICE MULTI] Berhasil memindai dokumen -> File: {hasil_scan}")
        return hasil_scan


# Fungsi client HANYA bergantung pada apa yang dibutuhkannya:
def proses_cetak_laporan(perangkat: Pencetak, judul: str):
    # Tidak peduli apakah perangkat punya scanner atau fax, yang penting bisa mencetak!
    perangkat.cetak_dokumen(judul)


# ==============================================================================
# 2. [D] - DEPENDENCY INVERSION PRINCIPLE (DIP)
# Modul tingkat tinggi (Checkout) bergantung pada Abstraksi, bukan detail teknis.
# ==============================================================================

# --- KONTRAK ABSTRAKSI (INTERFACE) ---
class StorageRepository(ABC):
    @abstractmethod
    def simpan_transaksi(self, order_id: str, total: int):
        pass


class LayananNotifikasi(ABC):
    @abstractmethod
    def kirim_pesan(self, penerima: str, pesan: str):
        pass


# --- IMPLEMENTASI KONKRET 1 (PRODUKSI) ---
class PostgreSQLStorage(StorageRepository):
    def simpan_transaksi(self, order_id: str, total: int):
        print(f"[POSTGRESQL] Menyimpan data order {order_id} (Total: Rp {total:,}) ke cloud server.")


class WhatsAppNotifier(LayananNotifikasi):
    def kirim_pesan(self, penerima: str, pesan: str):
        print(f"[WHATSAPP API] Mengirim WA ke {penerima}: '{pesan}'")


# --- IMPLEMENTASI KONKRET 2 (TESTING / MOCK) ---
class MemoryMockStorage(StorageRepository):
    def __init__(self):
        self.data_tercatat = []

    def simpan_transaksi(self, order_id: str, total: int):
        self.data_tercatat.append((order_id, total))
        print(f"[MOCK RAM] Order {order_id} disimpan sementara di list memori pengujian.")


class ConsoleNotifier(LayananNotifikasi):
    def kirim_pesan(self, penerima: str, pesan: str):
        print(f"[TERMINAL MOCK] Notif untuk {penerima} disimulasikan di konsol.")


# --- MODUL TINGKAT TINGGI (LOGIKA BISNIS UTAMA) ---
class LayananCheckout:
    """
    Perhatikan: LayananCheckout TIDAK meng-import PostgreSQL atau WhatsApp secara kaku!
    Keduanya disuntikkan (Dependency Injection) melalui constructor.
    """
    def __init__(self, storage: StorageRepository, notifier: LayananNotifikasi):
        self.storage = storage          # Bergantung pada abstraksi
        self.notifier = notifier        # Bergantung pada abstraksi

    def checkout(self, order_id: str, pelanggan: str, total: int):
        print(f"\n[CHECKOUT] Memproses pembayaran order {order_id}...")
        # 1. Simpan ke database
        self.storage.simpan_transaksi(order_id, total)
        # 2. Kirim notifikasi bukti bayar
        self.notifier.kirim_pesan(pelanggan, f"Terima kasih! Pembayaran Rp {total:,} untuk {order_id} berhasil.")


# ==============================================================================
# BLOK PENGUJIAN
# ==============================================================================
if __name__ == "__main__":
    print("=" * 65)
    print("[DEMO 1] INTERFACE SEGREGATION PRINCIPLE (ISP)")
    print("=" * 65)

    printer_murah = PrinterRumahan()
    mesin_kantor = MesinAllInOneKantor()

    proses_cetak_laporan(printer_murah, "Laporan_Keuangan_Q1.pdf")
    proses_cetak_laporan(mesin_kantor, "Laporan_Keuangan_Q1.pdf")
    # Mesin kantor bisa memindai tanpa membebani printer rumahan:
    mesin_kantor.pindai_dokumen()

    print("\n" + "=" * 65)
    print("[DEMO 2] DEPENDENCY INVERSION PRINCIPLE (DIP)")
    print("=" * 65)

    # 1. Lingkungan Produksi Asli (PostgreSQL + WhatsApp)
    print("--- 1. Menjalankan di Lingkungan Produksi ---")
    storage_prod = PostgreSQLStorage()
    notif_prod = WhatsAppNotifier()
    checkout_prod = LayananCheckout(storage=storage_prod, notifier=notif_prod)
    checkout_prod.checkout("ORD-881", "0812-3344-5566", 750_000)

    # 2. Lingkungan Unit Testing (Mock Storage + Console Notifier)
    # Sangat mudah ditukar tanpa mengubah satu baris pun kode di LayananCheckout!
    print("\n--- 2. Menjalankan di Lingkungan Unit Test (Tanpa Database Asli) ---")
    mock_db = MemoryMockStorage()
    mock_notif = ConsoleNotifier()
    checkout_test = LayananCheckout(storage=mock_db, notifier=mock_notif)
    checkout_test.checkout("ORD-TEST-001", "tester@test.com", 150_000)

    print("\n" + "=" * 65)
    print("[OK] Selesai: Prinsip ISP dan DIP berhasil dibuktikan.")
    print("=" * 65)
