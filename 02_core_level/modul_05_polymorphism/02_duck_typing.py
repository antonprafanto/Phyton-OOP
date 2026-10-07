"""
02_duck_typing.py
=================
Modul 5: Pilar 3 – Polymorphism & Filosofi Duck Typing

File ini mendemonstrasikan:
1. Filosofi Duck Typing khas Python
2. Dua cara eksekusi: LBYL (hasattr) vs EAFP (try-except)
3. Python Modern: typing.Protocol (Duck Typing dengan Type Hinting)
"""
import sys
from typing import Protocol

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

print("=" * 60)
print("[DEMO] DUCK TYPING, EAFP, & MODERN PROTOCOL")
print("=" * 60)

# ==============================================================
# 1. EMPAT KELAS TANPA HUBUNGAN INHERITANCE SAMA SEKALI
# ==============================================================
class FileAudioMp3:
    def __init__(self, judul: str):
        self.judul = judul

    def putar(self):
        print(f"[AUDIO] Memainkan lagu '{self.judul}.mp3' melalui speaker...")

class StreamingYoutube:
    def __init__(self, url: str):
        self.url = url

    def putar(self):
        print(f"[YOUTUBE] Melakukan buffer streaming dari URL: {self.url}...")

class DokumenPdf:
    """Objek yang TIDAK punya method putar()!"""
    def __init__(self, nama_file: str):
        self.nama_file = nama_file


# ==============================================================
# 2. GAYA EKSEKUSI 1: LBYL (Look Before You Leap)
# ==============================================================
def putar_gaya_lbyl(media):
    print("\n--- Eksekusi Gaya LBYL (hasattr) ---")
    if hasattr(media, "putar") and callable(media.putar):
        media.putar()
    else:
        print(f"[LBYL DITOLAK] Objek '{type(media).__name__}' tidak punya method putar()!")


# ==============================================================
# 3. GAYA EKSEKUSI 2: EAFP (Gaya Favorit Komunitas Python)
# ==============================================================
def putar_gaya_eafp(media):
    print("\n--- Eksekusi Gaya EAFP (try-except) ---")
    try:
        media.putar()
    except AttributeError:
        print(f"[EAFP DITANGKAP] Objek '{type(media).__name__}' gagal diputar karena tidak punya method putar()!")


# ==============================================================
# 4. PYTHON MODERN: typing.Protocol
# ==============================================================
class BisaDiputar(Protocol):
    """Kontrak bentuk: Objek apa pun yang punya method putar() dianggap kompatibel."""
    def putar(self) -> None:
        ...

def putar_player_modern(media: BisaDiputar):
    media.putar()


# --- PENGUJIAN ---
lagu = FileAudioMp3("Bohemian Rhapsody")
video = StreamingYoutube("https://youtu.be/demo123")
buku = DokumenPdf("Buku_OOP.pdf")

# Uji LBYL
putar_gaya_lbyl(lagu)
putar_gaya_lbyl(buku)

# Uji EAFP
putar_gaya_eafp(video)
putar_gaya_eafp(buku)

# Uji Modern Protocol
print("\n--- Eksekusi Player Modern (typing.Protocol) ---")
putar_player_modern(lagu)
putar_player_modern(video)

print("\n" + "=" * 60)
print("[OK] Selesai: Duck Typing, EAFP, dan typing.Protocol terkuasai.")
print("=" * 60)
