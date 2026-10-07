"""
02_solusi_oop.py
================
Modul 0: Mengapa Kita Butuh OOP?

File ini mendemonstrasikan bagaimana OOP menyatukan Data (Atribut)
dan Tindakan (Method) ke dalam satu wadah mandiri yang aman.
"""
import sys

# Memastikan output terminal mendukung encoding UTF-8 di Windows
if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

print("=" * 60)
print("[OK] SOLUSI MENGGUNAKAN OOP (BERORIENTASI OBJEK)")
print("=" * 60)

# 1. KITA BUAT CETAKANNYA (CLASS)
class RekeningBank:
    """
    Cetak biru (blueprint) untuk melahirkan objek rekening bank.
    Menyatukan data pemilik, nomor rekening, dan saldo ke dalam satu kesatuan.
    """
    def __init__(self, nama: str, no_rekening: str, saldo_awal: int):
        # ATRIBUT (Ciri-ciri / Data yang melekat pada rekening)
        self.nama = nama
        self.no_rekening = no_rekening
        self.saldo = saldo_awal

    # METHOD (Perilaku / Aksi yang bisa dilakukan oleh rekening)
    def tampilkan_info(self):
        print(f"[REKENING] Nasabah: {self.nama:<10} | No: {self.no_rekening:<5} | Saldo: Rp {self.saldo:,}")

    def setor(self, jumlah: int):
        if jumlah > 0:
            self.saldo += jumlah
            print(f"[OK] Setoran Rp {jumlah:,} berhasil! Saldo {self.nama} sekarang: Rp {self.saldo:,}")
        else:
            print("[X] Jumlah setoran harus lebih dari 0!")

    def tarik(self, jumlah: int):
        if jumlah <= 0:
            print("[X] Jumlah penarikan tidak valid!")
        elif jumlah > self.saldo:
            print(f"[X] Saldo {self.nama} tidak mencukupi untuk menarik Rp {jumlah:,} (Sisa saldo: Rp {self.saldo:,})")
        else:
            self.saldo -= jumlah
            print(f"[OK] Penarikan Rp {jumlah:,} berhasil! Sisa saldo {self.nama}: Rp {self.saldo:,}")


# 2. KITA LAHIRKAN OBJEK NYATA (INSTANSIASI)
budi = RekeningBank("Budi", "101", 500_000)
siti = RekeningBank("Siti", "102", 1_200_000)
ahmad = RekeningBank("Ahmad", "103", 350_000)

print("\n--- Kondisi Awal Nasabah ---")
budi.tampilkan_info()
siti.tampilkan_info()
ahmad.tampilkan_info()

print("\n" + "-" * 60)
print("[INFO] BUKTI KEUNGGULAN OOP:")
print("-" * 60)

# Keunggulan 1: Aksi mandiri (Budi setor uang tidak mengganggu saldo Siti / Ahmad)
print("1. Budi menyetor Rp 200.000:")
budi.setor(200_000)

# Keunggulan 2: Validasi logika bisnis otomatis
print("\n2. Ahmad mencoba menarik Rp 500.000 (melebihi saldo):")
ahmad.tarik(500_000)

# Keunggulan 3: Jika Siti dihapus, data Ahmad & Budi TETAP AMAN!
print("\n3. Siti menutup akunnya (dihapus dari sistem):")
del siti  # Menghapus objek siti dari memori

print("\n--- Cek kembali Budi & Ahmad setelah Siti dihapus ---")
budi.tampilkan_info()
ahmad.tampilkan_info()
print("\n>>> DATA TIDAK AKAN TERTUKAR! Karena setiap objek berdiri sendiri secara utuh.")
print("=" * 60)
