# ==============================================================================
# MODUL 13: DESIGN PATTERNS - BAGIAN 2: FACTORY METHOD & STRATEGY PATTERNS
# ==============================================================================
# File: 02_factory_dan_strategy.py
# Deskripsi: Penerapan Factory Method dengan Registry Dictionary modern dan
#            Strategy Pattern dengan pergantian algoritma dinamis saat runtime.
# ==============================================================================

import sys
from abc import ABC, abstractmethod
from typing import Dict, Any, Type

# Konfigurasi terminal agar output UTF-8 berjalan mulus di Windows PowerShell
if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass


# ==============================================================================
# BAGIAN 1: FACTORY METHOD PATTERN (CREATIONAL)
# ==============================================================================
print("=" * 70)
print("1. FACTORY METHOD PATTERN (EKSPORTIR DOKUMEN LAPORAN)")
print("=" * 70)

# 1.1 Interface / Abstraksi Produk
class EksportirDokumen(ABC):
    """Interface untuk seluruh jenis format eksportir."""
    @abstractmethod
    def ekspor(self, nama_laporan: str, data: Dict[str, Any]) -> str:
        """Mengonversi data laporan ke format spesifik."""
        pass


# 1.2 Produk Konkret 1: PDF
class EksportirPDF(EksportirDokumen):
    def ekspor(self, nama_laporan: str, data: Dict[str, Any]) -> str:
        return f"[PDF] '{nama_laporan}.pdf' berhasil digenerate dengan layout cetak A4. Total Baris: {len(data)}"


# 1.3 Produk Konkret 2: CSV
class EksportirCSV(EksportirDokumen):
    def ekspor(self, nama_laporan: str, data: Dict[str, Any]) -> str:
        baris_csv = ",".join(data.keys())
        return f"[CSV] '{nama_laporan}.csv' berhasil dibuat dengan pemisah koma: ({baris_csv})"


# 1.4 Produk Konkret 3: Excel (XLSX)
class EksportirExcel(EksportirDokumen):
    def ekspor(self, nama_laporan: str, data: Dict[str, Any]) -> str:
        return f"[EXCEL] '{nama_laporan}.xlsx' berhasil diekspor dengan multi-sheet & formula."


# 1.5 Factory Modern dengan Dictionary Registry (Bebas if-elif panjang!)
class EksportirFactory:
    """
    Factory yang mengelola registrasi kelas produk.
    Jika ada format baru (misal: JSON, XML), kita cukup mendaftarkannya
    tanpa merusak logika yang sudah ada (Open/Closed Principle).
    """
    _registry: Dict[str, Type[EksportirDokumen]] = {}

    @classmethod
    def daftarkan_format(cls, format_tipe: str, kelas_eksportir: Type[EksportirDokumen]):
        """Mendaftarkan eksportir baru ke dalam katalog factory."""
        cls._registry[format_tipe.lower()] = kelas_eksportir

    @classmethod
    def buat_eksportir(cls, format_tipe: str) -> EksportirDokumen:
        """Membuat instance eksportir berdasarkan jenis format yang diminta."""
        kunci = format_tipe.lower()
        kelas_eksportir = cls._registry.get(kunci)
        if not kelas_eksportir:
            format_tersedia = ", ".join(cls._registry.keys())
            raise ValueError(
                f"Format eksportir '{format_tipe}' tidak dikenali! Format yang tersedia: [{format_tersedia}]"
            )
        return kelas_eksportir()


# Daftarkan format-format standar ke Factory
EksportirFactory.daftarkan_format("pdf", EksportirPDF)
EksportirFactory.daftarkan_format("csv", EksportirCSV)
EksportirFactory.daftarkan_format("excel", EksportirExcel)

# Simulasi Client: Meminta Factory mengekspor laporan
data_penjualan = {"Total": 15000000, "Transaksi": 45, "Kasir": "Siti"}

print("\n--- Simulasi Client Meminta Dokumen Lewat Factory ---")
for format_pilihan in ["pdf", "csv", "excel"]:
    # Client sama sekali TIDAK PERLU tahu class 'EksportirPDF' atau 'EksportirCSV'
    eksportir = EksportirFactory.buat_eksportir(format_pilihan)
    hasil = eksportir.ekspor("Laporan_Keuangan_Januari", data_penjualan)
    print(hasil)


