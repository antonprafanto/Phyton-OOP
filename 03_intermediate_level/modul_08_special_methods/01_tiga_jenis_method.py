"""
================================================================================
MODUL 8: METODE SPESIAL
Berkas 01: Tiga Jenis Method dalam Python (Instance, Class, & Static)
================================================================================
Tujuan Pembelajaran:
1. Memahami perbedaan sintaks dan penggunaan:
   - Instance Method: Menerima 'self' (bekerja pada satu objek spesifik).
   - Class Method: Menerima 'cls' (bekerja pada tingkat cetakan class).
   - Static Method: Tanpa 'self' dan tanpa 'cls' (fungsi bantuan independen).
2. Membuktikan bagaimana masing-masing method mengakses atau tidak mengakses data.
================================================================================
"""

import sys

# Konfigurasi terminal agar kompatibel dengan encoding Windows / UTF-8
if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass


class Karyawan:
    # -------------------------------------------------------------
    # CLASS ATTRIBUTES (Dimiliki bersama oleh semua karyawan)
    # -------------------------------------------------------------
    nama_perusahaan = "PT Antigravity Digital Solusi"
    standar_kenaikan_persen = 10  # Kenaikan default 10% per tahun

    def __init__(self, nama: str, gaji_pokok: int, posisi: str):
        # ---------------------------------------------------------
        # INSTANCE ATTRIBUTES (Data unik milik masing-masing objek)
        # ---------------------------------------------------------
        self.nama = nama
        self.gaji_pokok = gaji_pokok
        self.posisi = posisi

    # =============================================================
    # 1. INSTANCE METHOD (Default)
    # Ciri: Parameter pertama adalah 'self'.
    # Hak Akses: Bisa membaca & mengubah atribut objek (self.xxx)
    #            dan atribut kelas (self.nama_perusahaan).
    # =============================================================
    def tampilkan_profil(self) -> str:
        gaji_teks = self.format_rupiah(self.gaji_pokok)
        return (
            f"[KARYAWAN] {self.nama} ({self.posisi})\n"
            f"  - Kantor : {self.nama_perusahaan}\n"
            f"  - Gaji   : {gaji_teks}"
        )

    def ajukan_kenaikan_tahunan(self):
        """Menaikkan gaji sebesar standar class attribute."""
        tambahan = int(self.gaji_pokok * (self.standar_kenaikan_persen / 100))
        self.gaji_pokok += tambahan
        print(f"[NAIK GAJI] Gaji {self.nama} naik {self.standar_kenaikan_persen}% "
              f"(+{self.format_rupiah(tambahan)}) -> Total Baru: {self.format_rupiah(self.gaji_pokok)}")

    # =============================================================
    # 2. CLASS METHOD
    # Ciri: Menggunakan dekorator @classmethod, parameter pertama 'cls'.
    # Hak Akses: Hanya bisa mengakses & mengubah tingkat kelas (cls.xxx).
    #            TIDAK BISA mengakses atribut objek individual (self.xxx).
    # =============================================================
    @classmethod
    def ubah_nama_perusahaan(cls, nama_baru: str):
        """Mengubah nama perusahaan untuk SEMUA karyawan sekaligus."""
        print(f"[REBRANDING] Nama perusahaan berganti: '{cls.nama_perusahaan}' -> '{nama_baru}'")
        cls.nama_perusahaan = nama_baru

    @classmethod
    def set_standar_kenaikan(cls, persen_baru: int):
        """Mengatur kebijakan kenaikan gaji pusat."""
        cls.standar_kenaikan_persen = persen_baru
        print(f"[KEBIJAKAN BARU] Standar kenaikan gaji sekarang menjadi {persen_baru}%")

    @classmethod
    def buat_karyawan_magang(cls, nama: str):
        """
        Alternative Constructor:
        Melahirkan karyawan baru dengan peran 'Magang' dan gaji standar 3 juta.
        """
        print(f"[REKRUT MAGANG] Merekrut peserta magang baru: {nama}")
        # Mengembalikan objek baru menggunakan cetakan 'cls'
        return cls(nama=nama, gaji_pokok=3_000_000, posisi="Analis Magang")

    # =============================================================
    # 3. STATIC METHOD
    # Ciri: Menggunakan dekorator @staticmethod, TANPA 'self' & 'cls'.
    # Hak Akses: Fungsi murni (pure function) yang tidak menyentuh
    #            data objek maupun kelas.
    # Alasan di dalam class: Relevan secara konteks dengan domain Karyawan.
    # =============================================================
    @staticmethod
    def format_rupiah(angka: int) -> str:
        """Utilitas untuk memformat angka integer menjadi string Rupiah."""
        return f"Rp {angka:,.0f}".replace(",", ".")

    @staticmethod
    def apakah_hari_kerja(hari_ke: int) -> bool:
        """
        Mengecek apakah hari kerja.
        1: Senin, 2: Selasa, ... 5: Jumat -> True
        6: Sabtu, 7: Minggu -> False
        """
        return 1 <= hari_ke <= 5


# ==============================================================================
# BLOK PENGUJIAN DAN DEMONSTRASI LANGSUNG
# ==============================================================================
if __name__ == "__main__":
    print("=" * 65)
    print("[DEMO 1] INSTANCE METHOD: Bekerja pada Objek Tertentu")
    print("=" * 65)

    budi = Karyawan("Budi Santoso", 8_000_000, "Senior Backend Engineer")
    siti = Karyawan("Siti Rahma", 12_000_000, "Lead Product Manager")

    print(budi.tampilkan_profil())
    print()
    print(siti.tampilkan_profil())
    print()

    # Memanggil instance method yang mengubah atribut milik Budi saja
    budi.ajukan_kenaikan_tahunan()
    # Gaji Siti tidak terpengaruh karena 'self' merujuk ke Budi
    print(f"Gaji Siti tetap: {Karyawan.format_rupiah(siti.gaji_pokok)}")

    print("\n" + "=" * 65)
    print("[DEMO 2] CLASS METHOD: Bekerja pada Level Blueprint / Kebijakan")
    print("=" * 65)

    # 1. Mengubah nama perusahaan lewat Class langsung
    Karyawan.ubah_nama_perusahaan("PT Vibe Super Coding Tbk")

    # Bukti: Semua karyawan (Budi dan Siti) otomatis melihat nama perusahaan baru
    print(f"Perusahaan Budi : {budi.nama_perusahaan}")
    print(f"Perusahaan Siti : {siti.nama_perusahaan}")
    print()

    # 2. Mengubah kebijakan kenaikan gaji menjadi 15%
    Karyawan.set_standar_kenaikan(15)
    siti.ajukan_kenaikan_tahunan()

    # 3. Melahirkan karyawan magang lewat Class Method
    joko_magang = Karyawan.buat_karyawan_magang("Joko Susanto")
    print(joko_magang.tampilkan_profil())

    print("\n" + "=" * 65)
    print("[DEMO 3] STATIC METHOD: Fungsi Bantu / Utilitas Murni")
    print("=" * 65)

    # Static method bisa dipanggil langsung dari nama Class tanpa membuat objek
    angka_tes = 25_750_000
    print(f"Format Angka {angka_tes} -> {Karyawan.format_rupiah(angka_tes)}")

    print(f"Apakah hari ke-3 (Rabu) hari kerja?   : {Karyawan.apakah_hari_kerja(3)}")
    print(f"Apakah hari ke-7 (Minggu) hari kerja? : {Karyawan.apakah_hari_kerja(7)}")

    print("\n" + "=" * 65)
    print("[OK] Selesai: Tiga jenis method berhasil dieksekusi dan dipahami.")
    print("=" * 65)
