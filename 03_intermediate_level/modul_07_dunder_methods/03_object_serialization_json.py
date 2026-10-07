"""
03_object_serialization_json.py
===============================
Modul 7: Python Superpowers – Dunder Methods & Serialisasi JSON

File ini mendemonstrasikan:
1. Cara mengubah objek hidup di RAM menjadi file JSON permanen (Serialization)
2. Cara membaca file JSON dan melahirkan kembali objeknya di memori (Deserialization)
3. Pola standar industri: to_dict() dan @classmethod from_dict()
"""
import sys
import json
import os

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

print("=" * 60)
print("[DEMO] OBJECT SERIALIZATION: MENYIMPAN OBJEK KE JSON")
print("=" * 60)

class ProfilGamer:
    def __init__(self, username: str, level: int, skor: int, item_inventory: list):
        self.username = username
        self.level = level
        self.skor = skor
        self.item_inventory = item_inventory

    def __str__(self) -> str:
        return f"Gamer '{self.username}' | Lvl {self.level} | Skor: {self.skor:,} | Items: {len(self.item_inventory)}"

    # 1. SERIALISASI: Ubah objek menjadi Dictionary Python murni
    def to_dict(self) -> dict:
        return {
            "username": self.username,
            "level": self.level,
            "skor": self.skor,
            "item_inventory": self.item_inventory
        }

    # 2. DESERIALISASI: Buat objek baru dari Dictionary hasil baca file
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            username=data["username"],
            level=data["level"],
            skor=data["skor"],
            item_inventory=data["item_inventory"]
        )


# --- PENGUJIAN ---
FILE_DATA = "saved_game_profile.json"

print("\n--- 1. Membuat Objek Karakter di RAM ---")
player_anton = ProfilGamer(
    username="anton_vibe",
    level=42,
    skor=158_900,
    item_inventory=["Pedang Naga", "Armor Emas", "Ramuan HP x5"]
)
print(f"Data Objek Awal: {player_anton}")

print("\n--- 2. Menyimpan Objek ke Harddisk (File JSON) ---")
# Mengubah objek ke dictionary lalu menyimpan ke file:
with open(FILE_DATA, "w", encoding="utf-8") as file:
    json.dump(player_anton.to_dict(), file, indent=4)
print(f"[BERHASIL] Objek berhasil disimpan ke file '{FILE_DATA}'.")

print("\n--- 3. Simulasi: Program Dimatikan & Objek Dihapus dari RAM ---")
del player_anton  # Menghapus objek dari memori
try:
    print(player_anton)
except NameError:
    print("[HAPUS] Objek 'player_anton' sudah musnah dari RAM komputer!")

print("\n--- 4. Memulihkan Kembali Objek dari File JSON ---")
with open(FILE_DATA, "r", encoding="utf-8") as file:
    data_kamus = json.load(file)
    player_pulih = ProfilGamer.from_dict(data_kamus)

print(f"Data Objek Pulih: {player_pulih}")
print(f"Username : {player_pulih.username}")
print(f"Level    : {player_pulih.level}")
print(f"Barang   : {', '.join(player_pulih.item_inventory)}")
print(">>> OBJEK BERHASIL LAHIR KEMBALI DENGAN DATA PERSIS SEPERTI SEBELUMNYA!")

# Bersihkan file sampah eksperimen setelah pengujian selesai:
if os.path.exists(FILE_DATA):
    os.remove(FILE_DATA)

print("\n" + "=" * 60)
print("[OK] Selesai: Teknik serialisasi objek ke JSON berhasil dikuasai.")
print("=" * 60)
