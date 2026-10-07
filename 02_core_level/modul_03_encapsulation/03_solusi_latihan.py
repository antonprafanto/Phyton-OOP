"""
03_solusi_latihan.py
====================
Modul 3: Pilar 1 – Encapsulation & Gaya Elegan @property

Kunci Jawaban & Pembahasan Latihan Dompet Digital Aman 📱💳
"""
import sys

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

class DompetDigital:
    def __init__(self, pemilik: str, nomor_hp: str, saldo_awal: int, pin: str):
        self.pemilik = pemilik
        self._nomor_hp = nomor_hp
        self._saldo = max(0, saldo_awal)
        self.__pin = pin  # Private mutlak!

    # 1. READ-ONLY PROPERTY (Nomor HP Tersensor)
    @property
    def nomor_hp(self) -> str:
        # Jika format nomor minimal 8 karakter, sensor 4 angka di tengah
        if len(self._nomor_hp) >= 8:
            return f"{self._nomor_hp[:4]}****{self._nomor_hp[-4:]}"
        return self._nomor_hp

    # 2. GETTER SALDO
    @property
    def saldo(self) -> int:
        return self._saldo

    # 3. SETTER SALDO DENGAN VALIDASI KETAT
    @saldo.setter
    def saldo(self, nilai_baru: int):
        if nilai_baru < 0:
            print(f"[ERROR SETTER] Saldo tidak boleh bernilai negatif (Rp {nilai_baru:,})!")
        else:
            self._saldo = nilai_baru

    # 4. METHOD TOP UP
    def top_up(self, jumlah: int):
        if jumlah > 0:
            self.saldo += jumlah
            print(f"[TOP-UP SUKSES] Berhasil isi saldo Rp {jumlah:,}. Saldo terkini: Rp {self.saldo:,}")
        else:
            print("[TOP-UP GAGAL] Jumlah isi saldo harus lebih dari 0!")

    # 5. METHOD BAYAR DENGAN OTORISASI PIN
    def bayar(self, jumlah: int, input_pin: str):
        # Lapisan 1: Verifikasi PIN Private
        if input_pin != self.__pin:
            print(f"[BAYAR DITOLAK] PIN transaksi salah untuk pengguna {self.pemilik}!")
            return False

        # Lapisan 2: Validasi Jumlah Pembayaran
        if jumlah <= 0:
            print("[BAYAR DITOLAK] Jumlah pembayaran tidak valid!")
            return False

        # Lapisan 3: Verifikasi Kecukupan Saldo
        if jumlah > self.saldo:
            print(f"[BAYAR DITOLAK] Saldo tidak cukup! Butuh Rp {jumlah:,}, sisa saldo Rp {self.saldo:,}")
            return False

        # Transaksi Sah: Kurangi saldo
        self.saldo -= jumlah
        print(f"[BAYAR SUKSES] Pembayaran Rp {jumlah:,} berhasil disetujui! Sisa saldo: Rp {self.saldo:,}")
        return True


# --- PENGUJIAN SOLUSI ---
if __name__ == "__main__":
    print("=" * 60)
    print("[OK] HASIL EKSEKUSI KUNCI JAWABAN DOMPET DIGITAL")
    print("=" * 60)

    dompet = DompetDigital("Anton", "081234567890", 150_000, "246810")

    print(f"Pemilik  : {dompet.pemilik}")
    print(f"No HP    : {dompet.nomor_hp}")  # 0812****7890
    print(f"Saldo    : Rp {dompet.saldo:,}")

    # Coba ganti nomor HP (Harus gagal karena Read-Only)
    try:
        dompet.nomor_hp = "089999999999"
    except AttributeError:
        print("[TERBUKTI AMAN] Nomor HP berstatus Read-Only, tidak bisa diganti!")

    # Coba isi saldo
    print("\n--- Top-up Saldo ---")
    dompet.top_up(50_000)

    # Percobaan Bayar 1: PIN Salah
    print("\n--- Percobaan Bayar 1: PIN Salah ---")
    dompet.bayar(75_000, "000000")

    # Percobaan Bayar 2: Saldo Kurang
    print("\n--- Percobaan Bayar 2: Saldo Kurang ---")
    dompet.bayar(500_000, "246810")

    # Percobaan Bayar 3: Berhasil
    print("\n--- Percobaan Bayar 3: Berhasil ---")
    dompet.bayar(120_000, "246810")

    print(f"\n[INFO] Saldo Akhir {dompet.pemilik}: Rp {dompet.saldo:,}")
    print("=" * 60)
