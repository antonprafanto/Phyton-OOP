"""
03_solusi_latihan.py
====================
Modul 2: Variabel Milik Siapa? (Instance vs Class Attributes)

Kunci Jawaban & Pembahasan Latihan Sistem Karyawan Perusahaan 🏢
"""
import sys

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

class Karyawan:
    # 1. CLASS ATTRIBUTE (Berlaku seragam untuk seluruh karyawan)
    nama_perusahaan = "PT Tech Inovasi"
    gaji_minimum = 5_000_000
    total_karyawan = 0

    def __init__(self, nama: str, jabatan: str, gaji_tawaran: int):
        # 2. INSTANCE ATTRIBUTE (Milik pribadi karyawan ini)
        self.nama = nama
        self.jabatan = jabatan
        
        # Validasi bisnis: Gaji tidak boleh di bawah standar minimum perusahaan
        self.gaji = max(Karyawan.gaji_minimum, gaji_tawaran)

        # 3. Rekrutmen baru: Tambah total karyawan di level Class
        Karyawan.total_karyawan += 1

    def tampilkan_slip(self):
        print(f"[SLIP] Perusahaan : {Karyawan.nama_perusahaan}")
        print(f"       Karyawan   : {self.nama:<10} | Jabatan: {self.jabatan:<18} | Gaji: Rp {self.gaji:,}")

    def naikkan_gaji(self, persen: int):
        kenaikan = int(self.gaji * (persen / 100))
        self.gaji += kenaikan
        print(f"[PROMOSI] Gaji {self.nama} naik {persen}% (+Rp {kenaikan:,})!")


# --- PENGUJIAN SOLUSI ---
if __name__ == "__main__":
    print("=" * 60)
    print("[OK] HASIL EKSEKUSI KUNCI JAWABAN SISTEM KARYAWAN")
    print("=" * 60)

    print(f"Total Karyawan di Awal: {Karyawan.total_karyawan}")

    # 1. Karyawan 1 (Gaji 8 juta -> tetap 8 juta)
    print("\n--- Perekrutan Karyawan 1 ---")
    k1 = Karyawan("Anton", "Backend Developer", 8_000_000)
    k1.tampilkan_slip()

    # 2. Karyawan 2 (Gaji 3 juta ditolak -> disesuaikan ke UMR 5 juta)
    print("\n--- Perekrutan Karyawan 2 ---")
    k2 = Karyawan("Budi", "Junior Support", 3_000_000)
    k2.tampilkan_slip()

    # 3. Karyawan 3
    print("\n--- Perekrutan Karyawan 3 ---")
    k3 = Karyawan("Siti", "UI/UX Designer", 6_500_000)
    k3.tampilkan_slip()

    # 4. Cek total karyawan yang terdaftar
    print(f"\n[INFO] Total Karyawan Terdaftar: {Karyawan.total_karyawan} orang")

    # 5. Promosi kenaikan gaji
    print("\n--- Kenaikan Gaji Anton (10%) ---")
    k1.naikkan_gaji(10)
    k1.tampilkan_slip()

    # Gaji Budi dan Siti tidak berubah:
    print(f"Gaji Budi tetap: Rp {k2.gaji:,} (Tidak ikut naik)")
    print(f"Gaji Siti tetap: Rp {k3.gaji:,} (Tidak ikut naik)")
    print("=" * 60)
