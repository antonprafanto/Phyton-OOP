"""
02_duck_typing.py
=================
Modul 5: Pilar 3 – Polymorphism & Filosofi Duck Typing

File ini mendemonstrasikan:
1. Filosofi Duck Typing khas Python:
   "Jika dia berjalan seperti bebek dan bersuara seperti bebek, maka dia adalah bebek!"
2. Polymorphism TANPA ikatan Inheritance sama sekali
3. Pemeriksaan fleksibel dengan hasattr() vs EAFP (try-except)
"""
import sys

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

print("=" * 60)
print("[DEMO] DUCK TYPING (POLYMORPHISM TANPA INHERITANCE)")
print("=" * 60)

# ==============================================================
# EMPAT KELAS YANG SAMA SEKALI TIDAK PUNYA HUBUNGAN KELUARGA / INDUK
# ==============================================================
class FileAudioMp3:
    def __init__(self, judul: str):
        self.judul = judul

    def putar(self):
        print(f"[AUDIO] Memainkan lagu '{self.judul}.mp3' melalui speaker stereo...")

class FileVideoMp4:
    def __init__(self, judul: str):
        self.judul = judul

    def putar(self):
        print(f"[VIDEO] Menampilkan video HD '{self.judul}.mp4' di layar monitor...")

class StreamingYoutube:
    def __init__(self, url: str):
        self.url = url

    def putar(self):
        print(f"[YOUTUBE] Melakukan buffer streaming dari URL: {self.url}...")

class DokumenPdf:
    """Objek yang TIDAK punya method putar()!"""
    def __init__(self, nama_file: str):
        self.nama_file = nama_file

    def baca_halaman(self):
        print(f"[PDF] Membaca halaman dokumen {self.nama_file}...")


# ==============================================================
# APLIKASI PEMUTAR MEDIA (MEDIA PLAYER ENGINE)
# ==============================================================
def putar_media(sumber_media):
    """
    Fungsi ini tidak peduli 'sumber_media' turunan siapa!
    Asalkan dia punya method putar(), jalankan! (Duck Typing)
    """
    if hasattr(sumber_media, "putar") and callable(sumber_media.putar):
        sumber_media.putar()
    else:
        print(f"[TOLAK] Objek bertipe '{type(sumber_media).__name__}' tidak bisa diputar!")


# --- PENGUJIAN ---
daftar_antrian = [
    FileAudioMp3("Bohemian Rhapsody"),
    FileVideoMp4("Tutorial_Python_OOP"),
    StreamingYoutube("https://youtube.com/watch?v=12345"),
    DokumenPdf("Ebook_Panduan.pdf")  # Ini bukan media yang bisa diputar
]

print("\n--- Memulai Pemutaran Beragam Media ---")
for item in daftar_antrian:
    putar_media(item)

print("\n" + "=" * 60)
print("[OK] Selesai: Duck Typing berhasil memproses objek beragam bentuk secara dinamis.")
print("=" * 60)
