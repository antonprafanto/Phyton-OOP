"""
03_latihan_mandiri.py
=====================
Modul 0: Mengapa Kita Butuh OOP?

TANTANGAN UNTUK ANDA:
Bedahlah sebuah benda nyata yang ada di genggaman Anda: SMARTPHONE!

LENGKAPI KODE DI BAWAH INI:
1. Sebuah Smartphone memiliki data (Atribut):
   - pemilik (contoh: "Anton")
   - merk (contoh: "Samsung Galaxy" / "iPhone")
   - baterai (angka 0 sampai 100)

2. Smartphone memiliki kemampuan (Method):
   - tampilkan_status(): mencetak nama pemilik, merk, dan sisa baterai saat ini.
   - gunakan_aplikasi(durasi_menit): setiap 10 menit pemakaian, baterai berkurang 5%.
   - isi_daya(persen): menambah baterai, maksimal tidak boleh lebih dari 100%.

Instruksi:
Gantilah bagian TODO di bawah ini dengan logika yang benar!
Jika Anda bingung, jangan khawatir, Anda bisa intip jawabannya di file '03_solusi_latihan.py'.
"""
import sys

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

class Smartphone:
    def __init__(self, pemilik: str, merk: str, baterai_awal: int):
        # TODO 1: Simpan parameter ke dalam atribut self
        self.pemilik = pemilik
        self.merk = merk
        self.baterai = baterai_awal

    def tampilkan_status(self):
        # TODO 2: Cetak status hp dengan rapi
        print(f"[HP] {self.merk} milik {self.pemilik} | Sisa Baterai: {self.baterai}%")

    def gunakan_aplikasi(self, durasi_menit: int):
        # TODO 3: Hitung baterai yang berkurang (tiap 10 menit berkurang 5%)
        # Kurangi self.baterai, tapi jangan sampai di bawah 0%!
        pengurangan = (durasi_menit // 10) * 5
        print(f"[PAKAI] {self.pemilik} memakai HP selama {durasi_menit} menit...")
        
        # Lengkapi logika pengurangan baterai di bawah ini:
        pass

    def isi_daya(self, persen: int):
        # TODO 4: Tambahkan self.baterai, tapi pastikan tidak melebihi 100%!
        print(f"[CAS] Sedang mengecas HP {self.pemilik} sebesar +{persen}%...")
        
        # Lengkapi logika isi daya di bawah ini:
        pass


# --- UJI COBA KODE ANDA DI SINI ---
if __name__ == "__main__":
    print("=" * 60)
    print("[TEST] MENGUJI OBJEK SMARTPHONE")
    print("=" * 60)
    
    # 1. Lahirkan objek HP
    hp_saya = Smartphone("Anton", "Pixel 8", 40)
    hp_saya.tampilkan_status()

    # 2. Coba gunakan
    hp_saya.gunakan_aplikasi(30)  # Dipakai 30 menit -> baterai berkurang 15%
    hp_saya.tampilkan_status()

    # 3. Coba cas
    hp_saya.isi_daya(50)          # Dicas 50%
    hp_saya.tampilkan_status()

    # 4. Coba cas berlebihan (apakah mentok di 100%?)
    hp_saya.isi_daya(80)
    hp_saya.tampilkan_status()
