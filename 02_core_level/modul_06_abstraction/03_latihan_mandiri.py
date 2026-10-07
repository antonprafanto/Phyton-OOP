"""
03_latihan_mandiri.py
=====================
Modul 6: Pilar 4 – Abstraction (Menyembunyikan Kerumitan dengan abc)

TANTANGAN PRAKTEK: SISTEM NOTIFIKASI OMNICHANNEL 📲🔔

Skenario:
Sebuah platform perbankan digital butuh sistem pengiriman notifikasi transaksi
ke nasabah melalui beragam kanal (Email, SMS, dan WhatsApp).
Seluruh layanan notifikasi WAJIB tunduk pada standar kontrak baku 'LayananNotifikasi'!

KETENTUAN YANG HARUS ANDA BUAT:

1. KELAS ABSTRAK INDUK 'LayananNotifikasi(ABC)':
   - @property @abstractmethod: nama_kanal -> str
   - @abstractmethod: kirim_pesan(penerima: str, isi_pesan: str) -> bool

2. CONCRETE CLASS 1: 'NotifikasiEmail':
   - Mewarisi LayananNotifikasi
   - nama_kanal: mengembalikan "Email Server SMTP"
   - kirim_pesan(penerima, isi_pesan):
       * Cek validasi: jika '@' tidak ada di penerima -> cetak gagal, return False
       * Jika valid: cetak "[EMAIL ke {penerima}]: {isi_pesan}", return True

3. CONCRETE CLASS 2: 'NotifikasiSMS':
   - Mewarisi LayananNotifikasi
   - nama_kanal: mengembalikan "SMS Cellular Gateway"
   - kirim_pesan(penerima, isi_pesan):
       * Cek validasi: jika penerima tidak diawali '08' atau '+62' -> cetak nomor tidak valid, return False
       * Jika valid: cetak "[SMS ke {penerima}]: {isi_pesan}", return True

4. CONCRETE CLASS 3: 'NotifikasiWhatsApp':
   - Mewarisi LayananNotifikasi
   - nama_kanal: mengembalikan "WhatsApp Business Cloud"
   - kirim_pesan(penerima, isi_pesan):
       * Cetak "[WA ke {penerima}]: {isi_pesan} (Centang Dua Biru)", return True

5. FUNGSI 'broadcast_pengumuman(layanan: LayananNotifikasi, tujuan: str, info: str)':
   - Cetak "Menghubungi kanal {layanan.nama_kanal}..."
   - Panggil 'layanan.kirim_pesan(tujuan, info)'

Instruksi:
Lengkapi bagian TODO di bawah ini. Kunci jawaban tersedia di '03_solusi_latihan.py'.
"""
import sys
from abc import ABC, abstractmethod

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# ==============================================================
# 1. KELAS ABSTRAK (SURAT KONTRAK BAKU)
# ==============================================================
class LayananNotifikasi(ABC):
    @property
    @abstractmethod
    def nama_kanal(self) -> str:
        pass

    @abstractmethod
    def kirim_pesan(self, penerima: str, isi_pesan: str) -> bool:
        pass


# ==============================================================
# 2. CONCRETE CLASS: EMAIL
# ==============================================================
class NotifikasiEmail(LayananNotifikasi):
    # TODO 1: Implementasikan property nama_kanal ("Email Server SMTP")
    # TODO 2: Implementasikan method kirim_pesan dengan validasi tanda '@'
    pass


# ==============================================================
# 3. CONCRETE CLASS: SMS
# ==============================================================
class NotifikasiSMS(LayananNotifikasi):
    # TODO 3: Implementasikan property nama_kanal ("SMS Cellular Gateway")
    # TODO 4: Implementasikan method kirim_pesan dengan validasi awalan nomor
    pass


# ==============================================================
# 4. CONCRETE CLASS: WHATSAPP
# ==============================================================
class NotifikasiWhatsApp(LayananNotifikasi):
    # TODO 5: Implementasikan property nama_kanal ("WhatsApp Business Cloud")
    # TODO 6: Implementasikan method kirim_pesan
    pass


# ==============================================================
# 5. FUNGSI BROADCAST
# ==============================================================
def broadcast_pengumuman(layanan: LayananNotifikasi, tujuan: str, info: str):
    print(f"\n[BROADCAST] Menghubungi gateway {layanan.nama_kanal}...")
    # TODO 7: Panggil layanan.kirim_pesan(tujuan, info)
    pass


# --- PENGUJIAN KODE ANDA ---
if __name__ == "__main__":
    print("=" * 60)
    print("[TEST] MENGUJI SISTEM NOTIFIKASI OMNICHANNEL")
    print("=" * 60)

    email = NotifikasiEmail()
    sms = NotifikasiSMS()
    wa = NotifikasiWhatsApp()

    # Tes broadcast email
    broadcast_pengumuman(email, "anton@example.com", "OTP Login Anda: 882910")
    broadcast_pengumuman(email, "anton_salah_email", "OTP Login Anda: 882910")  # Harus ditolak

    # Tes broadcast SMS
    broadcast_pengumuman(sms, "08123456789", "Tagihan internet Anda sudah terbit.")

    # Tes broadcast WA
    broadcast_pengumuman(wa, "08123456789", "Promo Diskon Kopi 50% Hari Ini!")
    print("=" * 60)
