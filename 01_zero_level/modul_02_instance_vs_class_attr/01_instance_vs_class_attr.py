"""
01_instance_vs_class_attr.py
============================
Modul 2: Variabel Milik Siapa? (Instance vs Class Attributes)

File ini mendemonstrasikan:
1. Cara mendefinisikan Class Attribute (milik bersama) & Konstanta HURUF BESAR
2. Cara mendefinisikan Instance Attribute (milik pribadi)
3. Mengintip isi kantong objek dengan properti sakti __dict__
4. Bedah jebakan "Shadowing" (salah mengubah class attribute lewat objek)
"""
import sys

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

print("=" * 60)
print("[DEMO] INSTANCE ATTRIBUTE VS CLASS ATTRIBUTE & __dict__")
print("=" * 60)

class Siswa:
    # 1. CLASS ATTRIBUTE: Berlaku untuk semua siswa yang bersekolah di sini
    nama_sekolah = "SMA Nusantara 1"
    PAJAK_KOPERASI = 0.05      # Konstanta (huruf besar): Pajak 5%
    total_siswa_terdaftar = 0  # Counter pelacak otomatis

    def __init__(self, nama: str, kelas: str):
        # 2. INSTANCE ATTRIBUTE: Melekat khusus pada siswa ini
        self.nama = nama
        self.kelas = kelas
        
        # Setiap kali objek Siswa baru lahir, naikkan total pendaftar di level Class:
        Siswa.total_siswa_terdaftar += 1

    def tampilkan_biodata(self):
        print(f"[SISWA] Nama: {self.nama:<10} | Kelas: {self.kelas:<5} | Sekolah: {self.nama_sekolah}")


# --- PENGUJIAN ---
print("\n--- 1. Pendaftaran Siswa ---")
s1 = Siswa("Budi", "10-IPA")
s2 = Siswa("Siti", "10-IPS")

s1.tampilkan_biodata()
s2.tampilkan_biodata()
print(f"Total Siswa Terdaftar di Sistem: {Siswa.total_siswa_terdaftar} orang")

# --- MENGINTIP ISI KANTONG DENGAN __dict__ ---
print("\n--- 2. Mengintip Isi Kantong Pribadi Objek (__dict__) ---")
print(f"Isi kantong s1 (Budi) : {s1.__dict__}")
print(f"Isi kantong s2 (Siti) : {s2.__dict__}")
print(">>> LIHAT: 'nama_sekolah' TIDAK ADA di dalam kantong pribadi s1 maupun s2!")
print("    Python otomatis mencarinya ke lemari bersama (Class Siswa)!")

# --- BEDAH JEBAKAN SHADOWING ---
print("\n--- 3. Bedah Jebakan 'Shadowing' (Salah Menimpa Variabel) ---")
print("Skenario Salah: Kita ingin ganti sekolah, tapi menulis lewat s1 (s1.nama_sekolah = 'SMA Garuda'):")
s1.nama_sekolah = "SMA Garuda"  # <-- SHADOWING!

print("\nCek isi kantong s1 sekarang:")
print(f"Isi kantong s1 : {s1.__dict__}  <-- 'nama_sekolah' sekarang masuk ke kantong pribadi!")

print("\nLihat dampaknya ke siswa lain:")
s1.tampilkan_biodata()  # Sekolah Budi berubah jadi SMA Garuda
s2.tampilkan_biodata()  # Sekolah Siti TETAP SMA Nusantara 1!
print(f"Sekolah resmi di Class: {Siswa.nama_sekolah} (TIDAK BERUBAH!)")

# --- CARA BENAR MENGUBAH CLASS ATTRIBUTE ---
print("\n--- 4. Cara Benar Mengubah Class Attribute untuk Semua Siswa ---")
print("Gunakan Nama Class langsung: Siswa.nama_sekolah = 'SMA Unggulan Nasional'")
Siswa.nama_sekolah = "SMA Unggulan Nasional"

print("\nCek kembali s2 (Siti):")
s2.tampilkan_biodata()
print(">>> SITI OTOMATIS BERUBAH MENGIKUTI KELAS!")
print("    (Catatan: Budi tetap tertimpa bayangannya sendiri karena tadi s1.nama_sekolah diubah manual)")

print("\n" + "=" * 60)
print("[OK] Selesai: Arsitektur data Class vs Instance dipahami dengan tuntas.")
print("=" * 60)
