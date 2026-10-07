"""
03_solusi_latihan.py
====================
Modul 1: Melahirkan Objek Pertama (Class, Object, Constructor, & self)

Kunci Jawaban & Pembahasan Latihan Kedai Kopi ☕
"""
import sys

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

class PesananKopi:
    def __init__(self, pelanggan: str, jenis: str, ukuran: str):
        self.pelanggan = pelanggan
        self.jenis = jenis
        self.ukuran = ukuran
        self.status_siap = False

    def tampilkan_ringkasan(self):
        status_teks = "SIAP DISAJIKAN" if self.status_siap else "SEDANG MENGANTRI"
        print(f"[PESANAN] Pelanggan: {self.pelanggan:<10} | Menu: {self.jenis:<18} ({self.ukuran}) | Status: {status_teks}")

    def seduh(self):
        print(f"[BARISTA] Menyeduh biji kopi pilihan untuk {self.jenis} pesanan {self.pelanggan}...")
        self.status_siap = True
        print(f"[SELESAI] Kopi {self.jenis} sekarang sudah matang dan harum!")

    def sajikan(self):
        if self.status_siap:
            print(f"[SUKSES] Pesanan diserahkan: 'Silakan dinikmati, Kak {self.pelanggan}!'")
        else:
            print(f"[TUNGGU] Mohon bersabar, Kak {self.pelanggan}, kopi {self.jenis} masih dalam proses penyeduhan!")


# --- PENGUJIAN SOLUSI ---
if __name__ == "__main__":
    print("=" * 60)
    print("[OK] HASIL EKSEKUSI KUNCI JAWABAN PESANAN KOPI")
    print("=" * 60)

    # 1. Pesanan masuk
    pesanan_1 = PesananKopi("Anton", "Caramel Macchiato", "Besar")
    pesanan_2 = PesananKopi("Dian", "Americano Dingin", "Sedang")

    pesanan_1.tampilkan_ringkasan()
    pesanan_2.tampilkan_ringkasan()

    # 2. Coba sajikan sebelum diseduh
    print("\n--- Percobaan Penyajian Awal ---")
    pesanan_1.sajikan()

    # 3. Barista menyeduh hanya pesanan Anton
    print("\n--- Barista Memproses Pesanan Anton ---")
    pesanan_1.seduh()
    pesanan_1.tampilkan_ringkasan()

    # 4. Sajikan kembali kedua pesanan
    print("\n--- Percobaan Penyajian Kedua ---")
    pesanan_1.sajikan()  # Berhasil!
    pesanan_2.sajikan()  # Tetap menolak karena pesanan Dian belum diseduh!

    print("\n" + "=" * 60)
    print("Perhatikan: Status 'status_siap' milik Anton berubah menjadi True,")
    print("tetapi milik Dian tetap False. Objek bekerja secara terisolasi!")
    print("=" * 60)
