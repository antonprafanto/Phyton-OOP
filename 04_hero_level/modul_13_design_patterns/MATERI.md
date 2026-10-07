# 🎭 Modul 13: Design Patterns Populer (Singleton, Factory Method, Strategy)

Selamat datang di Modul 13! Ini adalah puncak pembelajaran arsitektur di **Fase 4: Hero Level**.

Dalam dunia memasak, koki profesional tidak menciptakan teknik memotong bawang atau resep memanggang roti dari nol setiap pagi. Mereka menggunakan **resep standar yang terbukti lezat** (*proven recipe*).

Dalam rekayasa perangkat lunak, resep-resep standar tersebut dikenal sebagai **Design Patterns (Pola Desain)**. Pola desain adalah solusi arsitektural yang telah teruji, disempurnakan, dan disepakati oleh para pakar industri selama puluhan tahun untuk memecahkan masalah-masalah berulang dalam pemrograman berorientasi objek.

Di modul ini, kita akan mempelajari 3 pola desain paling populer dan paling sering digunakan di industri:
1. **Singleton Pattern** *(Creational)*: Menjamin hanya ada 1 instansi objek di seluruh aplikasi.
2. **Factory Method Pattern** *(Creational)*: Memusatkan pembuatan objek agar kode pemanggil tidak terikat ke class konkret.
3. **Strategy Pattern** *(Behavioral)*: Mengisolasi sekumpulan algoritma agar bisa ditukar-pasang saat aplikasi berjalan.

---

## 🎯 Target Pembelajaran
Setelah menyelesaikan modul ini, Anda akan mampu:
1. Memahami apa itu **Design Pattern** dan kapan harus menggunakannya.
2. Menguasai pembuatan **Singleton Pattern** di Python menggunakan metode spesial `__new__()`.
3. Menguasai **Factory Method Pattern** dengan teknik modern *Registry Dictionary* (bebas `if-elif` panjang).
4. Menerapkan **Strategy Pattern** untuk algoritma yang dinamis (*runtime interchangeable*).
5. Menghindari sindrom *Patternitis* (memaksakan design pattern secara berlebihan pada kode sederhana).

---

## 🧭 Peta Tiga Kategori Besar Design Patterns (GoF)

Secara internasional, buku legendaris *Gang of Four* membagi 23 pola desain ke dalam 3 kategori:

```mermaid
mindmap
  root((Kategori Design Patterns))
    Creational Patterns
      Fokus: Cara Objek Diciptakan
      Singleton: Hanya 1 Objek di RAM
      Factory Method: Pabrik Pencipta Objek
    Structural Patterns
      Fokus: Susunan & Komposisi Objek
      Adapter: Jembatan Dua Interface Berbeda
      Decorator: Menambah Fitur Dinamis
      Facade: Menyederhanakan Sistem Rumit
    Behavioral Patterns
      Fokus: Komunikasi & Algoritma Objek
      Strategy: Algoritma yang Bisa Ditukar
      Observer: Notifikasi Langganan Pub/Sub
```

---

## 👑 1. Singleton Pattern (Pola Tunggal)
> *"Ensure a class has only one instance, and provide a global point of access to it."*  
> (Menjamin sebuah class hanya memiliki SATU objek di memori, dan menyediakan akses global ke objek tersebut).

### 🏛️ Analogi Ramah Awam:
Bayangkan **Presiden sebuah negara** atau **Pintu Gerbang Utama sebuah benteng**.  
* Di sebuah negara, tidak boleh ada dua orang presiden yang memimpin secara bersamaan.
* Di aplikasi komputer, ada hal-hal yang **harus tunggal**:
  - **Koneksi Database Pool**: Mencegah 100 koneksi dibuat bersamaan yang bisa membuat server database tumbang.
  - **Sistem Logger Terpusat**: Seluruh aktivitas dicatat ke satu buku log yang sama.
  - **Konfigurasi Global (`config.json`)**: Semua modul membaca setelan yang identik.

```mermaid
sequenceDiagram
    participant App as Kode Aplikasi
    participant Singleton as Kelas Singleton
    App->>Singleton: Minta Objek Pertama kali (cfg1 = Config())
    Singleton-->>App: Buat Objek Baru di RAM (id: 0x01)
    App->>Singleton: Minta Objek Kedua kali (cfg2 = Config())
    Singleton-->>App: Kembalikan Objek Lama (id: 0x01)!
```

### Implementasi Elegan di Python menggunakan `__new__()`:
Di Python, sebelum method `__init__` dijalankan, Python mengeksekusi `__new__` untuk mengalokasikan memori:

```python
class DatabaseConnection:
    _instance = None  # Menyimpan satu-satunya objek di memori

    def __new__(cls):
        if cls._instance is None:
            # Jika belum pernah lahir, lahirkan objek pertama!
            cls._instance = super().__new__(cls)
            cls._instance.status = "Tersambung ke PostgreSQL"
        # Jika sudah ada, kembalikan objek yang lama!
        return cls._instance

db1 = DatabaseConnection()
db2 = DatabaseConnection()

print(db1 is db2)  # Output: True (Dua variabel merujuk ke fisik objek yang persis sama di RAM!)
```

