"""
02_multiple_inheritance_mro.py
==============================
Modul 4: Pilar 2 – Inheritance (Pewarisan Sifat & DRY)

File ini mendemonstrasikan:
1. Multiple Inheritance di Python
2. Penerapan Pola Nyata Industri: Mixin Pattern (LoggerMixin)
3. Masalah Berlian (Diamond Problem) & MRO (Method Resolution Order)
"""
import sys

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

print("=" * 60)
print("[DEMO] MULTIPLE INHERITANCE, MIXIN, & MRO")
print("=" * 60)

# ==============================================================
# 1. POLA INDUSTRI: MIXIN PATTERN (PLUGIN KEMAMPUAN MANDIRI)
# ==============================================================
class LoggerMixin:
    """Mixin untuk memberikan kemampuan mencetak log aktivitas."""
    def catat_log(self, pesan: str):
        print(f"[LOG {self.__class__.__name__}]: {pesan}")

class NotifikasiSmsMixin:
    """Mixin untuk memberikan kemampuan mengirim SMS notifikasi."""
    def kirim_sms(self, nomor: str, pesan: str):
        print(f"[SMS ke {nomor}]: {pesan}")

# Kelas Bisnis Nyata yang memanfaatkan dua Mixin di atas:
class AkunUser(LoggerMixin, NotifikasiSmsMixin):
    def __init__(self, username: str, no_hp: str):
        self.username = username
        self.no_hp = no_hp

    def ganti_password(self, password_baru: str):
        # Memanfaatkan fitur dari LoggerMixin:
        self.catat_log(f"User '{self.username}' berhasil mengganti password.")
        # Memanfaatkan fitur dari NotifikasiSmsMixin:
        self.kirim_sms(self.no_hp, "Keamanan: Password akun Anda baru saja diperbarui.")

print("\n--- 1. Menguji Penerapan Mixin Pattern ---")
user = AkunUser("anton_dev", "08123456789")
user.ganti_password("RahasiaBaru#2026")

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
anak.sapa()  # Memanggil AyahB karena ditulis lebih dulu di parameter class

# --- MELIHAT URUTAN MRO SECARA NYATA ---
print("\n--- Melihat Jalur Pencarian MRO Python (Class.mro()) ---")
for urutan, cls in enumerate(AnakD.mro(), start=1):
    print(f"Prioritas {urutan}: {cls.__name__}")

print("\n>>> KESIMPULAN MRO:")
print("Python mencari dari kiri ke kanan:")
print("1. Cek di AnakD -> 2. Cek di AyahB -> 3. Cek di IbuC -> 4. Cek di KakekA -> 5. object")

print("\n" + "=" * 60)
print("[OK] Selesai: Mixin Pattern & MRO terkuasai dengan mantap.")
print("=" * 60)
