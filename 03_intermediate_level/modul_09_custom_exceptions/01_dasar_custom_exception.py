"""
================================================================================
MODUL 9: CUSTOM EXCEPTION & ERROR HANDLING BERBASIS OBJEK
Berkas 01: Dasar Pembuatan Custom Exception & Penyimpanan Metadata
================================================================================
Tujuan Pembelajaran:
1. Mengetahui cara mewarisi class 'Exception' bawaan Python.
2. Memahami cara menyematkan data tambahan (metadata) ke dalam objek error.
3. Menggunakan struktur lengkap: try ... except ... else ... finally.
================================================================================
"""

import sys

# Konfigurasi terminal agar kompatibel dengan encoding Windows / UTF-8
if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass


# ==============================================================================
# 1. MEMBUAT CUSTOM EXCEPTION PERTAMA
# ==============================================================================
class UsiaBelumCukupError(Exception):
    """
    Exception kustom yang dilempar ketika calon pendaftar belum cukup umur.
    Menyimpan metadata berupa usia pendaftar dan syarat usia minimal.
    """
    def __init__(self, usia_input: int, usia_minimal: int = 17):
        self.usia_input = usia_input
        self.usia_minimal = usia_minimal
        self.selisih = usia_minimal - usia_input

        # Membuat pesan error yang jelas dan ramah
        pesan = (
            f"Syarat pendaftaran ditolak! Usia pendaftar ({usia_input} tahun) "
            f"belum memenuhi batas minimal ({usia_minimal} tahun). "
            f"Kurang {self.selisih} tahun lagi."
        )

        # Meneruskan pesan ke class induk Exception
        super().__init__(pesan)


# ==============================================================================
# 2. FUNGSI BISNIS YANG MENGGUNAKAN EXCEPTION KUSTOM
# ==============================================================================
def daftarkan_sim_online(nama: str, usia: int):
    print(f"\n[MEMPROSES] Memeriksa berkas permohonan SIM untuk: '{nama}' (Usia: {usia} thn)...")

    if not isinstance(usia, int) or usia <= 0:
        raise ValueError(f"Usia harus berupa bilangan bulat positif! Diterima: {usia}")

    if usia < 17:
        # Melempar Custom Exception kita dengan membawa metadata
        raise UsiaBelumCukupError(usia_input=usia, usia_minimal=17)

    print(f"[BERHASIL] Selamat {nama}, Anda memenuhi syarat usia dan permohonan SIM diproses!")
    return f"SIM-{nama[:3].upper()}-9902"


# ==============================================================================
# 3. PENGUJIAN DAN DEMONSTRASI PENANGANAN ERROR
# ==============================================================================
if __name__ == "__main__":
    print("=" * 65)
    print("[DEMO] DASAR CUSTOM EXCEPTION DENGAN METADATA")
    print("=" * 65)

    daftar_pemohon = [
        ("Budi Prasetyo", 22),   # Memenuhi syarat
        ("Riko Bocil", 14),      # Usia belum cukup -> UsiaBelumCukupError
        ("Maya Lestari", 16),    # Usia belum cukup -> UsiaBelumCukupError
        ("Jaka Tarub", 19)       # Memenuhi syarat
    ]

    for nama, usia in daftar_pemohon:
        try:
            nomor_sim = daftarkan_sim_online(nama, usia)
        except UsiaBelumCukupError as err:
            # Di sini kita bisa mengakses metadata error secara langsung!
            print(f"[DITOLAK] Alasan: {err}")
            print(f"  -> Usia Pendaftar : {err.usia_input} tahun")
            print(f"  -> Usia Minimal   : {err.usia_minimal} tahun")
            print(f"  -> Silakan daftar kembali {err.selisih} tahun mendatang.")
        except ValueError as val_err:
            print(f"[ERROR INPUT] Format input salah: {val_err}")
        else:
            # Blok 'else' HANYA berjalan jika blok 'try' sukses tanpa error!
            print(f"  -> Nomor Registrasi Penerbitan: {nomor_sim}")
        finally:
            # Blok 'finally' SELALU berjalan baik sukses maupun gagal (misal untuk tutup sesi)
            print("  -> Status pemeriksaan berkas selesai dicatat.")

    print("\n" + "=" * 65)
    print("[OK] Selesai: Custom exception berhasil dibuat dan menangkap error terstruktur.")
    print("=" * 65)
