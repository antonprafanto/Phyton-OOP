"""
================================================================================
MODUL 11: HUBUNGAN ANTAR OBJEK (OBJECT RELATIONSHIPS)
Berkas 04: Solusi Resmi & Pembahasan Arsitektur PC & Programmer
================================================================================
STUDI KASUS: SISTEM SIMULASI PERAKITAN PC & PENGGUNA KOMPUTER
================================================================================
"""

import sys

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass


# ==============================================================================
# 1. KOMPONEN INTERNAL (KOMPOSISI: part-of kuat)
# ==============================================================================
class Processor:
    def __init__(self, model: str, speed_ghz: float, cores: int):
        self.model = model
        self.speed_ghz = speed_ghz
        self.cores = cores

    def info(self) -> str:
        return f"{self.model} ({self.cores} Cores @ {self.speed_ghz:.1f} GHz)"


class RAM:
    def __init__(self, kapasitas_gb: int, tipe_ddr: str):
        self.kapasitas_gb = kapasitas_gb
        self.tipe_ddr = tipe_ddr

    def info(self) -> str:
        return f"{self.kapasitas_gb} GB {self.tipe_ddr.upper()}"


# ==============================================================================
# 2. KOMPONEN EKSTERNAL (AGREGASI: has-a longgar)
# ==============================================================================
class Aksesoris:
    def __init__(self, nama: str, jenis: str):
        self.nama = nama
        self.jenis = jenis

    def __repr__(self) -> str:
        return f"Aksesoris('{self.nama}', Jenis: {self.jenis})"


# ==============================================================================
# 3. KOMPUTER (WADAH UTAMA)
# ==============================================================================
class Komputer:
    def __init__(self, nama_pc: str, proc_model: str, proc_ghz: float, proc_cores: int, ram_gb: int, ram_ddr: str):
        self.nama_pc = nama_pc

        # HUBUNGAN 1: KOMPOSISI
        # Processor dan RAM diciptakan DI DALAM constructor Komputer
        self.processor = Processor(model=proc_model, speed_ghz=proc_ghz, cores=proc_cores)
        self.ram = RAM(kapasitas_gb=ram_gb, tipe_ddr=ram_ddr)

        # HUBUNGAN 2: AGREGASI
        # Wadah untuk aksesoris yang dibuat di luar dan bisa dicopot-pasang
        self.daftar_aksesoris: list[Aksesoris] = []

    def colok_aksesoris(self, aksesoris: Aksesoris):
        self.daftar_aksesoris.append(aksesoris)
        print(f"[AGREGASI] Menghubungkan {aksesoris.jenis} '{aksesoris.nama}' ke {self.nama_pc}.")

    def cabut_aksesoris(self, nama_aksesoris: str) -> Aksesoris | None:
        for idx, item in enumerate(self.daftar_aksesoris):
            if item.nama.lower() == nama_aksesoris.lower():
                dicabut = self.daftar_aksesoris.pop(idx)
                print(f"[AGREGASI] Mencabut {dicabut.jenis} '{dicabut.nama}' dari {self.nama_pc}.")
                return dicabut
        print(f"[NOTIF] Aksesoris '{nama_aksesoris}' tidak ditemukan di {self.nama_pc}.")
        return None

    def cetak_spesifikasi(self):
        print("\n+" + "=" * 56 + "+")
        print(f"|            SPESIFIKASI RIG: {self.nama_pc:<24} |")
        print("+" + "=" * 56 + "+")
        print(f"| Processor : {self.processor.info():<42} |")
        print(f"| RAM       : {self.ram.info():<42} |")
        print("+" + "-" * 56 + "+")
        print(f"| Periferal Terpasang ({len(self.daftar_aksesoris)} unit):{' ' * 27} |")
        if not self.daftar_aksesoris:
            print(f"|   (Belum ada periferal eksternal yang dicolok){' ' * 9} |")
        else:
            for item in self.daftar_aksesoris:
                teks_item = f"- [{item.jenis}] {item.nama}"
                print(f"|   {teks_item:<50} |")
        print("+" + "=" * 56 + "+\n")


# ==============================================================================
# 4. PROGRAMMER (ASOSIASI: uses-a)
# ==============================================================================
class Programmer:
    def __init__(self, nama: str, bahasa: str):
        self.nama = nama
        self.bahasa = bahasa

    # HUBUNGAN 3: ASOSIASI
    # Programmer menggunakan PC sebagai alat kerja lewat parameter fungsi
    def koding(self, pc: Komputer, nama_proyek: str):
        print(f"[ASOSIASI] {self.nama} membuka VS Code di PC '{pc.nama_pc}'...")
        print(f"  -> Sedang memprogram proyek : '{nama_proyek}'")
        print(f"  -> Bahasa Pemrograman       : {self.bahasa}")
        print(f"  -> Spesifikasi Mesin        : {pc.processor.model} | {pc.ram.kapasitas_gb} GB RAM")
        print(f"  -> Kompilasi Sukses! Proyek '{nama_proyek}' berjalan lancar.\n")


# ==============================================================================
# PENGUJIAN DAN PEMBUKTIAN KUNCI JAWABAN
# ==============================================================================
if __name__ == "__main__":
    print("=" * 65)
    print("[SOLUSI] PENGUJIAN LENGKAP ARSITEKTUR KOMPUTER & PROGRAMMER")
    print("=" * 65)

    # 1. Merakit Komputer (Komposisi)
    rig_anton = Komputer(
        nama_pc="Rig-Workstation-2026",
        proc_model="AMD Ryzen 9 7950X",
        proc_ghz=5.7,
        proc_cores=16,
        ram_gb=64,
        ram_ddr="DDR5"
    )

    # 2. Membuat Aksesoris di Luar (Agregasi)
    mouse_logi = Aksesoris("Logitech MX Master 3S", "Mouse")
    keyboard_keychron = Aksesoris("Keychron Q1 Max", "Keyboard")
    monitor_lg = Aksesoris("LG UltraFine 4K 32 Inch", "Monitor")

    # Colok aksesoris ke PC
    rig_anton.colok_aksesoris(mouse_logi)
    rig_anton.colok_aksesoris(keyboard_keychron)
    rig_anton.colok_aksesoris(monitor_lg)

    # Cetak Spesifikasi Lengkap
    rig_anton.cetak_spesifikasi()

    # 3. Programmer Menggunakan PC (Asosiasi)
    anton = Programmer("Anton Prafanto", "Python 3.12")
    anton.koding(rig_anton, "SmartPOS Enterprise System")

    # 4. Pembuktian Siklus Hidup Agregasi:
    # Jika rig_anton dijual / dihapus dari RAM, apakah mouse_logi ikut musnah?
    print("--- Pembuktian Independensi Agregasi ---")
    mouse_cabutan = rig_anton.cabut_aksesoris("Logitech MX Master 3S")
    del rig_anton  # Komputer dihancurkan

    # mouse_cabutan dan keyboard_keychron tetap eksis dan hidup!
    print(f"Mouse setelah PC dihapus : {mouse_cabutan} (MASIH EKSIS!)")
    print(f"Keyboard setelah PC dihapus : {keyboard_keychron} (MASIH EKSIS!)")

    print("\n" + "=" * 65)
    print("[OK] Selesai: Tiga jenis hubungan objek terbukti dan terverifikasi 100%.")
    print("=" * 65)
