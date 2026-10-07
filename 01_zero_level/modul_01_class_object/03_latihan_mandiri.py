"""
03_latihan_mandiri.py
=====================
Modul 1: Melahirkan Objek Pertama (Class, Object, Constructor, & self)

TANTANGAN PRAKTEK: SISTEM KASIR KEDAI KOPI (CoffeeShop Order) ☕

Skenario:
Setiap kali ada pelanggan memesan kopi, kasir akan membuat sebuah objek 'PesananKopi'.

LENGKAPI KODE DI BAWAH INI:
1. Class 'PesananKopi' harus memiliki:
   - Atribut (di dalam __init__):
     * pelanggan: nama pembeli (misal: "Anton")
     * jenis: jenis kopi (misal: "Espresso", "Caramel Latte")
     * ukuran: ukuran cup ("Sedang" atau "Besar")
     * status_siap: status pesanan (di awal selalu False / belum diseduh)

2. Method:
   - tampilkan_ringkasan(): mencetak rincian pesanan dan statusnya
   - seduh(): mengubah status_siap menjadi True dan mencetak pesan bahwa kopi sedang dibuat
   - sajikan(): jika kopi sudah siap (status_siap == True), cetak bahwa kopi diserahkan ke pelanggan.
                jika belum siap, peringatkan bahwa kopi belum selesai diseduh!

Instruksi:
Gantilah bagian TODO di bawah ini. Kunci jawaban tersedia di '03_solusi_latihan.py'.
"""
import sys

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

class PesananKopi:
    def __init__(self, pelanggan: str, jenis: str, ukuran: str):
        # TODO 1: Pasangkan parameter ke atribut self
        self.pelanggan = pelanggan
        self.jenis = jenis
        self.ukuran = ukuran
        self.status_siap = False  # Bawaan lahir: belum diseduh

    def tampilkan_ringkasan(self):
        # TODO 2: Tampilkan informasi pesanan dengan rapi
        status_teks = "SIAP DISAJIKAN" if self.status_siap else "SEDANG MENGANTRI"
        print(f"[PESANAN] Pelanggan: {self.pelanggan} | Menu: {self.jenis} ({self.ukuran}) | Status: {status_teks}")

    def seduh(self):
        # TODO 3: Ubah self.status_siap menjadi True dan beri pesan notifikasi
        pass

    def sajikan(self):
        # TODO 4: Periksa apakah self.status_siap bernilai True.
        # Jika ya: cetak notifikasi penyerahan ke pelanggan.
        # Jika belum: cetak peringatan bahwa kopi belum selesai dibuat!
        pass


# --- PENGUJIAN KODE ANDA ---
if __name__ == "__main__":
    print("=" * 60)
    print("[TEST] MENGUJI OBJEK PESANAN KOPI")
    print("=" * 60)

    # 1. Pesanan datang
    pesanan_1 = PesananKopi("Anton", "Caramel Macchiato", "Besar")
    pesanan_1.tampilkan_ringkasan()

    # 2. Pelayan mencoba menyajikan padahal belum diseduh
    print("\n--- Mencoba Menyajikan Terlalu Cepat ---")
    pesanan_1.sajikan()

    # 3. Barista menyeduh kopi
    print("\n--- Barista Mulai Bekerja ---")
    pesanan_1.seduh()
    pesanan_1.tampilkan_ringkasan()

    # 4. Pelayan menyajikan kembali kopi yang sudah jadi
    print("\n--- Menyajikan Kembali ---")
    pesanan_1.sajikan()
    print("=" * 60)
