"""
02_property_decorator.py
========================
Modul 3: Pilar 1 – Encapsulation & Gaya Elegan @property

File ini mendemonstrasikan:
1. Cara modern membuat Getter dengan @property
2. Cara membuat Setter dengan validasi ketat (@variabel.setter)
3. Cara membuat Read-Only Property (hanya bisa dibaca)
4. Bedah jebakan RecursionError saat menulis property
"""
import sys

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

print("=" * 60)
print("[DEMO] GAYA MODERN PYTHON: DECORATOR @property & @setter")
print("=" * 60)

class RekeningModern:
    def __init__(self, nomor_rekening: str, pemilik: str, saldo_awal: int):
        self._nomor_rekening = nomor_rekening  # Read-only
        self.pemilik = pemilik                 # Public
        self._saldo = max(0, saldo_awal)       # Protected dengan validasi

    # -------------------------------------------------------------
    # 1. READ-ONLY PROPERTY (Hanya ada getter, tanpa setter!)
    # -------------------------------------------------------------
    @property
    def nomor_rekening(self) -> str:
        """Nomor rekening hanya bisa dibaca, tidak boleh diubah selamanya!"""
        return self._nomor_rekening

    # -------------------------------------------------------------
    # 2. PROPERTY DENGAN VALIDASI (@property + @setter)
    # -------------------------------------------------------------
    @property
    def saldo(self) -> int:
        """Getter: Membaca saldo seolah-olah membaca variabel biasa."""
        return self._saldo

    @saldo.setter
    def saldo(self, nilai_baru: int):
        """Setter: Mengamankan perubahan saldo dari angka ilegal."""
        if nilai_baru < 0:
            print(f"[DITOLAK] Gagal update saldo {self.pemilik}! Saldo tidak boleh negatif (Rp {nilai_baru:,})")
        else:
            self._saldo = nilai_baru
            print(f"[BERHASIL] Saldo {self.pemilik} berhasil diubah menjadi: Rp {self._saldo:,}")


# --- PENGUJIAN ---
budi = RekeningModern("ACC-998811", "Budi Santoso", 1_000_000)

print("\n--- 1. Membaca Data Menggunakan Notasi Titik Bersih ---")
print(f"Nomor Rekening : {budi.nomor_rekening}")
print(f"Pemilik Akun   : {budi.pemilik}")
print(f"Saldo Saat Ini : Rp {budi.saldo:,}")

print("\n--- 2. Menguji Read-Only Property (Mencoba Mengubah No Rekening) ---")
try:
    budi.nomor_rekening = "ACC-000000"
except AttributeError as err:
    print(f"Peringatan Python:\n>>> {err}")
    print(">>> Nomor rekening AMAN dari perubahan liar!")

print("\n--- 3. Menguji Setter dengan Nilai Ilegal (Minus) ---")
budi.saldo = -500_000
print(f"Saldo setelah percobaan ilegal: Rp {budi.saldo:,} (Tetap tidak berubah!)")

print("\n--- 4. Menguji Setter dengan Nilai Valid ---")
budi.saldo = 2_500_000
print(f"Saldo terkini: Rp {budi.saldo:,}")

# --- BEDAH JEBAKAN RECURSION ERROR ---
print("\n" + "-" * 60)
print("[BEDAH JEBAKAN] Mengapa RecursionError Terjadi?")
print("-" * 60)

class ContohJebakanRecursion:
    @property
    def poin(self):
        return self._poin

    @poin.setter
    def poin(self, nilai):
        # JIKA MENULIS: self.poin = nilai  <-- OOPS! Ini memanggil setter ini lagi tanpa henti!
        # YANG BENAR:
        self._poin = nilai

j = ContohJebakanRecursion()
j.poin = 100
print(f"Poin berhasil diset dengan aman ke _poin: {j.poin}")
print("Aturan: Jangan menamai variabel internal sama persis dengan nama @property-nya!")

print("\n" + "=" * 60)
print("[OK] Selesai: @property dan validasi data bekerja sempurna.")
print("=" * 60)
