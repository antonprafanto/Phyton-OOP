"""
02_jebakan_pemula.py
====================
Modul 1: Melahirkan Objek Pertama (Class, Object, Constructor, & self)

File ini sengaja membedah 3 KESALAHAN PALING POPULER yang sering dialami pemula
beserta penjelasan pesan error yang muncul dari Python.
"""
import sys

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

print("=" * 60)
print("[BEDAH ERROR] 3 JEBAKAN KLASIK PEMULA SAAT BELAJAR OOP")
print("=" * 60)

# -------------------------------------------------------------
# JEBAKAN 1: LUPA MENULIS 'self' DI PARAMETER METHOD
# -------------------------------------------------------------
print("\n[JEBAKAN 1] Lupa menulis 'self' pada fungsi di dalam class:")

class RobotRusak:
    def sapa():  # <-- PERHATIKAN: LUPA MENULIS self DI SINI!
        print("Halo, aku robot!")

robot = RobotRusak()

try:
    # Memanggil method tanpa self di definisinya:
    robot.sapa()
except TypeError as error:
    print(f"  >>> PESAN ERROR DARI PYTHON:\n      {error}")
    print("  >>> PENYEBAB:")
    print("      Python otomatis mengirimkan objek 'robot' ke dalam fungsi sapa().")
    print("      Karena fungsi sapa() tidak punya wadah (self), Python komplain:")
    print("      'takes 0 positional arguments but 1 was given'!")

# -------------------------------------------------------------
# JEBAKAN 2: TYPO PADA '__init__' (HANYA 1 UNDERSCORE: '_init_')
# -------------------------------------------------------------
print("\n" + "-" * 60)
print("[JEBAKAN 2] Typo kurang underscore ('_init_' bukan '__init__'):")

class MahasiswaTypo:
    def _init_(self, nama):  # <-- KURANG 1 UNDERSCORE DI KIRI DAN KANAN!
        self.nama = nama

mhs = MahasiswaTypo()  # Python tidak menjalankan _init_ secara otomatis!

try:
    print(mhs.nama)
except AttributeError as error:
    print(f"  >>> PESAN ERROR DARI PYTHON:\n      {error}")
    print("  >>> PENYEBAB:")
    print("      Python hanya menganggap '__init__' (dua underscore) sebagai constructor.")
    print("      Jika ditulis '_init_', fungsi tersebut dianggap fungsi biasa yang diabaikan.")

# -------------------------------------------------------------
# JEBAKAN 3: LUPA TANDA KURUNG '()' SAAT MEMANGGIL METHOD
# -------------------------------------------------------------
print("\n" + "-" * 60)
print("[JEBAKAN 3] Lupa tanda kurung '()' saat memanggil method:")

class KucingSehat:
    def mengeong(self):
        return "Meoooong!"

kucing = KucingSehat()

print("  Jika dipanggil SALAH tanpa kurung: kucing.mengeong")
hasil_salah = kucing.mengeong
print(f"  >>> Output: {hasil_salah}")
print("      (Yang keluar adalah alamat memori fungsi, BUKAN hasil aksinya!)")

print("\n  Jika dipanggil BENAR dengan kurung: kucing.mengeong()")
hasil_benar = kucing.mengeong()
print(f"  >>> Output: {hasil_benar}")

print("\n" + "=" * 60)
print("[KESIMPULAN] Ingat 3 aturan emas:")
print("1. Selalu pasang 'self' di parameter pertama method.")
print("2. Gunakan dua underscore: '__init__'.")
print("3. Selalu pakai tanda kurung '()' untuk menjalankan aksi method.")
print("=" * 60)
