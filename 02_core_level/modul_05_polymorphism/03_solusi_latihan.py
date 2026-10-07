"""
03_solusi_latihan.py
====================
Modul 5: Pilar 3 – Polymorphism & Filosofi Duck Typing

Kunci Jawaban & Pembahasan Latihan Payment Gateway E-Commerce 🛒💳
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
        print(f"[TUNAI] Menerima uang fisik cash pas sebesar Rp {nominal:,} di meja kasir.")
        return True


# ==============================================================
# 2. KELAS PEMBAYARAN QRIS
# ==============================================================
class BayarQRIS:
    def __init__(self, provider: str, saldo_ewallet: int):
        self.provider = provider
        self.saldo_ewallet = saldo_ewallet

    def proses_bayar(self, nominal: int) -> bool:
        if self.saldo_ewallet >= nominal:
            self.saldo_ewallet -= nominal
            print(f"[QRIS] Scan barcode via {self.provider} berhasil!")
            print(f"       Terpotong: Rp {nominal:,} | Sisa Saldo: Rp {self.saldo_ewallet:,}")
            return True
        else:
            print(f"[QRIS DITOLAK] Saldo {self.provider} tidak cukup! Butuh Rp {nominal:,}, sisa Rp {self.saldo_ewallet:,}")
            return False


# ==============================================================
# 3. KELAS PEMBAYARAN KARTU KREDIT
# ==============================================================
class BayarKartuKredit:
    def __init__(self, nomor_kartu: str, sisa_limit: int):
        self.nomor_kartu = nomor_kartu
        self.sisa_limit = sisa_limit

    def proses_bayar(self, nominal: int) -> bool:
        if self.sisa_limit >= nominal:
            self.sisa_limit -= nominal
            sensor_kartu = f"****{self.nomor_kartu[-4:]}"
            print(f"[KARTU KREDIT] Otorisasi kartu {sensor_kartu} berhasil!")
            print(f"               Tagihan: Rp {nominal:,} | Sisa Limit: Rp {self.sisa_limit:,}")
            return True
        else:
            print(f"[KARTU DITOLAK] Limit kartu kredit tidak mencukupi untuk tagihan Rp {nominal:,}!")
            return False


# ==============================================================
# 4. FUNGSI KASIR POLIMORFIK (SATU PINTU UNTUK SEMUA)
# ==============================================================
def checkout_belanja(pelanggan: str, total_tagihan: int, kanal_bayar):
    print(f"\n[KASIR] Memproses pesanan {pelanggan} senilai Rp {total_tagihan:,}...")
    
    # KEKUATAN POLYMORPHISM: Panggil saja 'proses_bayar()' secara seragam!
    status_sukses = kanal_bayar.proses_bayar(total_tagihan)
    
    if status_sukses:
        print(f"[STATUS] ✅ Pembayaran untuk {pelanggan} LUNAS. Struk belanja dicetak!")
    else:
        print(f"[STATUS] ❌ Transaksi untuk {pelanggan} GAGAL. Silakan coba metode lain.")


# --- PENGUJIAN SOLUSI ---
if __name__ == "__main__":
    print("=" * 60)
    print("[OK] HASIL EKSEKUSI KUNCI JAWABAN PAYMENT GATEWAY")
    print("=" * 60)

    # Inisialisasi kanal pembayaran
    tunai = BayarTunai()
    gopay = BayarQRIS("GoPay", 100_000)
    kartu_bca = BayarKartuKredit("4556112233448899", 1_000_000)

    # Transaksi 1: Tunai
    checkout_belanja("Anton", 45_000, tunai)

    # Transaksi 2: QRIS (Saldo Cukup: 100.000 - 60.000 = sisa 40.000)
    checkout_belanja("Budi", 60_000, gopay)

    # Transaksi 3: QRIS (Saldo Kurang: butuh 50.000, sisa cuma 40.000)
    checkout_belanja("Budi", 50_000, gopay)

    # Transaksi 4: Kartu Kredit
    checkout_belanja("Siti", 450_000, kartu_bca)
    print("=" * 60)
