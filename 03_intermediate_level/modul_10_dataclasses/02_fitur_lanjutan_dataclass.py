"""
================================================================================
MODUL 10: MODERN PYTHON SHORTCUT (@dataclass) & TYPE HINTING
Berkas 02: Fitur Lanjutan (@dataclass) - Field Factory, Post Init, Frozen, & Order
================================================================================
Tujuan Pembelajaran:
1. Mengatasi jebakan mutable default dengan field(default_factory=list).
2. Melakukan validasi dan komputasi field otomatis lewat __post_init__.
3. Mengunci objek agar kebal perubahan (Immutable / Read-Only) lewat frozen=True.
4. Mengaktifkan fitur pengurutan dan perbandingan otomatis lewat order=True.
================================================================================
"""

import sys
from dataclasses import dataclass, field, FrozenInstanceError

# Konfigurasi terminal agar kompatibel dengan encoding Windows / UTF-8
if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass


# ==============================================================================
# 1. FITUR: default_factory & __post_init__
# ==============================================================================
@dataclass
class AnggotaDeveloper:
    nama: str
    gaji_pokok: int
    # 1. Hindari 'skills: list = []'! Gunakan default_factory:
    skills: list[str] = field(default_factory=list)

    # 2. Field turunan: dihitung otomatis di post_init, tidak diminta di __init__
    pajak_pph: int = field(init=False)
    gaji_bersih: int = field(init=False)

    def __post_init__(self):
        """Dijalankan otomatis segera setelah __init__ selesai."""
        # A. Validasi Aturan Bisnis
        if self.gaji_pokok <= 0:
            raise ValueError(f"Gaji pokok harus positif! Diterima: {self.gaji_pokok}")

        # B. Komputasi Nilai Turunan (Pajak 5% dan Gaji Bersih)
        self.pajak_pph = int(self.gaji_pokok * 0.05)
        self.gaji_bersih = self.gaji_pokok - self.pajak_pph


# ==============================================================================
# 2. FITUR: frozen=True (Objek Read-Only / Immutable)
# ==============================================================================
@dataclass(frozen=True)
class KonfigurasiServer:
    """Objek konfigurasi penting yang tidak boleh diubah saat aplikasi berjalan."""
    host: str
    port: int
    secret_key: str


# ==============================================================================
# 3. FITUR: order=True (Perbandingan & Pengurutan Otomatis)
# ==============================================================================
@dataclass(order=True)
class SkorTurnamen:
    """
    Dengan order=True, objek otomatis memiliki method __lt__, __le__, __gt__, __ge__.
    Python membandingkan field dari urutan pertama (poin).
    """
    poin: int
    nama_player: str = field(compare=False)  # compare=False agar pengurutan murni dari poin


# ==============================================================================
# BLOK PENGUJIAN
# ==============================================================================
if __name__ == "__main__":
    print("=" * 65)
    print("[DEMO 1] default_factory & __post_init__")
    print("=" * 65)

    dev1 = AnggotaDeveloper("Andi", 10_000_000)
    dev1.skills.append("Python")
    dev1.skills.append("FastAPI")

    dev2 = AnggotaDeveloper("Budi", 15_000_000)
    # Bukti: dev2 memiliki list terpisah (tidak terkontaminasi skill Andi)
    dev2.skills.append("Flutter")

    print(f"Dev 1 : {dev1.nama}")
    print(f"  Skills       : {dev1.skills}")
    print(f"  Gaji Pokok   : Rp {dev1.gaji_pokok:,}")
    print(f"  Pajak (5%)   : Rp {dev1.pajak_pph:,} (Dihitung di __post_init__)")
    print(f"  Gaji Bersih  : Rp {dev1.gaji_bersih:,}")

    print(f"\nDev 2 : {dev2.nama}")
    print(f"  Skills       : {dev2.skills} (List terpisah berkat default_factory)")
    print(f"  Gaji Bersih  : Rp {dev2.gaji_bersih:,}")

    print("\n" + "=" * 65)
    print("[DEMO 2] frozen=True (Objek Kebal Perubahan)")
    print("=" * 65)

    config = KonfigurasiServer(host="api.antigravity.id", port=8080, secret_key="RAHASIA_123")
    print(f"Konfigurasi aktif: {config}")

    # Mencoba mengubah nilai host:
    try:
        config.host = "hacker-site.com"  # type: ignore
    except FrozenInstanceError as err:
        print(f"[PROTEKSI AKTIF] ⛔ Perubahan ditolak: {err}")
        print("  -> Objek berstatus Read-Only dan aman dari modifikasi tidak sengaja.")

    print("\n" + "=" * 65)
    print("[DEMO 3] order=True (Pengurutan Otomatis Objek)")
    print("=" * 65)

    leaderboard = [
        SkorTurnamen(poin=120, nama_player="Gamer_Noob"),
        SkorTurnamen(poin=950, nama_player="Pro_Sniper"),
        SkorTurnamen(poin=450, nama_player="Mid_Lane")
    ]

    print("Leaderboard Sebelum Diurutkan:")
    for entry in leaderboard:
        print(f"  - {entry.nama_player:<12}: {entry.poin} poin")

    # Mengurutkan otomatis dari poin terendah ke tertinggi:
    leaderboard.sort()
    print("\nLeaderboard Setelah list.sort() (Terurut Menaik):")
    for entry in leaderboard:
        print(f"  - {entry.nama_player:<12}: {entry.poin} poin")

    # Pengurutan menurun (Ranking tertinggi di atas):
    leaderboard.sort(reverse=True)
    print("\nLeaderboard Ranking Tertinggi (reverse=True):")
    for entry in leaderboard:
        print(f"  - {entry.nama_player:<12}: {entry.poin} poin")

    print("\n" + "=" * 65)
    print("[OK] Selesai: Fitur lanjutan @dataclass berhasil dipelajari dan diuji.")
    print("=" * 65)
