"""
02_property_decorator.py
========================
Modul 3: Pilar 1 – Encapsulation & Gaya Elegan @property

File ini mendemonstrasikan:
1. Cara modern membuat Getter dengan @property
2. Cara membuat Setter dengan validasi tipe data (isinstance) & nilai
3. Cara membuat Deleter (@property.deleter)
4. Cara membuat Computed Property (perhitungan dinamis anti-data basi)
5. Bedah jebakan RecursionError saat menulis property
"""
import sys

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

print("=" * 60)
print("[DEMO] GAYA MODERN PYTHON: DECORATOR @property LENGKAP")
print("=" * 60)

# ==============================================================
# 1. TRIO PROPERTY LENGKAP (GETTER, SETTER, DELETER)
# ==============================================================
class RekeningModern:
    def __init__(self, nomor_rekening: str, pemilik: str, saldo_awal: int):
        self._nomor_rekening = nomor_rekening  # Read-only
        self.pemilik = pemilik                 # Public
        self._saldo = max(0, saldo_awal)       # Protected dengan validasi

    # 1. READ-ONLY PROPERTY (Getter saja)
    @property
    def nomor_rekening(self) -> str:
        """Nomor rekening hanya bisa dibaca, tidak boleh diubah selamanya!"""
        return self._nomor_rekening

    # 2. GETTER
    @property
    def saldo(self) -> int:
        return self._saldo

    # 3. SETTER DENGAN VALIDASI TIPE & NILAI
    @saldo.setter
    def saldo(self, nilai_baru):
        # Validasi 1: Harus berupa angka
        if not isinstance(nilai_baru, (int, float)):
            print(f"[DITOLAK] Nilai saldo harus berupa angka, bukan '{type(nilai_baru).__name__}'!")
            return

        # Validasi 2: Tidak boleh negatif
        if nilai_baru < 0:
            print(f"[DITOLAK] Gagal update saldo {self.pemilik}! Saldo tidak boleh negatif (Rp {nilai_baru:,})")
            return

        self._saldo = int(nilai_baru)
        print(f"[BERHASIL] Saldo {self.pemilik} berhasil diubah menjadi: Rp {self._saldo:,}")

    # 4. DELETER (Mengatur aksi saat perintah 'del akun.saldo' dijalankan)
    @saldo.deleter
    def saldo(self):
        print(f"[RESET] Perintah 'del' diterima: Saldo {self.pemilik} di-reset menjadi Rp 0!")
        self._saldo = 0


# ==============================================================
# 2. COMPUTED PROPERTY (MENCEGAH DATA BASI / DESINKRONISASI)
# ==============================================================
class PersegiPanjang:
    def __init__(self, panjang: float, lebar: float):
        self.panjang = panjang
        self.lebar = lebar

    # Dihitung otomatis kapan saja diminta!
    @property
    def luas(self) -> float:
        return self.panjang * self.lebar


# --- PENGUJIAN ---
print("\n--- 1. Uji Coba Rekening Modern ---")
budi = RekeningModern("ACC-998811", "Budi Santoso", 1_000_000)
print(f"Nomor Rekening : {budi.nomor_rekening}")
print(f"Saldo Awal     : Rp {budi.saldo:,}")

print("\n--- 2. Validasi Tipe Data & Nilai Negatif ---")
budi.saldo = "seratus ribu"  # Ditolak karena tipe string!
budi.saldo = -500_000        # Ditolak karena negatif!
budi.saldo = 2_500_000       # Berhasil!

print("\n--- 3. Menguji @deleter ---")
del budi.saldo               # Memicu deleter: reset ke 0
print(f"Saldo setelah del : Rp {budi.saldo:,}")

print("\n--- 4. Menguji Computed Property (Persegi Panjang) ---")
kotak = PersegiPanjang(10, 5)
print(f"Panjang = {kotak.panjang}, Lebar = {kotak.lebar} -> Luas = {kotak.luas}")

print("Jika panjang diubah menjadi 25...")
kotak.panjang = 25
print(f"Panjang = {kotak.panjang}, Lebar = {kotak.lebar} -> Luas = {kotak.luas} (OTOMATIS SEGAR & AKURAT!)")

print("\n" + "=" * 60)
print("[OK] Selesai: Trio @property dan Computed Property terkuasai.")
print("=" * 60)
