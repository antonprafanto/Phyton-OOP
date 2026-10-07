"""
03_latihan_mandiri.py
=====================
Modul 4: Pilar 2 – Inheritance (Pewarisan Sifat & DRY)

TANTANGAN PRAKTEK: SISTEM STRUKTUR KARYAWAN KANTOR 👔🏢

Skenario:
Sebuah perusahaan konsultan IT memiliki beragam peran karyawan:
Semua orang adalah 'Karyawan', tetapi 'Programmer' dan 'Manager'
memiliki tugas serta skema bonus yang berbeda!

KETENTUAN YANG HARUS ANDA BUAT:

1. KELAS INDUK (Karyawan):
   - __init__: nama: str, id_karyawan: str, gaji_pokok: int
   - tampilkan_profil(): mencetak ID, nama, dan gaji pokok
   - hitung_gaji_total(): mengembalikan nilai gaji_pokok

2. KELAS ANAK 1 (Programmer):
   - Mewarisi Karyawan
   - __init__: gunakan super() untuk nama, id_karyawan, gaji_pokok.
               tambahkan atribut khusus: bahasa_utama: str, bonus_proyek: int
   - hitung_gaji_total(): menimpa (override) fungsi induk!
                          Gaji total = gaji_pokok + bonus_proyek
   - koding(): mencetak bahwa programmer sedang ngoding dalam bahasa_utama

3. KELAS ANAK 2 (Manager):
   - Mewarisi Karyawan
   - __init__: gunakan super() untuk nama, id_karyawan, gaji_pokok.
               tambahkan atribut khusus: tunjangan_manajerial: int, daftar_tim: list (list kosong di awal)
   - hitung_gaji_total(): Gaji total = gaji_pokok + tunjangan_manajerial
   - rekrut_anggota(karyawan: Karyawan): menambahkan objek karyawan ke dalam daftar_tim

Instruksi:
Lengkapi bagian TODO di bawah ini. Kunci jawaban tersedia di '03_solusi_latihan.py'.
"""
import sys

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# ==============================================================
# 1. KELAS INDUK
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
        # TODO 1: Panggil super().__init__ untuk mengurus data karyawan umum
        # TODO 2: Pasang atribut bahasa_utama dan bonus_proyek
        pass

    def hitung_gaji_total(self) -> int:
        # TODO 3: Kembalikan gaji_pokok + bonus_proyek
        pass

    def koding(self):
        # TODO 4: Cetak aksi koding
        pass


# ==============================================================
# 3. KELAS ANAK 2: MANAGER
# ==============================================================
class Manager(Karyawan):
    def __init__(self, nama: str, id_karyawan: str, gaji_pokok: int, tunjangan: int):
        # TODO 5: Panggil super().__init__
        # TODO 6: Pasang tunjangan dan siapkan self.daftar_tim = []
        pass

    def hitung_gaji_total(self) -> int:
        # TODO 7: Kembalikan gaji_pokok + tunjangan
        pass

    def rekrut_anggota(self, karyawan: Karyawan):
        # TODO 8: Masukkan karyawan ke self.daftar_tim dan cetak pesan
        pass


# --- PENGUJIAN KODE ANDA ---
if __name__ == "__main__":
    print("=" * 60)
    print("[TEST] MENGUJI STRUKTUR KARYAWAN KANTOR")
    print("=" * 60)

    # 1. Buat Programmer
    prog = Programmer("Anton", "DEV-01", 10_000_000, "Python", 3_500_000)
    prog.tampilkan_profil()
    prog.koding()
    print(f"Total Gaji Masuk: Rp {prog.hitung_gaji_total():,}")

    # 2. Buat Manager
    print("\n--- Data Manager ---")
    mgr = Manager("Pak Budi", "MGR-01", 15_000_000, 5_000_000)
    mgr.tampilkan_profil()
    print(f"Total Gaji Masuk: Rp {mgr.hitung_gaji_total():,}")

    # 3. Manager merekrut Programmer
    print("\n--- Manajemen Tim ---")
    mgr.rekrut_anggota(prog)
    print("=" * 60)
