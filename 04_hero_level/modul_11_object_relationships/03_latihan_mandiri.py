"""
================================================================================
MODUL 11: HUBUNGAN ANTAR OBJEK (OBJECT RELATIONSHIPS)
Berkas 03: Lembar Latihan Mandiri (Arsitektur PC & Programmer)
================================================================================
STUDI KASUS: SISTEM SIMULASI PERAKITAN PC & PENGGUNA KOMPUTER

Deskripsi Tugas:
Anda diminta memodelkan sistem perakitan komputer lengkap dengan 3 jenis hubungan:
1. KOMPOSISI: Komputer memiliki komponen inti (Processor dan RAM) yang lahir
   di dalam Komputer.
2. AGREGASI: Komputer memiliki Aksesoris eksternal (Keyboard, Mouse, Monitor) yang
   diciptakan di luar dan bisa dicolok/dicabut kapan saja.
3. ASOSIASI: Programmer menggunakan Komputer untuk menulis kode aplikasi.

Spesifikasi Class yang Harus Dibuat:

1. Class `Processor`:
   - `__init__(self, model: str, speed_ghz: float, cores: int)`
   - `info(self) -> str`

2. Class `RAM`:
   - `__init__(self, kapasitas_gb: int, tipe_ddr: str)`
   - `info(self) -> str`

3. Class `Aksesoris`:
   - `__init__(self, nama: str, jenis: str)` (Contoh: "Logitech MX Master", "Mouse")
   - `__repr__(self) -> str`

4. Class `Komputer`:
   - `__init__(self, nama_pc: str, proc_model: str, proc_ghz: float, proc_cores: int, ram_gb: int, ram_ddr: str)`:
     * KOMPOSISI: Buat objek Processor dan RAM di dalam constructor ini!
     * AGREGASI: Buat list kosong `self.daftar_aksesoris` untuk menampung aksesoris luar.
   - Method `colok_aksesoris(self, aksesoris: Aksesoris)`:
     * Menambahkan aksesoris ke dalam `self.daftar_aksesoris`.
   - Method `cetak_spesifikasi(self)`:
     * Menampilkan spesifikasi Processor, RAM, dan seluruh aksesoris yang terpasang.

5. Class `Programmer`:
   - `__init__(self, nama: str, bahasa: str)`
   - Method ASOSIASI `koding(self, pc: Komputer, nama_proyek: str)`:
     * Menampilkan pesan bahwa programmer sedang menggunakan `pc.nama_pc` untuk
       mengembangkan `nama_proyek` dengan bahasa pemrogramannya.

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


# ==============================================================================
# KOMPONEN INTERNAL (KOMPOSISI)
# ==============================================================================
class Processor:
    def __init__(self, model: str, speed_ghz: float, cores: int):
        # [TODO 1]: Inisialisasi atribut processor
        pass

    def info(self) -> str:
        # [TODO 2]: Kembalikan ringkasan teks processor
        pass


class RAM:
    def __init__(self, kapasitas_gb: int, tipe_ddr: str):
        # [TODO 3]: Inisialisasi atribut RAM
        pass

    def info(self) -> str:
        # [TODO 4]: Kembalikan ringkasan teks RAM
        pass


# ==============================================================================
# KOMPONEN EKSTERNAL (AGREGASI)
# ==============================================================================
class Aksesoris:
    def __init__(self, nama: str, jenis: str):
        # [TODO 5]: Inisialisasi atribut aksesoris
        pass

    def __repr__(self) -> str:
        # [TODO 6]: Format representasi string aksesoris
        pass


# ==============================================================================
# KOMPUTER (WADAH UTAMA: KOMPOSISI + AGREGASI)
# ==============================================================================
class Komputer:
    def __init__(self, nama_pc: str, proc_model: str, proc_ghz: float, proc_cores: int, ram_gb: int, ram_ddr: str):
        self.nama_pc = nama_pc
        # [TODO 7]: Terapkan Komposisi (Instansiasi Processor dan RAM di sini)
        # self.processor = ...
        # self.ram = ...

        # [TODO 8]: Terapkan Agregasi (Wadah list untuk aksesoris)
        # self.daftar_aksesoris = []
        pass

    def colok_aksesoris(self, aksesoris: Aksesoris):
        # [TODO 9]: Masukkan aksesoris ke daftar_aksesoris
        pass

    def cetak_spesifikasi(self):
        # [TODO 10]: Tampilkan rincian PC, Processor, RAM, dan seluruh aksesoris
        pass


# ==============================================================================
# PENGGUNA (ASOSIASI)
# ==============================================================================
class Programmer:
    def __init__(self, nama: str, bahasa: str):
        self.nama = nama
        self.bahasa = bahasa

    def koding(self, pc: Komputer, nama_proyek: str):
        # [TODO 11]: Terapkan Asosiasi (Gunakan pc sebagai alat kerja)
        pass


# ==============================================================================
# AREA PENGUJIAN OTOMATIS
# ==============================================================================
if __name__ == "__main__":
    print("=" * 65)
    print("[UJI COBA] ARSITEKTUR KOMPUTER & PROGRAMMER")
    print("=" * 65)

    print("\nSilakan lengkapi kode di atas, lalu aktifkan kode pengujian di bawah ini:\n")

    # 1. Rakit Komputer (Komposisi internal)
    # pc_gaming = Komputer("Battlestation-Pro", "Intel Core i9-14900K", 5.8, 24, 64, "DDR5")

    # 2. Pasang Aksesoris (Agregasi eksternal)
    # mouse = Aksesoris("Razer DeathAdder", "Mouse")
    # keyboard = Aksesoris("Keychron Q1 Pro", "Mechanical Keyboard")
    # pc_gaming.colok_aksesoris(mouse)
    # pc_gaming.colok_aksesoris(keyboard)
    # pc_gaming.cetak_spesifikasi()

    # 3. Programmer Bekerja (Asosiasi)
    # dev = Programmer("Anton", "Python")
    # dev.koding(pc_gaming, "SmartPOS System")
