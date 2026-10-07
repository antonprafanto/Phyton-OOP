"""
================================================================================
MODUL 11: HUBUNGAN ANTAR OBJEK (OBJECT RELATIONSHIPS)
Berkas 02: Filosofi Arsitektur - Favor Composition Over Inheritance
================================================================================
Tujuan Pembelajaran:
1. Memahami bencana 'Class Explosion' ketika terlalu mengandalkan Inheritance.
2. Membuktikan bagaimana Komposisi memungkinkan perilaku objek diganti secara
   dinamis saat runtime (Plug-and-Play / Dependency Injection).
3. Mengubah arsitektur RPG kaku menjadi sistem modular layaknya balok Lego.
================================================================================
"""

import sys
from abc import ABC, abstractmethod

# Konfigurasi terminal agar kompatibel dengan encoding Windows / UTF-8
if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass


# ==============================================================================
# 1. KOMPONEN SENJATA (DAPAT DITUKAR-PASANG)
# ==============================================================================
class Senjata(ABC):
    @abstractmethod
    def nama_senjata(self) -> str:
        pass

    @abstractmethod
    def base_damage(self) -> int:
        pass


class PedangBesi(Senjata):
    def nama_senjata(self) -> str:
        return "Pedang Ksatria Baja"

    def base_damage(self) -> int:
        return 50


class BusurPanah(Senjata):
    def nama_senjata(self) -> str:
        return "Busur Angin Siluman"

    def base_damage(self) -> int:
        return 40


class TongkatSihir(Senjata):
    def nama_senjata(self) -> str:
        return "Tongkat Permata Bintang"

    def base_damage(self) -> int:
        return 75


# ==============================================================================
# 2. KOMPONEN ELEMEN (MODIFIER EFEK)
# ==============================================================================
class Elemen(ABC):
    @abstractmethod
    def efek(self) -> str:
        pass

    @abstractmethod
    def bonus_damage(self) -> int:
        pass


class ElemenApi(Elemen):
    def efek(self) -> str:
        return "Kobaran Api Membara (Luka Bakar)"

    def bonus_damage(self) -> int:
        return 25


class ElemenEs(Elemen):
    def efek(self) -> str:
        return "Hawa Beku Gletser (Efek Lambat)"

    def bonus_damage(self) -> int:
        return 15


class ElemenNetral(Elemen):
    def efek(self) -> str:
        return "Fisik Murni"

    def bonus_damage(self) -> int:
        return 0


# ==============================================================================
# 3. KELAS UTAMA: KARAKTER (MEMILIKI SENJATA & ELEMEN LEWAT KOMPOSISI)
# ==============================================================================
class Pahlawan:
    """
    Kelas Pahlawan TIDAK mewarisi Pedang, Busur, atau Api.
    Pahlawan MEMILIKI (HAS-A) Senjata dan Elemen!
    """
    def __init__(self, nama: str, senjata: Senjata, elemen: Elemen = ElemenNetral()):
        self.nama = nama
        self.senjata = senjata  # Komposisi
        self.elemen = elemen    # Komposisi

    def serang(self, target: str):
        total_serangan = self.senjata.base_damage() + self.elemen.bonus_damage()
        print(f"\n[SERANGAN] {self.nama} menyerang '{target}'!")
        print(f"  -> Senjata       : {self.senjata.nama_senjata()} (Base: {self.senjata.base_damage()})")
        print(f"  -> Elemen        : {self.elemen.efek()} (+{self.elemen.bonus_damage()})")
        print(f"  -> Total Damage  : {total_serangan} poin!")

    def pasang_senjata_baru(self, senjata_baru: Senjata):
        """Kekuatan Komposisi: Senjata bisa diganti saat game sedang berjalan!"""
        print(f"\n[LOOT ITEM] {self.nama} membuang {self.senjata.nama_senjata()} dan melengkapi: {senjata_baru.nama_senjata()}!")
        self.senjata = senjata_baru

    def berkati_elemen(self, elemen_baru: Elemen):
        """Elemen bisa di-upgrade kapan saja tanpa mengubah class Karakter."""
        print(f"\n[ENCHANT] Senjata {self.nama} diberkati dengan: {elemen_baru.efek()}!")
        self.elemen = elemen_baru


# ==============================================================================
# PENGUJIAN DAN DEMONSTRASI KEUNGGULAN KOMPOSISI
# ==============================================================================
if __name__ == "__main__":
    print("=" * 65)
    print("[DEMO] KEKUATAN KOMPOSISI DIBANDINGKAN INHERITANCE")
    print("=" * 65)

    # 1. Pahlawan lahir dengan Pedang Netral
    arthur = Pahlawan("Arthur", senjata=PedangBesi())
    arthur.serang("Goblin Liar")

    # 2. Arthur menemukan Kuil Api kuno -> Elemen di-upgrade saat runtime!
    arthur.berkati_elemen(ElemenApi())
    arthur.serang("Bos Orc")

    # 3. Arthur menemukan Busur Panah dari peti harta karun -> Senjata berganti!
    # Jika menggunakan Inheritance, objek Arthur tidak bisa mengubah class-nya.
    # Dengan Komposisi, cukup ubah atribut self.senjata!
    arthur.pasang_senjata_baru(BusurPanah())
    arthur.serang("Naga Merah")

    # 4. Arthur berganti profesi menjadi Penyihir Es dalam 1 detik!
    arthur.pasang_senjata_baru(TongkatSihir())
    arthur.berkati_elemen(ElemenEs())
    arthur.serang("Raja Iblis")

    print("\n" + "=" * 65)
    print("[OK] Selesai: Filosofi 'Favor Composition over Inheritance' terbukti!")
    print("=" * 65)
