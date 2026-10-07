"""
01_instance_vs_class_attr.py
============================
Modul 2: Variabel Milik Siapa? (Instance vs Class Attributes)

File ini mendemonstrasikan:
1. Cara mendefinisikan Class Attribute (milik bersama)
2. Cara mendefinisikan Instance Attribute (milik pribadi)
3. Menggunakan Class Attribute sebagai penghitung (counter) total objek otomatis
"""
import sys

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

print("=" * 60)
print("[DEMO] INSTANCE ATTRIBUTE VS CLASS ATTRIBUTE")
print("=" * 60)

class Siswa:
    # 1. CLASS ATTRIBUTE: Berlaku untuk semua siswa yang bersekolah di sini
    nama_sekolah = "SMA Nusantara 1"
    total_siswa_terdaftar = 0  # Counter pelacak otomatis

    def __init__(self, nama: str, kelas: str):
        # 2. INSTANCE ATTRIBUTE: Melekat khusus pada siswa ini
        self.nama = nama
        self.kelas = kelas
        
        # Setiap kali objek Siswa baru lahir, naikkan total pendaftar di level Class:
        Siswa.total_siswa_terdaftar += 1

    def tampilkan_biodata(self):
        print(f"[SISWA] Nama: {self.nama:<10} | Kelas: {self.kelas:<5} | Sekolah: {Siswa.nama_sekolah}")


# --- PENGUJIAN ---
print("\n--- 1. Kondisi Awal Sebelum Ada Siswa yang Mendaftar ---")
print(f"Total Siswa Terdaftar: {Siswa.total_siswa_terdaftar}")

print("\n--- 2. Siswa Pertama Mendaftar ---")
s1 = Siswa("Budi", "10-IPA")
s1.tampilkan_biodata()
print(f"Total Siswa Sekarang : {Siswa.total_siswa_terdaftar}")

print("\n--- 3. Siswa Kedua & Ketiga Mendaftar ---")
s2 = Siswa("Siti", "10-IPS")
s3 = Siswa("Joko", "10-IPA")
s2.tampilkan_biodata()
s3.tampilkan_biodata()
print(f"Total Siswa Sekarang : {Siswa.total_siswa_terdaftar}")

print("\n--- 4. Mengubah Nilai Class Attribute ---")
print("Kasus: Sekolah berganti nama menjadi 'SMA Unggulan Nusantara'...")
Siswa.nama_sekolah = "SMA Unggulan Nusantara"

print("Cek kembali nama sekolah semua murid:")
s1.tampilkan_biodata()
s2.tampilkan_biodata()
s3.tampilkan_biodata()
print(">>> CUKUP UBAH SATU KALI DI CLASS, SEMUA OBJEK OTOMATIS MENGIKUTI!")

print("\n" + "=" * 60)
print("[OK] Selesai: Class attribute berhasil mengelola data bersama.")
print("=" * 60)
