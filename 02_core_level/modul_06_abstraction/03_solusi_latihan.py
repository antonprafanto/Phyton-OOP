"""
03_solusi_latihan.py
====================
Modul 6: Pilar 4 – Abstraction (Menyembunyikan Kerumitan dengan abc)

Kunci Jawaban & Pembahasan Latihan Sistem Notifikasi Omnichannel 📲🔔
"""
import sys
from abc import ABC, abstractmethod

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# ==============================================================
# 1. KELAS ABSTRAK INDUK (KONTRAK STANDAR)
# ==============================================================
class LayananNotifikasi(ABC):
    @property
    @abstractmethod
    def nama_kanal(self) -> str:
        """Setiap kanal wajib memiliki nama identitas kanal."""
        pass

    @abstractmethod
    def kirim_pesan(self, penerima: str, isi_pesan: str) -> bool:
        """Setiap kanal wajib mengimplementasikan protokol kirim_pesan."""
        pass


# ==============================================================
# 2. CONCRETE CLASS 1: EMAIL
# ==============================================================
class NotifikasiEmail(LayananNotifikasi):
    @property
    def nama_kanal(self) -> str:
        return "Email Server SMTP"

    def kirim_pesan(self, penerima: str, isi_pesan: str) -> bool:
        if "@" not in penerima:
            print(f"[EMAIL DITOLAK] Alamat email '{penerima}' tidak valid (kurang '@')!")
            return False
        
        print(f"[EMAIL] Terkirim ke: {penerima}")
        print(f"        Subjek: Notifikasi Bank | Pesan: {isi_pesan}")
        return True


# ==============================================================
# 3. CONCRETE CLASS 2: SMS
# ==============================================================
class NotifikasiSMS(LayananNotifikasi):
    @property
    def nama_kanal(self) -> str:
        return "SMS Cellular Gateway"

    def kirim_pesan(self, penerima: str, isi_pesan: str) -> bool:
        if not (penerima.startswith("08") or penerima.startswith("+62")):
            print(f"[SMS DITOLAK] Nomor HP '{penerima}' tidak valid untuk SMS!")
            return False

        print(f"[SMS] Terkirim ke nomor seluler: {penerima}")
        print(f"      Pesan SMS: {isi_pesan}")
        return True


# ==============================================================
# 4. CONCRETE CLASS 3: WHATSAPP
# ==============================================================
class NotifikasiWhatsApp(LayananNotifikasi):
    @property
    def nama_kanal(self) -> str:
        return "WhatsApp Business Cloud API"

    def kirim_pesan(self, penerima: str, isi_pesan: str) -> bool:
        print(f"[WHATSAPP] Terkirim via WA API ke: {penerima}")
        print(f"           Pesan WA: \"{isi_pesan}\" (Status: Terkirim centang dua)")
        return True


# ==============================================================
# 5. FUNGSI BROADCAST STANDAR
# ==============================================================
def broadcast_pengumuman(layanan: LayananNotifikasi, tujuan: str, info: str):
    print(f"\n[BROADCAST] Menghubungi gateway '{layanan.nama_kanal}'...")
    status = layanan.kirim_pesan(tujuan, info)
    if status:
        print(">>> Status Pengiriman: [SUKSES]")
    else:
        print(">>> Status Pengiriman: [GAGAL]")


# --- PENGUJIAN SOLUSI ---
if __name__ == "__main__":
    print("=" * 60)
    print("[OK] HASIL EKSEKUSI KUNCI JAWABAN NOTIFIKASI OMNICHANNEL")
    print("=" * 60)

    email = NotifikasiEmail()
    sms = NotifikasiSMS()
    wa = NotifikasiWhatsApp()

    # 1. Kirim Email Sah & Tidak Sah
    broadcast_pengumuman(email, "anton@gmail.com", "Kode OTP verifikasi Anda: 882910")
    broadcast_pengumuman(email, "anton_tanpa_domain", "Kode OTP verifikasi Anda: 882910")

    # 2. Kirim SMS Sah
    broadcast_pengumuman(sms, "08123456789", "Tagihan bulanan Anda: Rp 350.000 sudah terbayar.")

    # 3. Kirim WhatsApp Sah
    broadcast_pengumuman(wa, "08123456789", "Selamat! Anda mendapatkan promo diskon 50%.")
    print("=" * 60)
