"""
02_abstract_property.py
=======================
Modul 6: Pilar 4 – Abstraction (Menyembunyikan Kerumitan dengan abc)

File ini mendemonstrasikan:
1. Kombinasi decorator @property + @abstractmethod (Abstract Property)
2. Memaksa seluruh kelas anak wajib mendefinisikan properti tertentu
3. Studi kasus: Tarif Kendaraan Transportasi Umum
"""
import sys
from abc import ABC, abstractmethod

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

print("=" * 60)
print("[DEMO] ABSTRACT PROPERTY (@property + @abstractmethod)")
print("=" * 60)

# ==============================================================
# 1. KELAS INDUK ABSTRAK DENGAN ABSTRACT PROPERTY
# ==============================================================
class TransportasiPublik(ABC):
    def __init__(self, nama_armada: str):
        self.nama_armada = nama_armada

    # ABSTRACT PROPERTY: Anak WAJIB mendefinisikan nilai tarif_per_km
    @property
    @abstractmethod
    def tarif_per_km(self) -> int:
        pass

    # Method biasa yang memanfaatkan properti abstrak di atas:
    def hitung_ongkos(self, jarak_km: float) -> int:
        total = int(self.tarif_per_km * jarak_km)
        print(f"[{self.nama_armada}] Jarak {jarak_km} km x Rp {self.tarif_per_km:,}/km -> Total: Rp {total:,}")
        return total


# ==============================================================
# 2. CONCRETE CLASSES DENGAN IMPLEMENTASI PROPERTI
# ==============================================================
class Angkot(TransportasiPublik):
    @property
    def tarif_per_km(self) -> int:
        return 3_000

class TaksiEksekutif(TransportasiPublik):
    @property
    def tarif_per_km(self) -> int:
        return 12_500


# --- PENGUJIAN ---
angkot = Angkot("Angkot Jurusan Pasar")
taksi = TaksiEksekutif("Silver Bird Alphard")

print("\n--- 1. Menghitung Ongkos Perjalanan 10 KM ---")
angkot.hitung_ongkos(10.0)
taksi.hitung_ongkos(10.0)

print("\n--- 2. Eksperimen: Anak yang Lupa Mendefinisikan Abstract Property ---")
class BusKotaLupa(TransportasiPublik):
    pass  # Lupa mendefinisikan properti tarif_per_km!

try:
    bus = BusKotaLupa("TransKota")
except TypeError as err:
    print(f"[DITOLAK] Pesan Error:\n>>> {err}")
    print("Python mendeteksi bahwa BusKotaLupa belum menentukan tarif_per_km!")

print("\n" + "=" * 60)
print("[OK] Selesai: Abstract Property berhasil mewajibkan atribut standar pada anak.")
print("=" * 60)
