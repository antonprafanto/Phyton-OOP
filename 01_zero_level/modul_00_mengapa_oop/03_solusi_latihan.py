"""
03_solusi_latihan.py
====================
Modul 0: Mengapa Kita Butuh OOP?

Kunci Jawaban & Pembahasan Latihan Smartphone
"""
import sys

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

class Smartphone:
    def __init__(self, pemilik: str, merk: str, baterai_awal: int):
        self.pemilik = pemilik
        self.merk = merk
        # Pastikan baterai awal berada di rentang 0 - 100
        self.baterai = max(0, min(100, baterai_awal))

    def tampilkan_status(self):
        print(f"[HP] {self.merk} milik {self.pemilik} | Sisa Baterai: {self.baterai}%")

    def gunakan_aplikasi(self, durasi_menit: int):
        pengurangan = (durasi_menit // 10) * 5
        print(f"[PAKAI] {self.pemilik} memakai HP selama {durasi_menit} menit (konsumsi: -{pengurangan}%)...")
        
        # Kurangi baterai, gunakan max(0, ...) agar tidak minus
        self.baterai = max(0, self.baterai - pengurangan)
        
        if self.baterai == 0:
            print("[PERINGATAN] Baterai habis total! HP mati otomatis.")

    def isi_daya(self, persen: int):
        print(f"[CAS] Sedang mengecas HP {self.pemilik} sebesar +{persen}%...")
        
        # Tambah baterai, gunakan min(100, ...) agar tidak tembus 100%
        self.baterai = min(100, self.baterai + persen)
        
        if self.baterai == 100:
            print("[INFO] Baterai sudah penuh (100%)!")


# --- UJI COBA SOLUSI ---
if __name__ == "__main__":
    print("=" * 60)
    print("[OK] HASIL EKSEKUSI KUNCI JAWABAN SMARTPHONE")
    print("=" * 60)
    
    hp_saya = Smartphone("Anton", "Pixel 8", 40)
    hp_saya.tampilkan_status()

    # Pakai 30 menit -> berkurang 15% (40% - 15% = 25%)
    hp_saya.gunakan_aplikasi(30)
    hp_saya.tampilkan_status()

    # Cas 50% -> bertambah (25% + 50% = 75%)
    hp_saya.isi_daya(50)
    hp_saya.tampilkan_status()

    # Cas 80% lagi -> harus mentok di 100% (bukan 155%)
    hp_saya.isi_daya(80)
    hp_saya.tampilkan_status()
    print("=" * 60)
