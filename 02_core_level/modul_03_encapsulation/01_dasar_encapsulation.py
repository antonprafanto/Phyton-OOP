"""
01_dasar_encapsulation.py
=========================
Modul 3: Pilar 1 – Encapsulation & Gaya Elegan @property

File ini mendemonstrasikan:
1. Tiga tingkatan akses di Python (Public, Protected, Private)
2. Mekanisme Name Mangling pada atribut private
3. Mengintip kamus __dict__ untuk melihat bagaimana Python mengubah nama variabel
"""
import sys

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

print("=" * 60)
print("[DEMO] TIGA TINGKATAN AKSES DATA DI PYTHON")
print("=" * 60)

class RekeningBank:
    def __init__(self, nama_nasabah: str, saldo_awal: int, pin_rahasia: str):
        # 1. PUBLIC: Bebas diakses siapa saja
        self.nama = nama_nasabah

        # 2. PROTECTED: 1 garis bawah (Konvensi kesopanan: jangan utak-atik dari luar!)
        self._saldo = saldo_awal

        # 3. PRIVATE: 2 garis bawah (Memicu Name Mangling Python)
        self.__pin = pin_rahasia

    def periksa_pin(self, input_pin: str) -> bool:
        """Method resmi untuk validasi PIN tanpa membocorkan PIN aslinya."""
        return self.__pin == input_pin


# --- PENGUJIAN ---
akun_budi = RekeningBank("Budi Santoso", 5_000_000, "7890")

print("\n--- 1. Mengakses Atribut Public ---")
print(f"Nama Nasabah : {akun_budi.nama} (Bisa diakses langsung)")

print("\n--- 2. Mengakses Atribut Protected ---")
print(f"Saldo (_saldo): Rp {akun_budi._saldo:,}")
print("Catatan: Secara teknis bisa dibaca, tetapi konvensi Python melarang")
print("mengubah variabel berawalan satu underscore (_) secara sembarangan!")

print("\n--- 3. Mengakses Atribut Private (__pin) Secara Langsung ---")
try:
    print(akun_budi.__pin)
except AttributeError as err:
    print(f"Gagal diakses! Pesan Error:\n>>> {err}")
    print("Python menolak karena nama '__pin' sudah disembunyikan!")

print("\n--- 4. Membongkar Rahasia Name Mangling ---")
print("Mari kita intip kamus memori akun_budi.__dict__:")
print(f"Isi __dict__: {akun_budi.__dict__}")
print("\nPerhatikan kunci untuk PIN:")
print(f"Kuncinya berubah nama menjadi: '_RekeningBank__pin'")

# Membuktikan akses via Name Mangling:
print(f"Mengakses via name mangling (akun_budi._RekeningBank__pin): {akun_budi._RekeningBank__pin}")
print("Filosofi Python: 'We are all consenting adults here'.")
print("Name mangling bukan enkripsi anti-hacker, melainkan gembok peringatan keras.")

print("\n" + "=" * 60)
print("[OK] Selesai: Tiga tingkatan akses berhasil dipelajari.")
print("=" * 60)