---

## 🏭 2. Factory Method Pattern (Pola Pabrik Objek)
> *"Define an interface for creating an object, but let subclasses decide which class to instantiate."*  
> (Pusatkan pembuatan objek ke dalam sebuah 'Pabrik' agar client tidak perlu tahu nama class konkret pembuatnya).

### 🍔 Analogi Ramah Awam:
Bayangkan Anda pergi ke kasir restoran cepat saji:
* Anda cukup berkata: *"Mbak, pesan Paket Burger Keju!"*
* Kasir meneruskan pesanan ke **Dapur (Factory)**.
* Anda tidak perlu tahu resep roti, cara memanggang daging, atau siapa koki yang memasak. Dapur yang bertugas meracik objek `BurgerKeju` dan menyerahkannya kepada Anda.

```mermaid
flowchart LR
    Client[Client / Kasir] -->|Minta tipe 'pdf'| Factory[EksportirFactory]
    Factory -->|Melahirkan| P1[EksportirPDF]
    Factory -->|Melahirkan| P2[EksportirCSV]
    Factory -->|Melahirkan| P3[EksportirExcel]
```

### Implementasi Modern dengan Factory Registry:
Hindari rantai `if-elif` yang panjang dengan mendaftarkan class ke dalam dictionary:

```python
from abc import ABC, abstractmethod

class Notifikasi(ABC):
    @abstractmethod
    def kirim(self, pesan: str): pass

class EmailNotif(Notifikasi):
    def kirim(self, pesan: str): print(f"[EMAIL] {pesan}")

class SMSNotif(Notifikasi):
    def kirim(self, pesan: str): print(f"[SMS] {pesan}")

class NotifikasiFactory:
    _pendaftar = {
        "email": EmailNotif,
        "sms": SMSNotif
    }

    @classmethod
    def buat_notifikasi(cls, tipe: str) -> Notifikasi:
        kelas_target = cls._pendaftar.get(tipe.lower())
        if not kelas_target:
            raise ValueError(f"Tipe notifikasi '{tipe}' tidak dikenali!")
        return kelas_target()

# Penggunaan di Client:
notif = NotifikasiFactory.buat_notifikasi("email")
notif.kirim("Halo Pelanggan!")
```

---

## 🧭 3. Strategy Pattern (Pola Strategi Algoritma)
> *"Define a family of algorithms, encapsulate each one, and make them interchangeable."*  
> (Kelompokkan keluarga algoritma ke dalam class-class mandiri agar bisa saling ditukar secara dinamis saat aplikasi berjalan).

### 🗺️ Analogi Ramah Awam:
Lihatlah aplikasi **Google Maps**:
Saat Anda ingin pergi dari Jakarta ke Bandung, aplikasi menyediakan beberapa pilihan algoritma rute:
* **Mobil:** Lewat Jalan Tol (Cepat tapi berbayar).
* **Sepeda Motor:** Lewat Jalur Puncak (Bebas tol tapi berliku).
* **Kereta Cepat (Whoosh):** Menggunakan jalur rel khusus.

Aplikasi Google Maps adalah **Context**, sedangkan jenis rute adalah **Strategy**. Anda bisa mengganti strategi rute dengan **1 kali klik tombol** tanpa harus menutup atau merestart aplikasi!

```mermaid
classDiagram
    class Navigator {
        -strategi: StrategiRute
        +set_strategi(strategi)
        +hitung_perjalanan(titik_a, titik_b)
    }

    class StrategiRute {
        <<Interface>>
        +rute(asal, tujuan)
    }

    class RuteMobilTol {
        +rute(asal, tujuan)
    }
    class RuteMotor {
        +rute(asal, tujuan)
    }
    class RuteKeretaCepat {
        +rute(asal, tujuan)
    }

    StrategiRute <|-- RuteMobilTol
    StrategiRute <|-- RuteMotor
    StrategiRute <|-- RuteKeretaCepat
    Navigator o-- StrategiRute : Memakai (HAS-A)
```

### Implementasi Python:
```python
class StrategiRute(ABC):
    @abstractmethod
    def kalkulasi(self, asal: str, tujuan: str) -> str: pass

class RuteMobilTol(StrategiRute):
    def kalkulasi(self, asal: str, tujuan: str) -> str:
        return f"{asal} -> {tujuan} via Tol Cipularang (150 km, 2.5 jam, Biaya Rp 80.000)"

class RuteKeretaCepat(StrategiRute):
    def kalkulasi(self, asal: str, tujuan: str) -> str:
        return f"{asal} -> {tujuan} via Whoosh KCIC (45 menit, Biaya Rp 250.000)"

class AplikasiNavigasi:
    def __init__(self, strategi: StrategiRute):
        self.strategi = strategi

    def set_strategi(self, strategi_baru: StrategiRute):
        self.strategi = strategi_baru

    def cari_jalan(self, asal: str, tujuan: str):
        print(self.strategi.kalkulasi(asal, tujuan))

# Penggunaan:
nav = AplikasiNavigasi(strategi=RuteMobilTol())
nav.cari_jalan("Jakarta", "Bandung")

# Ganti strategi saat runtime:
nav.set_strategi(RuteKeretaCepat())
nav.cari_jalan("Jakarta", "Bandung")
```

