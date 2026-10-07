"""
03_latihan_mandiri.py
=====================
Modul 3: Pilar 1 – Encapsulation & Gaya Elegan @property

TANTANGAN PRAKTEK: DOMPET DIGITAL AMAN (Safe E-Wallet) 📱💳

Skenario:
Anda ditugaskan merancang class 'DompetDigital' untuk aplikasi fintech.
Aplikasi ini harus tahan dari manipulasi saldo ilegal dan kebocoran PIN!

KETENTUAN YANG HARUS ANDA BUAT:
1. ATRIBUT DI DALAM __init__:
   - pemilik: str (Public)
   - _nomor_hp: str (Disimpan di variabel protected, misal: "081234567890")
   - _saldo: int (Disimpan di variabel protected, saldo awal minimal 0)
   - __pin: str (Private mutlak! misal: "123456")

2. PROPERTY & SETTER:
   - nomor_hp: Jadikan READ-ONLY PROPERTY yang mengembalikan nomor HP tersensor!
               Contoh: "0812****7890" (4 angka awal + '****' + 4 angka akhir).
   - saldo: Gunakan @property untuk membaca saldo.
            Gunakan @saldo.setter untuk validasi: Saldo tidak boleh diisi nilai negatif!

3. METHOD TRANSAKSI:
   - top_up(jumlah: int): menambah saldo (gunakan setter saldo).
   - bayar(jumlah: int, input_pin: str):
       * Cek 1: Periksa apakah input_pin cocok dengan __pin. Jika salah, batalkan!
       * Cek 2: Periksa apakah saldo cukup untuk membayar jumlah tersebut.
       * Jika lolos: kurangi saldo dan cetak struk pembayaran berhasil.

Instruksi:
Lengkapi bagian TODO di bawah ini. Kunci jawaban tersedia di '03_solusi_latihan.py'.
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
        self.__pin = pin  # Private

    # TODO 1: Buat Read-Only Property 'nomor_hp' dengan sensor bintang (0812****7890)
    @property
    def nomor_hp(self) -> str:
        # Kembalikan nomor HP yang 4 angka tengahnya disensor
        pass

    # TODO 2: Buat Getter @property 'saldo'
    @property
    def saldo(self) -> int:
        pass

    # TODO 3: Buat Setter @saldo.setter dengan validasi tidak boleh negatif
    @saldo.setter
    def saldo(self, nilai_baru: int):
        pass

    # TODO 4: Method top_up(jumlah)
    def top_up(self, jumlah: int):
        if jumlah > 0:
            self.saldo += jumlah
            print(f"[TOP-UP] Berhasil isi saldo Rp {jumlah:,} untuk {self.pemilik}")
        else:
            print("[TOP-UP GAGAL] Jumlah isi saldo harus lebih dari 0!")

    # TODO 5: Method bayar(jumlah, input_pin)
    def bayar(self, jumlah: int, input_pin: str):
        # 1. Periksa kecocokan PIN
        # 2. Periksa kecukupan saldo
        # 3. Kurangi saldo jika valid
        pass


# --- PENGUJIAN KODE ANDA ---
if __name__ == "__main__":
    print("=" * 60)
    print("[TEST] MENGUJI DOMPET DIGITAL AMAN")
    print("=" * 60)

    dompet = DompetDigital("Anton", "081234567890", 150_000, "246810")

    print(f"Pemilik  : {dompet.pemilik}")
    print(f"No HP    : {dompet.nomor_hp}")  # Harus tersensor: 0812****7890
    print(f"Saldo    : Rp {dompet.saldo:,}")

    # Coba ubah nomor HP secara ilegal (harus error / ditolak):
    try:
        dompet.nomor_hp = "089999999999"
    except AttributeError:
        print("[AMAN] Nomor HP tidak bisa diubah sembarangan (Read-only)!")

    # Top Up
    dompet.top_up(50_000)

    # Pembayaran dengan PIN salah
    print("\n--- Percobaan Bayar 1: PIN Salah ---")
    dompet.bayar(75_000, "000000")

    # Pembayaran dengan PIN benar tapi saldo tidak cukup
    print("\n--- Percobaan Bayar 2: Saldo Kurang ---")
    dompet.bayar(500_000, "246810")

    # Pembayaran sah
    print("\n--- Percobaan Bayar 3: Berhasil ---")
    dompet.bayar(120_000, "246810")
    print(f"Sisa Saldo Akhir: Rp {dompet.saldo:,}")
    print("=" * 60)
