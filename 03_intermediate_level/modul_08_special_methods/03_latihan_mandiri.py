"""
================================================================================
MODUL 8: METODE SPESIAL
Berkas 03: Lembar Latihan Mandiri (Tantangan Mahasiswa/Pemula)
================================================================================
STUDI KASUS: SISTEM KASIR & GATEWAY PEMBAYARAN "SMART-PAY"

Deskripsi Tugas:
Anda diminta membangun sistem pencatatan transaksi toko modern. Data transaksi
bisa masuk dari kasir langsung (__init__), pembacaan file log mentah
(@classmethod dari_baris_log), atau integrasi API aplikasi belanja (@classmethod dari_json_api).

Spesifikasi Class `Transaksi`:
1. Class Attributes:
   - `ppn_persen`: int (default 11, artinya 11%)
2. Constructor `__init__(self, id_transaksi: str, total_belanja: int, metode_bayar: str)`:
   - Menyimpan ketiga data tersebut sebagai instance attributes.
3. Instance Methods:
   - `hitung_total_tagihan(self) -> int`:
     Mengembalikan nilai total belanja ditambah PPN (misal: 100.000 + 11% = 111.000).
   - `cetak_struk(self)`:
     Menampilkan ringkasan struk belanja yang memuat ID, Metode, Subtotal, PPN, dan Total Tagihan.
4. Class Methods:
   - `@classmethod def atur_tarif_ppn(cls, persen_baru: int)`:
     Mengubah nilai `ppn_persen` untuk seluruh transaksi.
   - `@classmethod def dari_baris_log(cls, baris_log: str)`:
     Menerima string dengan format `"TRX-901 | 250000 | QRIS"`.
     Memecah string berdasarkan karakter '|', memangkas spasi (.strip()),
     dan melahirkan objek Transaksi baru dengan `cls(...)`.
   - `@classmethod def dari_json_api(cls, payload: dict)`:
     Menerima dictionary: `{"order_id": "TRX-888", "amount": 500000, "channel": "KARTU_KREDIT"}`
     dan melahirkan objek Transaksi baru dengan `cls(...)`.
5. Static Methods:
   - `@staticmethod def validasi_id_transaksi(id_trx: str) -> bool`:
     Memeriksa apakah `id_trx` diawali dengan "TRX-" dan memiliki panjang minimal 7 karakter.
   - `@staticmethod def hitung_diskon(nominal: int, kode_promo: str) -> int`:
     - Jika kode "HEMAT10" -> diskon 10%
     - Jika kode "HEMAT20" -> diskon 20%
     - Jika lainnya -> 0

================================================================================
PETUNJUK:
Lengkapi blok kode dengan tanda [TODO] di bawah ini.
Setelah selesai, jalankan file ini. Jika output sesuai harapan, bandingkan
jawaban Anda dengan '04_solusi_latihan.py'.
================================================================================
"""

import sys

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass


class Transaksi:
    # [TODO 1]: Tentukan Class Attribute ppn_persen = 11
    ppn_persen = 11

    def __init__(self, id_transaksi: str, total_belanja: int, metode_bayar: str):
        # [TODO 2]: Simpan parameter ke dalam instance attribute (self)
        pass

    def hitung_total_tagihan(self) -> int:
        # [TODO 3]: Hitung total belanja + PPN (gunakan self.ppn_persen)
        pass

    def cetak_struk(self):
        # [TODO 4]: Tampilkan informasi struk lengkap
        pass

    @classmethod
    def atur_tarif_ppn(cls, persen_baru: int):
        # [TODO 5]: Ubah tarif PPN di level class
        pass

    @classmethod
    def dari_baris_log(cls, baris_log: str):
        # [TODO 6]: Pecah baris_log (pemisah '|'), bersihkan spasi, dan return cls(...)
        pass

    @classmethod
    def dari_json_api(cls, payload: dict):
        # [TODO 7]: Baca keys 'order_id', 'amount', 'channel', dan return cls(...)
        pass

    @staticmethod
    def validasi_id_transaksi(id_trx: str) -> bool:
        # [TODO 8]: Kembalikan True jika diawali 'TRX-' dan len >= 7
        pass

    @staticmethod
    def hitung_diskon(nominal: int, kode_promo: str) -> int:
        # [TODO 9]: Hitung diskon nominal berdasarkan kode promo
        pass

    @staticmethod
    def format_rupiah(angka: int) -> str:
        return f"Rp {angka:,.0f}".replace(",", ".")


# ==============================================================================
# AREA PENGUJIAN OTOMATIS
# ==============================================================================
if __name__ == "__main__":
    print("=" * 65)
    print("[UJI COBA] MENJALANKAN LATIHAN TRANSAKSI SMART-PAY")
    print("=" * 65)

    print("\nSilakan lengkapi kode di atas, lalu jalankan pengujian berikut!\n")

    # Contoh alur jika kode sudah selesai:
    # 1. Validasi ID Transaksi
    # print(Transaksi.validasi_id_transaksi("TRX-101")) # Harus True
    # print(Transaksi.validasi_id_transaksi("INV-999")) # Harus False

    # 2. Transaksi Manual
    # t1 = Transaksi("TRX-101", 100_000, "TUNAI")
    # t1.cetak_struk()

    # 3. Transaksi dari Baris Log
    # t2 = Transaksi.dari_baris_log("TRX-202 | 250000 | QRIS")
    # t2.cetak_struk()

    # 4. Transaksi dari Payload JSON
    # payload = {"order_id": "TRX-303", "amount": 400000, "channel": "DEBIT"}
    # t3 = Transaksi.dari_json_api(payload)
    # t3.cetak_struk()
