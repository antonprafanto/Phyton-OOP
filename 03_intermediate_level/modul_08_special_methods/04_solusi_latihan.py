"""
================================================================================
MODUL 8: METODE SPESIAL
Berkas 04: Solusi Resmi & Pembahasan Latihan Mandiri
================================================================================
STUDI KASUS: SISTEM KASIR & GATEWAY PEMBAYARAN "SMART-PAY"
================================================================================
"""

import sys

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass


class Transaksi:
    # --------------------------------------------------------------------------
    # 1. CLASS ATTRIBUTES
    # --------------------------------------------------------------------------
    ppn_persen: int = 11  # Standar PPN nasional Indonesia (11%)

    def __init__(self, id_transaksi: str, total_belanja: int, metode_bayar: str):
        # ----------------------------------------------------------------------
        # 2. INSTANCE ATTRIBUTES
        # ----------------------------------------------------------------------
        if not self.validasi_id_transaksi(id_transaksi):
            raise ValueError(f"ID Transaksi '{id_transaksi}' tidak valid! Harus diawali 'TRX-' dan minimal 7 karakter.")

        self.id_transaksi = id_transaksi
        self.total_belanja = total_belanja
        self.metode_bayar = metode_bayar.upper()

    # --------------------------------------------------------------------------
    # 3. INSTANCE METHODS (Aksi pada Objek Tertentu)
    # --------------------------------------------------------------------------
    def hitung_nilai_ppn(self) -> int:
        """Menghitung nominal rupiah dari PPN."""
        return int(self.total_belanja * (self.ppn_persen / 100))

    def hitung_total_tagihan(self) -> int:
        """Mengembalikan total belanja ditambah nilai PPN."""
        return self.total_belanja + self.hitung_nilai_ppn()

    def cetak_struk(self):
        """Mencetak struk belanja kasir yang rapi dan profesional."""
        subtotal_str = self.format_rupiah(self.total_belanja)
        ppn_str = self.format_rupiah(self.hitung_nilai_ppn())
        total_str = self.format_rupiah(self.hitung_total_tagihan())

        print("+" + "-" * 48 + "+")
        print(f"|            STRUK PEMBAYARAN SMART-PAY          |")
        print("+" + "-" * 48 + "+")
        print(f"| ID Transaksi : {self.id_transaksi:<31} |")
        print(f"| Metode Bayar : {self.metode_bayar:<31} |")
        print(f"| Subtotal     : {subtotal_str:<31} |")
        print(f"| PPN ({self.ppn_persen}%)    : {ppn_str:<31} |")
        print("+" + "-" * 48 + "+")
        print(f"| TOTAL AKHIR  : {total_str:<31} |")
        print("+" + "-" * 48 + "+\n")

    # --------------------------------------------------------------------------
    # 4. CLASS METHODS (Alternative Constructors & Kebijakan Global)
    # --------------------------------------------------------------------------
    @classmethod
    def atur_tarif_ppn(cls, persen_baru: int):
        """Mengubah kebijakan tarif PPN untuk seluruh transaksi sistem."""
        print(f"[KEBIJAKAN FISKAL] Tarif PPN diubah: {cls.ppn_persen}% -> {persen_baru}%")
        cls.ppn_persen = persen_baru

    @classmethod
    def dari_baris_log(cls, baris_log: str):
        """
        Alternative Constructor dari string log berpemisah pipa (|):
        Contoh input: 'TRX-901 | 250000 | QRIS'
        """
        bagian = baris_log.split("|")
        if len(bagian) != 3:
            raise ValueError(f"Format string log salah! Diharapkan 3 kolom dipisah '|', diterima: {len(bagian)}")

        id_trx = bagian[0].strip()
        nominal = int(bagian[1].strip())
        metode = bagian[2].strip()

        # Gunakan 'cls' untuk melahirkan objek baru
        return cls(id_transaksi=id_trx, total_belanja=nominal, metode_bayar=metode)

    @classmethod
    def dari_json_api(cls, payload: dict):
        """
        Alternative Constructor dari format response API / JSON:
        Contoh: {'order_id': 'TRX-888', 'amount': 500000, 'channel': 'KARTU_KREDIT'}
        """
        return cls(
            id_transaksi=payload["order_id"],
            total_belanja=int(payload["amount"]),
            metode_bayar=payload["channel"]
        )

    # --------------------------------------------------------------------------
    # 5. STATIC METHODS (Fungsi Bantuan Murni)
    # --------------------------------------------------------------------------
    @staticmethod
    def validasi_id_transaksi(id_trx: str) -> bool:
        """
        Validasi ID transaksi:
        - Harus diawali dengan 'TRX-'
        - Panjang minimal adalah 7 karakter (misal 'TRX-001')
        """
        if not isinstance(id_trx, str):
            return False
        return id_trx.startswith("TRX-") and len(id_trx) >= 7

    @staticmethod
    def hitung_diskon(nominal: int, kode_promo: str) -> int:
        """Menghitung potongan diskon dari kode voucher."""
        kode_bersih = kode_promo.strip().upper()
        if kode_bersih == "HEMAT10":
            return int(nominal * 0.10)
        elif kode_bersih == "HEMAT20":
            return int(nominal * 0.20)
        return 0

    @staticmethod
    def format_rupiah(angka: int) -> str:
        """Utilitas untuk mencetak format mata uang Rupiah."""
        return f"Rp {angka:,.0f}".replace(",", ".")


