"""
03_latihan_mandiri.py
=====================
Modul 5: Pilar 3 – Polymorphism & Filosofi Duck Typing

TANTANGAN PRAKTEK: PAYMENT GATEWAY TOKO ONLINE 🛒💳

Skenario:
Sebuah platform e-commerce membutuhkan modul kasir pintar (SmartCheckout).
Kasir harus mampu memproses pembayaran dari berbagai kanal secara polimorfik
tanpa harus membuat rantai 'if-elif' jenis pembayaran yang panjang!

KETENTUAN KELAS PEMBAYARAN:
Setiap metode pembayaran HARUS memiliki method seragam: 'proses_bayar(nominal: int) -> bool'

1. KELAS 'BayarTunai':
   - Tidak butuh saldo/limit.
   - proses_bayar(nominal): Mencetak bahwa uang tunai pas Rp {nominal} telah diterima di kasir. Kembalikan True.

2. KELAS 'BayarQRIS':
   - __init__(provider: str, saldo_ewallet: int)
   - proses_bayar(nominal):
       * Jika saldo_ewallet >= nominal: potong saldo, cetak pembayaran QRIS via {provider} berhasil, kembalikan True.
       * Jika saldo kurang: cetak saldo e-wallet tidak cukup, kembalikan False.

3. KELAS 'BayarKartuKredit':
   - __init__(nomor_kartu: str, sisa_limit: int)
   - proses_bayar(nominal):
       * Jika sisa_limit >= nominal: kurangi limit, cetak gesek kartu ****{4 digit akhir} berhasil, kembalikan True.
       * Jika limit kurang: cetak limit kartu kredit tidak mencukupi, kembalikan False.

4. FUNGSI KASIR POLIMORFIK 'checkout_belanja(pelanggan: str, total_tagihan: int, kanal_bayar)':
   - Jalankan 'kanal_bayar.proses_bayar(total_tagihan)'.
   - Jika berhasil: cetak struk 'TERIMA KASIH TELAH BERBELANJA!'.
   - Jika gagal: cetak 'TRANSAKSI DIBATALKAN. SILAKAN COBA METODE LAIN!'.

Instruksi:
Lengkapi bagian TODO di bawah ini. Kunci jawaban tersedia di '03_solusi_latihan.py'.
"""
import sys

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# ==============================================================
# 1. KELAS PEMBAYARAN TUNAI
# ==============================================================
class BayarTunai:
    def proses_bayar(self, nominal: int) -> bool:
        # TODO 1: Cetak pesan penerimaan uang tunai dan kembalikan True
        pass


# ==============================================================
# 2. KELAS PEMBAYARAN QRIS
# ==============================================================
class BayarQRIS:
    def __init__(self, provider: str, saldo_ewallet: int):
        self.provider = provider
        self.saldo_ewallet = saldo_ewallet

    def proses_bayar(self, nominal: int) -> bool:
        # TODO 2: Cek kecukupan saldo e-wallet.
        # Jika cukup: kurangi saldo, cetak notifikasi sukses, return True
        # Jika kurang: cetak pesan saldo tidak cukup, return False
        pass


# ==============================================================
# 3. KELAS PEMBAYARAN KARTU KREDIT
# ==============================================================
class BayarKartuKredit:
    def __init__(self, nomor_kartu: str, sisa_limit: int):
        self.nomor_kartu = nomor_kartu
        self.sisa_limit = sisa_limit

    def proses_bayar(self, nominal: int) -> bool:
        # TODO 3: Cek sisa limit kartu kredit.
        # Jika cukup: kurangi limit, cetak notifikasi dengan sensor 4 digit akhir, return True
        # Jika kurang: cetak limit tidak mencukupi, return False
        pass


# ==============================================================
# 4. FUNGSI KASIR POLIMORFIK (SATU PINTU UNTUK SEMUA)
# ==============================================================
def checkout_belanja(pelanggan: str, total_tagihan: int, kanal_bayar):
    print(f"\n[KASIR] Memproses pesanan {pelanggan} senilai Rp {total_tagihan:,}...")
    
    # TODO 4: Panggil method polimorfik 'proses_bayar' dari kanal_bayar
    # Cek hasilnya (True/False) dan cetak status akhir transaksi
    pass


# --- PENGUJIAN KODE ANDA ---
if __name__ == "__main__":
    print("=" * 60)
    print("[TEST] MENGUJI PAYMENT GATEWAY POLIMORFIK")
    print("=" * 60)

    # 1. Siapkan metode pembayaran
    tunai = BayarTunai()
    gopay = BayarQRIS("GoPay", 100_000)
    kartu_bca = BayarKartuKredit("4556112233448899", 1_000_000)

    # 2. Uji Coba Transaksi 1: Tunai
    checkout_belanja("Anton", 45_000, tunai)

    # 3. Uji Coba Transaksi 2: QRIS (Saldo Cukup)
    checkout_belanja("Budi", 60_000, gopay)

    # 4. Uji Coba Transaksi 3: QRIS (Saldo Kurang, sisa cuma 40rb)
    checkout_belanja("Budi", 50_000, gopay)

    # 5. Uji Coba Transaksi 4: Kartu Kredit
    checkout_belanja("Siti", 450_000, kartu_bca)
    print("=" * 60)