---

## ⚠️ 4. Awas Jebakan Pemula! (Common Pitfalls)

### ❌ Jebakan 1: Sindrom *Patternitis* (Kecanduan Design Pattern)
Banyak developer pemula yang baru belajar design pattern merasa gatal ingin memasukkan Singleton, Factory, dan Strategy ke dalam setiap 10 baris kode yang mereka tulis.  
*Ingat:* Design pattern menambah lapisan abstraksi. **Gunakan pola desain HANYA ketika masalah nyata tersebut memang muncul**, bukan untuk pamer kemahiran sintaks!

### ❌ Jebakan 2: Singleton Sebagai Global Variable Terselubung
Jika Anda menaruh terlalu banyak variabel yang bisa diubah-ubah di dalam Singleton, Singleton tersebut berubah menjadi *Global Variable*. Kode akan menjadi sangat sulit untuk diuji (*unit testing*) karena satu test dapat mengubah data dan merusak test lainnya.

### ❌ Jebakan 3: Kebingungan Antara Strategy Pattern vs State Pattern
* **Strategy Pattern:** Algoritma dipilih atau disuntikkan dari luar oleh *client* (misal: user memilih metode pembayaran QRIS vs Kartu).
* **State Pattern:** Objek mengubah perilakunya sendiri secara otomatis dari dalam berdasarkan transisi statusnya (misal: tombol pemutar musik yang berubah fungsi saat status berganti dari *Playing* ke *Paused*).

---

## 🧠 5. Kuis Uji Pemahaman

1. **Method bawaan Python manakah yang bertugas mengontrol alokasi pembuatan objek baru di memori dan paling sering digunakan untuk membuat Singleton?**
<details>
<summary>👁️ Lihat Jawaban</summary>
Method spesial <code>__new__(cls)</code>. Berbeda dengan <code>__init__</code> yang hanya menginisialisasi atribut setelah objek lahir, <code>__new__</code> bertugas mengembalikan fisik objek itu sendiri ke memori.
</details>

2. **Apa keuntungan menggunakan Factory Method dibandingkan langsung mengetik `objek = ClassKonkret()` di kode client?**
<details>
<summary>👁️ Lihat Jawaban</summary>
Kode client menjadi tidak terikat (*loosely coupled*) pada nama class konkret dan proses pembuatannya. Jika suatu saat pembuatan objek butuh validasi tambahan, konfigurasi baru, atau class baru, kita cukup mengubah kode di dalam Factory tanpa menyentuh kode client pemanggil.
</details>

3. **Mengapa Strategy Pattern jauh lebih baik daripada menggunakan blok `if-elif-else` panjang di dalam sebuah method?**
<details>
<summary>👁️ Lihat Jawaban</summary>
Karena Strategy Pattern mematuhi <strong>Open/Closed Principle (OCP)</strong>. Algoritma diisolasi ke dalam class mandiri, sehingga menambah strategi baru tidak perlu mengubah method utama dan strategi tersebut dapat diganti dengan mudah saat aplikasi sedang berjalan (runtime).
</details>

---

## 📂 Berkas Praktik pada Modul Ini
Silakan pelajari dan jalankan berkas-berkas berikut secara bertahap:
1. [`01_singleton_pattern.py`](file:///c:/Users/anton/vibecoding/OOP/04_hero_level/modul_13_design_patterns/01_singleton_pattern.py): Praktik pembuatan Singleton menggunakan `__new__()` dan pembuktian identitas objek di RAM.
2. [`02_factory_dan_strategy.py`](file:///c:/Users/anton/vibecoding/OOP/04_hero_level/modul_13_design_patterns/02_factory_dan_strategy.py): Praktik Factory Method (Eksportir Dokumen) dan Strategy Pattern (Kalkulator Rute & Ongkir).
3. [`03_latihan_mandiri.py`](file:///c:/Users/anton/vibecoding/OOP/04_hero_level/modul_13_design_patterns/03_latihan_mandiri.py): Lembar kerja tantangan sistem Payment Gateway & Ekspor Laporan Keuangan.
4. [`04_solusi_latihan.py`](file:///c:/Users/anton/vibecoding/OOP/04_hero_level/modul_13_design_patterns/04_solusi_latihan.py): Kunci jawaban resmi arsitektur enterprise lengkap.