# ==============================================================================
# BAGIAN 2: STRATEGY PATTERN (BEHAVIORAL)
# ==============================================================================
print("\n" + "=" * 70)
print("2. STRATEGY PATTERN (KALKULATOR ONGKOS KIRIM FLEKSIBEL)")
print("=" * 70)

# 2.1 Interface Strategi
class StrategiOngkir(ABC):
    """Interface untuk seluruh algoritma perhitungan ongkos kirim."""
    @abstractmethod
    def hitung_ongkir(self, berat_kg: float, jarak_km: float) -> int:
        pass

    @abstractmethod
    def estimasi_sampai(self) -> str:
        pass


# 2.2 Strategi Konkret: Reguler
class OngkirReguler(StrategiOngkir):
    def hitung_ongkir(self, berat_kg: float, jarak_km: float) -> int:
        # Tarif dasar: Rp 8.000 per kg + Rp 500 per km
        return int(8000 * max(1.0, berat_kg) + (jarak_km * 500))

    def estimasi_sampai(self) -> str:
        return "2 - 3 Hari Kerja"


# 2.3 Strategi Konkret: Express Next Day
class OngkirExpress(StrategiOngkir):
    def hitung_ongkir(self, berat_kg: float, jarak_km: float) -> int:
        # Tarif dasar premium: Rp 18.000 per kg + Rp 1.000 per km
        return int(18000 * max(1.0, berat_kg) + (jarak_km * 1000))

    def estimasi_sampai(self) -> str:
        return "Besok Pasti Sampai (Next Day)"


# 2.4 Strategi Konkret: Same-Day Instant Kurir
class OngkirSameDay(StrategiOngkir):
    def hitung_ongkir(self, berat_kg: float, jarak_km: float) -> int:
        # Flat rate instan + biaya kilometer
        return int(25000 + (jarak_km * 2500))

    def estimasi_sampai(self) -> str:
        return "Hari Ini (3 - 6 Jam)"


# 2.5 Context: Kelas yang Menggunakan Strategi (Kalkulator Checkout)
class PesananCheckout:
    """
    Context yang memegang objek strategi ongkos kirim.
    Strategi dapat diganti secara instan saat runtime (misal ketika user memilih opsi kurir di UI).
    """
    def __init__(self, id_pesanan: str, total_belanja: int, berat_kg: float, jarak_km: float, strategi: StrategiOngkir):
        self.id_pesanan = id_pesanan
        self.total_belanja = total_belanja
        self.berat_kg = berat_kg
        self.jarak_km = jarak_km
        self._strategi = strategi

    def set_strategi(self, strategi_baru: StrategiOngkir):
        """Mengganti algoritma perhitungan ongkir secara dinamis."""
        print(f"\n[Sistem] Mengganti opsi kurir ke: {strategi_baru.__class__.__name__}...")
        self._strategi = strategi_baru

    def rincian_tagihan(self):
        biaya_ongkir = self._strategi.hitung_ongkir(self.berat_kg, self.jarak_km)
        total_akhir = self.total_belanja + biaya_ongkir
        print("-" * 55)
        print(f"Rincian Pesanan     : {self.id_pesanan}")
        print(f"Subtotal Barang     : Rp {self.total_belanja:,}")
        print(f"Ongkos Kirim        : Rp {biaya_ongkir:,} (Estimasi: {self._strategi.estimasi_sampai()})")
        print(f"TOTAL AKHIR BAYAR   : Rp {total_akhir:,}")
        print("-" * 55)


# Simulasi Penggunaan di Runtime
print("\n--- User Checkout: Default Memilih Kurir Reguler ---")
order = PesananCheckout(
    id_pesanan="TRX-9988",
    total_belanja=250000,
    berat_kg=2.5,
    jarak_km=15.0,
    strategi=OngkirReguler()
)
order.rincian_tagihan()

print("\n--- User Mengubah Keputusan: Butuh Cepat (Pilih Express) ---")
order.set_strategi(OngkirExpress())
order.rincian_tagihan()

print("\n--- User Mengubah Keputusan Lagi: Sangat Mendesak (Pilih Same-Day) ---")
order.set_strategi(OngkirSameDay())
order.rincian_tagihan()

print("\n" + "=" * 70)
print("SELESAI: Factory mempermudah kreasi objek, Strategy melenturkan algoritma!")
print("=" * 70)