# ==============================================================================
# PENGUJIAN KUNCI JAWABAN
# ==============================================================================
if __name__ == "__main__":
    print("=" * 65)
    print("[SOLUSI] PENGUJIAN SISTEM TRANSAKSI SMART-PAY")
    print("=" * 65)

    # 1. Pengujian Static Method: Validasi ID Transaksi
    print("--- 1. Uji Static Method: Validasi ID ---")
    id_valid = "TRX-1001"
    id_salah = "INV-2002"
    print(f"Apakah '{id_valid}' valid? -> {Transaksi.validasi_id_transaksi(id_valid)} (Harus True)")
    print(f"Apakah '{id_salah}' valid? -> {Transaksi.validasi_id_transaksi(id_salah)} (Harus False)\n")

    # 2. Pengujian Static Method: Hitung Diskon
    nominal_tes = 200_000
    diskon10 = Transaksi.hitung_diskon(nominal_tes, "HEMAT10")
    print(f"Diskon untuk nominal {Transaksi.format_rupiah(nominal_tes)} dengan HEMAT10: {Transaksi.format_rupiah(diskon10)}")
    print()

    # 3. Transaksi 1: Melalui __init__ Standar (Kasir Langsung)
    print("--- 2. Transaksi Standar (__init__) ---")
    t1 = Transaksi("TRX-101", 100_000, "Tunai")
    t1.cetak_struk()

    # 4. Transaksi 2: Melalui @classmethod dari Baris Log Mentah
    print("--- 3. Alternative Constructor: dari_baris_log ---")
    log_mentah = "  TRX-202  |  350000  |  qris  "
    t2 = Transaksi.dari_baris_log(log_mentah)
    t2.cetak_struk()

    # 5. Transaksi 3: Melalui @classmethod dari Payload JSON API
    print("--- 4. Alternative Constructor: dari_json_api ---")
    api_data = {
        "order_id": "TRX-303",
        "amount": 750000,
        "channel": "Kartu Kredit"
    }
    t3 = Transaksi.dari_json_api(api_data)
    t3.cetak_struk()

    # 6. Mengubah Tarif PPN Global melalui @classmethod
    print("--- 5. Class Method: Mengubah Kebijakan Tarif PPN ---")
    Transaksi.atur_tarif_ppn(12)  # Misal pemerintah menaikkan PPN ke 12%
    print("\nStruk t3 setelah perubahan PPN global:")
    t3.cetak_struk()

    print("=" * 65)
    print("[OK] Selesai: Seluruh fitur Modul 8 berhasil diuji dengan sempurna!")
    print("=" * 65)
