"""
03_latihan_mandiri.py
=====================
Modul 2: Variabel Milik Siapa? (Instance vs Class Attributes)

TANTANGAN PRAKTEK: SISTEM KARYAWAN PERUSAHAAN (Employee System) 🏢

Skenario:
Sebuah perusahaan startup teknologi bernama "PT Tech Inovasi" ingin mengelola
data karyawannya.

KETENTUAN YANG HARUS ANDA BUAT DI CLASS 'Karyawan':
1. CLASS ATTRIBUTE (Berlaku untuk semua karyawan):
   - nama_perusahaan: "PT Tech Inovasi"
   - gaji_minimum: 5_000_000 (UMR perusahaan)
   - total_karyawan: 0 (Pelacak jumlah karyawan yang terdaftar)

2. INSTANCE ATTRIBUTE (Data pribadi masing-masing karyawan):
   - nama: str
   - jabatan: str
   - gaji: int (Aturan: Jika input gaji di bawah gaji_minimum perusahaan,
                       maka gaji otomatis disetel ke gaji_minimum!)

3. SETIAP KALI KARYAWAN BARU DIBUAT:
   - Naikkan nilai Karyawan.total_karyawan sebesar +1.

4. METHOD:
   - tampilkan_slip(): mencetak nama perusahaan, nama karyawan, jabatan, dan gaji.
   - naikkan_gaji(persen: int): menaikkan gaji karyawan ini sebesar persen tertentu.

Instruksi:
Lengkapi bagian TODO di bawah ini. Kunci jawaban tersedia di '03_solusi_latihan.py'.
"""
import sys

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

class Karyawan:
    # TODO 1: Definisikan 3 Class Attribute di sini
    nama_perusahaan = "PT Tech Inovasi"
    gaji_minimum = 5_000_000
    total_karyawan = 0

    def __init__(self, nama: str, jabatan: str, gaji_tawaran: int):
        # TODO 2: Simpan nama dan jabatan ke instance (self)
        self.nama = nama
        self.jabatan = jabatan

        # TODO 3: Pastikan gaji tidak boleh di bawah Karyawan.gaji_minimum
        # Petunjuk: gunakan max(Karyawan.gaji_minimum, gaji_tawaran)
        self.gaji = max(Karyawan.gaji_minimum, gaji_tawaran)

        # TODO 4: Naikkan penghitung total karyawan di level Class (+1)
        pass

    def tampilkan_slip(self):
        # TODO 5: Cetak informasi karyawan dengan rapi
        pass

    def naikkan_gaji(self, persen: int):
        # TODO 6: Hitung kenaikan gaji dan tambahkan ke self.gaji
        pass


# --- PENGUJIAN KODE ANDA ---
if __name__ == "__main__":
    print("=" * 60)
    print("[TEST] MENGUJI SISTEM KARYAWAN")
    print("=" * 60)

    print(f"Total Karyawan di Awal: {Karyawan.total_karyawan}")

    # 1. Merekrut karyawan 1 (Gaji di atas minimum)
    k1 = Karyawan("Anton", "Backend Developer", 8_000_000)
    k1.tampilkan_slip()

    # 2. Merekrut karyawan 2 (Gaji di bawah minimum, harus otomatis disesuaikan ke 5.000.000)
    k2 = Karyawan("Budi", "Junior Support", 3_000_000)
    k2.tampilkan_slip()

    # 3. Cek total karyawan yang terdaftar
    print(f"\nTotal Karyawan Saat Ini: {Karyawan.total_karyawan} orang")

    # 4. Kenaikan gaji Anton sebesar 10%
    print("\n--- Promosi Kenaikan Gaji Anton ---")
    k1.naikkan_gaji(10)
    k1.tampilkan_slip()
    print("=" * 60)
