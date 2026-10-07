"""
03_solusi_latihan.py
====================
Modul 4: Pilar 2 – Inheritance (Pewarisan Sifat & DRY)

Kunci Jawaban & Pembahasan Latihan Struktur Karyawan Kantor 👔🏢
"""
import sys

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# ==============================================================
# 1. KELAS INDUK (Karyawan)
# ==============================================================
class Karyawan:
    def __init__(self, nama: str, id_karyawan: str, gaji_pokok: int):
        self.nama = nama
        self.id_karyawan = id_karyawan
        self.gaji_pokok = gaji_pokok

    def tampilkan_profil(self):
        print(f"[{self.id_karyawan}] {self.nama} | Gaji Pokok: Rp {self.gaji_pokok:,}")

    def hitung_gaji_total(self) -> int:
        return self.gaji_pokok


# ==============================================================
# 2. KELAS ANAK 1: PROGRAMMER
# ==============================================================
class Programmer(Karyawan):
    def __init__(self, nama: str, id_karyawan: str, gaji_pokok: int, bahasa_utama: str, bonus_proyek: int):
        # Mendelegasikan inisialisasi data umum kepada orang tua:
        super().__init__(nama, id_karyawan, gaji_pokok)
        self.bahasa_utama = bahasa_utama
        self.bonus_proyek = bonus_proyek

    def hitung_gaji_total(self) -> int:
        # Menimpa (override) rumus gaji untuk menghitung bonus proyek:
        return self.gaji_pokok + self.bonus_proyek

    def koding(self):
        print(f"[KODING] {self.nama} sedang asyik menulis kode menggunakan bahasa {self.bahasa_utama}!")


# ==============================================================
# 3. KELAS ANAK 2: MANAGER
# ==============================================================
class Manager(Karyawan):
    def __init__(self, nama: str, id_karyawan: str, gaji_pokok: int, tunjangan: int):
        super().__init__(nama, id_karyawan, gaji_pokok)
        self.tunjangan = tunjangan
        self.daftar_tim = []  # List tim pribadi di level instance

    def hitung_gaji_total(self) -> int:
        return self.gaji_pokok + self.tunjangan

    def rekrut_anggota(self, karyawan: Karyawan):
        self.daftar_tim.append(karyawan)
        print(f"[REKRUT] {self.nama} merekrut {karyawan.nama} ke dalam timnya!")

    def tampilkan_tim(self):
        print(f"\n📋 Daftar Anggota Tim di Bawah {self.nama}:")
        for idx, k in enumerate(self.daftar_tim, start=1):
            print(f"   {idx}. {k.nama} ({k.id_karyawan}) - Gaji Total: Rp {k.hitung_gaji_total():,}")


# --- PENGUJIAN SOLUSI ---
if __name__ == "__main__":
    print("=" * 60)
    print("[OK] HASIL EKSEKUSI KUNCI JAWABAN KARYAWAN KANTOR")
    print("=" * 60)

    # 1. Buat 2 Orang Programmer
    prog1 = Programmer("Anton", "DEV-01", 10_000_000, "Python", 3_500_000)
    prog2 = Programmer("Dian", "DEV-02", 9_000_000, "JavaScript", 2_000_000)

    prog1.tampilkan_profil()
    prog1.koding()
    print(f"Total Penghasilan Anton: Rp {prog1.hitung_gaji_total():,}")

    # 2. Buat Manager
    print("\n--- Data Manager ---")
    mgr = Manager("Pak Budi", "MGR-01", 15_000_000, 5_000_000)
    mgr.tampilkan_profil()
    print(f"Total Penghasilan Pak Budi: Rp {mgr.hitung_gaji_total():,}")

    # 3. Manager Merekrut Programmer ke Timnya
    print("\n--- Pembentukan Tim Proyek ---")
    mgr.rekrut_anggota(prog1)
    mgr.rekrut_anggota(prog2)

    # 4. Tampilkan Isi Tim
    mgr.tampilkan_tim()
    print("=" * 60)
