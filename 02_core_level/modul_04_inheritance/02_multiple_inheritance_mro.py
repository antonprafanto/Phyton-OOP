"""
02_multiple_inheritance_mro.py
==============================
Modul 4: Pilar 2 – Inheritance (Pewarisan Sifat & DRY)

File ini mendemonstrasikan:
1. Multiple Inheritance di Python (mewarisi banyak induk sekaligus)
2. Masalah Berlian (Diamond Problem)
3. Cara Python menyelesaikan urutan pencarian dengan MRO (Method Resolution Order)
"""
import sys

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

print("=" * 60)
print("[DEMO] MULTIPLE INHERITANCE & MRO (METHOD RESOLUTION ORDER)")
print("=" * 60)

# ==============================================================
# 1. CONTOH DASAR: BEBEK DENGAN DUA KEMAMPUAN INDUK
# ==============================================================
class KemampuanTerbang:
    def aksi_terbang(self):
        print("[TERBANG] Mengepakkan sayap dan terbang di langit!")

class KemampuanBerenang:
    def aksi_berenang(self):
        print("[BERENANG] Mendayung kaki dan meluncur di atas air!")

class Bebek(KemampuanTerbang, KemampuanBerenang):
    def __init__(self, nama: str):
        self.nama = nama

    def bersuara(self):
        print(f"[{self.nama}] Kweeeek kweeeek!")

donald = Bebek("Donald")
print("\n--- 1. Bebek Mewarisi 2 Kemampuan Induk Sekaligus ---")
donald.bersuara()
donald.aksi_terbang()
donald.aksi_berenang()

# ==============================================================
# 2. BEDAH KASUS: DIAMOND PROBLEM & MRO
# ==============================================================
print("\n" + "-" * 60)
print("[BEDAH KASUS] KASUS PERCABANGAN DIAMOND PROBLEM")
print("-" * 60)

class KakekA:
    def sapa(self):
        print("Sapaan dari: Kakek A")

class AyahB(KakekA):
    def sapa(self):
        print("Sapaan dari: Ayah B")

class IbuC(KakekA):
    def sapa(self):
        print("Sapaan dari: Ibu C")

# Anak mewarisi AyahB lalu IbuC:
class AnakD(AyahB, IbuC):
    pass

anak = AnakD()
print("Siapa yang disapa saat 'anak.sapa()' dipanggil?")
anak.sapa()  # Akan memanggil AyahB karena ditulis lebih dulu di tanda kurung!

# --- MELIHAT URUTAN MRO SECARA NYATA ---
print("\n--- Melihat Jalur Pencarian MRO Python (Class.mro()) ---")
for urutan, cls in enumerate(AnakD.mro(), start=1):
    print(f"Prioritas {urutan}: {cls.__name__}")

print("\n>>> KESIMPULAN MRO:")
print("Python mencari dari kiri ke kanan:")
print("1. Cek di AnakD -> 2. Cek di AyahB -> 3. Cek di IbuC -> 4. Cek di KakekA -> 5. object")
print("Semua teratur dan bebas dari konflik percabangan!")

print("\n" + "=" * 60)
print("[OK] Selesai: Multiple Inheritance & MRO dipahami dengan jelas.")
print("=" * 60)
