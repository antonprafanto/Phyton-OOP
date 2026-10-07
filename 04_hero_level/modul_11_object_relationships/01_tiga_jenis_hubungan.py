"""
================================================================================
MODUL 11: HUBUNGAN ANTAR OBJEK (OBJECT RELATIONSHIPS)
Berkas 01: Praktik Tiga Hubungan - Association, Aggregation, & Composition
================================================================================
Tujuan Pembelajaran:
1. Memahami Asosiasi: Relasi setara 'uses-a' (Dokter menggunakan Pasien).
2. Memahami Agregasi: Relasi wadah 'has-a' lemah (Klub Sepakbola memiliki Pemain).
   Objek anak tetap hidup mandiri jika objek induk dihancurkan.
3. Memahami Komposisi: Relasi kepemilikan mutlak 'part-of' kuat (Mobil memiliki Mesin).
   Objek anak diciptakan di dalam induk dan musnah bersama induk.
================================================================================
"""

import sys

# Konfigurasi terminal agar kompatibel dengan encoding Windows / UTF-8
if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass


# ==============================================================================
# 1. ASOSIASI (ASSOCIATION: 'uses-a')
# Hubungan longgar di mana dua objek independen saling berinteraksi lewat method.
# ==============================================================================
class Pasien:
    def __init__(self, nama: str, keluhan: str):
        self.nama = nama
        self.keluhan = keluhan

    def __repr__(self):
        return f"Pasien(nama='{self.nama}', keluhan='{self.keluhan}')"


class Dokter:
    def __init__(self, nama: str, spesialisasi: str):
        self.nama = nama
        self.spesialisasi = spesialisasi

    # Asosiasi: Objek Pasien diterima sebagai parameter fungsi
    def periksa(self, pasien: Pasien) -> str:
        resep = f"Paracetamol & Istirahat (Untuk keluhan: {pasien.keluhan})"
        print(f"[ASOSIASI] Dr. {self.nama} ({self.spesialisasi}) memeriksa pasien {pasien.nama}.")
        return resep


# ==============================================================================
# 2. AGREGASI (AGGREGATION: 'has-a' Lemah / Whole-Part Independen)
# Objek anak diciptakan DI LUAR dan dimasukkan ke dalam wadah induk.
# Jika induk dihancurkan, anak TETAP HIDUP di RAM.
# ==============================================================================
class Pemain:
    def __init__(self, nama: str, posisi: str):
        self.nama = nama
        self.posisi = posisi

    def __repr__(self):
        return f"Pemain({self.nama}, {self.posisi})"


class KlubSepakbola:
    def __init__(self, nama_klub: str):
        self.nama_klub = nama_klub
        self.skuad: list[Pemain] = []  # Wadah Agregasi

    def rekrut_pemain(self, pemain: Pemain):
        self.skuad.append(pemain)
        print(f"[AGREGASI] {pemain.nama} resmi bergabung dengan {self.nama_klub}.")

    def tampilkan_skuad(self):
        print(f"\n--- Skuad {self.nama_klub} ---")
        for p in self.skuad:
            print(f"  - {p.nama:<15} ({p.posisi})")


# ==============================================================================
# 3. KOMPOSISI (COMPOSITION: 'part-of' Kuat / Keterikatan Mati-Hidup)
# Objek anak diciptakan DI DALAM constructor induk.
# Siklus hidup anak terikat 100% pada induk.
# ==============================================================================
class Mesin:
    def __init__(self, tipe_bahan_bakar: str, tenaga_kuda: int):
        self.tipe_bahan_bakar = tipe_bahan_bakar
        self.tenaga_kuda = tenaga_kuda

    def hidupkan(self):
        return f"Mesin {self.tipe_bahan_bakar} ({self.tenaga_kuda} HP) menyala halus: Bruuummm!"


class Mobil:
    def __init__(self, merk: str, bahan_bakar: str, hp: int):
        self.merk = merk
        # KOMPOSISI: Objek Mesin lahir bersamaan di dalam Mobil
        self.mesin = Mesin(tipe_bahan_bakar=bahan_bakar, tenaga_kuda=hp)

    def pacu_gas(self):
        print(f"[KOMPOSISI] Mobil {self.merk} memacu kecepatan:")
        print(f"  -> {self.mesin.hidupkan()}")


# ==============================================================================
# BLOK PENGUJIAN & BUKTI SIKLUS HIDUP
# ==============================================================================
if __name__ == "__main__":
    print("=" * 65)
    print("[DEMO 1] ASOSIASI (Hubungan Bebas & Setara)")
    print("=" * 65)

    dr_tirta = Dokter("Tirta", "Umum")
    pasien_andi = Pasien("Andi", "Demam dan Batuk")

    resep = dr_tirta.periksa(pasien_andi)
    print(f"Hasil Resep: {resep}")
    print("Bukti: Dr. Tirta dan Andi adalah 2 entitas bebas tanpa kepemilikan.")

    print("\n" + "=" * 65)
    print("[DEMO 2] AGREGASI (Wadah Hancur, Isi Tetap Hidup)")
    print("=" * 65)

    # 1. Pemain diciptakan terlebih dahulu di RAM
    cr7 = Pemain("Cristiano Ronaldo", "Penyerang")
    modric = Pemain("Luka Modric", "Gelandang")

    # 2. Klub dibentuk dan merekrut pemain
    madrid = KlubSepakbola("Real Madrid")
    madrid.rekrut_pemain(cr7)
    madrid.rekrut_pemain(modric)
    madrid.tampilkan_skuad()

    # 3. BUKTI AGREGASI: Hancurkan objek klub!
    print("\n[SIMULASI] Klub 'Real Madrid' bubar dan dihapus dari memori!")
    del madrid

    # Apakah pemain ikut mati? TIDAK!
    print(f"Status Pemain setelah klub bubar: {cr7.nama} MASIH HIDUP di RAM!")
    print(f"Status Pemain setelah klub bubar: {modric.nama} MASIH HIDUP di RAM!")

    # Pemain bisa bergabung ke klub baru:
    al_nassr = KlubSepakbola("Al-Nassr FC")
    al_nassr.rekrut_pemain(cr7)

    print("\n" + "=" * 65)
    print("[DEMO 3] KOMPOSISI (Keterikatan Mati-Hidup)")
    print("=" * 65)

    tesla = Mobil("Tesla Model S Plaid", "Listrik", 1020)
    tesla.pacu_gas()

    # Di dalam komposisi, mesin tidak diciptakan terpisah di luar.
    # Jika objek 'tesla' dihapus:
    print("\n[SIMULASI] Mobil Tesla hancur dilebur di tempat rongsokan (del tesla)...")
    del tesla
    # Kita tidak punya variabel independen bernama 'mesin' di luar mobil.
    # Mesinnya ikut musnah bersama badan mobil!
    print("[BUKTI] Objek mesin internal ikut musnah bersama mobil.")

    print("\n" + "=" * 65)
    print("[OK] Selesai: Tiga jenis hubungan objek terbukti secara nyata.")
    print("=" * 65)
