"""
01_dasar_polymorphism.py
========================
Modul 5: Pilar 3 – Polymorphism & Filosofi Duck Typing

File ini mendemonstrasikan:
1. Konsep dasar Polymorphism (Satu perintah, beragam tindakan)
2. Loop polimorfik yang elegan tanpa percabangan if-elif
3. Penanganan objek majemuk dalam armada transportasi
"""
import sys

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

print("=" * 60)
print("[DEMO] DASAR POLYMORPHISM (ARMADA TRANSPORTASI)")
print("=" * 60)

# ==============================================================
# 1. KELAS INDUK (KONTRAK PERINTAH BERSAMA)
# ==============================================================
class Kendaraan:
    def __init__(self, nama: str):
        self.nama = nama

    def bergerak(self):
        print(f"[{self.nama}] Kendaraan bergerak maju.")


# ==============================================================
# 2. KELAS-KELAS ANAK DENGAN TINDAKAN SPESIFIK (OVERRIDING)
# ==============================================================
class Mobil(Kendaraan):
    def bergerak(self):
        print(f"[MOBIL {self.nama}] Menggelinding cepat di atas jalan aspal... Ngreeeng!")

class KapalLaut(Kendaraan):
    def bergerak(self):
        print(f"[KAPAL {self.nama}] Membelah ombak di lautan biru... Cuurrrshhh!")

class PesawatTerbang(Kendaraan):
    def bergerak(self):
        print(f"[PESAWAT {self.nama}] Lepas landas dan meluncur menembus awan... Wuuuuzhh!")


# ==============================================================
# 3. KEKUATAN POLYMORPHISM: SATU PERINTAH UNTUK SEMUA
# ==============================================================
armada = [
    Mobil("Sedan Sport"),
    KapalLaut("Kapal Feri Nusantara"),
    PesawatTerbang("Boeing 737"),
    Mobil("Truk Logistik")
]

print("\n--- Memerintahkan Seluruh Armada Bergerak Bersama ---")
# PERHATIKAN: Cukup panggil k.bergerak()!
# Tidak perlu 'if isinstance(k, Mobil)' atau 'elif isinstance(k, Kapal)'!
for kendaraan in armada:
    kendaraan.bergerak()

print("\n" + "=" * 60)
print("[OK] Selesai: Setiap kendaraan tahu cara bergerak dengan karakternya sendiri.")
print("=" * 60)
