# 📘 SILABUS & ROADMAP BELAJAR: PYTHON OOP (FROM ZERO TO HERO)
> **Target Audiens**: Pemula & Orang Awam (Tanpa latar belakang programming rumit)  
> **Bahasa Pemrograman**: Python 3.x  
> **Metode**: Analogi Kehidupan Nyata $\rightarrow$ Masalah Nyata $\rightarrow$ Kode Bertahap $\rightarrow$ Jebakan Pemula $\rightarrow$ Mini Latihan  

---

## 🧭 Progress Tracker (Status Pembelajaran)

Gunakan daftar centang di bawah ini untuk memantau perjalanan belajar kita agar selalu *on the track*:

| Status | Modul | Topik Utama | Tingkat |
| :---: | :--- | :--- | :---: |
| [x] | **Modul 0** | Mengapa Butuh OOP? (Mental Model Dunia Nyata) | Zero |
| [ ] | **Modul 1** | Melahirkan Objek Pertama (Class, Object, Constructor, & `self`) | Zero |
| [ ] | **Modul 2** | Variabel Milik Siapa? (Instance Attribute vs Class Attribute) | Zero |
| [ ] | **Modul 3** | Pilar 1: Encapsulation & Gaya Elegan `@property` | Core |
| [ ] | **Modul 4** | Pilar 2: Inheritance (Pewarisan, `super()`, & Multiple Inheritance) | Core |
| [ ] | **Modul 5** | Pilar 3: Polymorphism & Filosofi *Duck Typing* | Core |
| [ ] | **Modul 6** | Pilar 4: Abstraction (Menyembunyikan Kerumitan dengan `abc`) | Core |
| [ ] | **Modul 7** | Python Superpowers: Magic / Dunder Methods (`__str__`, `__eq__`, dll.) | Intermediate |
| [ ] | **Modul 8** | Metode Spesial: `@classmethod` vs `@staticmethod` | Intermediate |
| [ ] | **Modul 9** | Custom Exception: Membuat Pesan Error Sendiri dengan OOP | Intermediate |
| [ ] | **Modul 10** | Modern Python Shortcut: `@dataclass` | Intermediate |
| [ ] | **Modul 11** | Hubungan Antar Objek: Association, Aggregation, & Composition | Hero |
| [ ] | **Modul 12** | Prinsip S.O.L.I.D untuk Pemula (Menulis Kode Rapi & Tahan Uji) | Hero |
| [ ] | **Modul 13** | Design Patterns Populer (Singleton, Factory, Strategy) | Hero |
| [ ] | **Modul 14** | Proyek Akhir (Capstone Project: SmartPOS / Text-RPG) | Hero |

---

## 📖 Rincian Kurikulum Modul per Modul

---

### 🟢 FASE 1: MENTAL MODEL & FONDASI DASAR (LEVEL 0 - ZERO)
*Tujuan: Membangun intuisi berpikir objek sebelum mengetik kode rumit.*

#### **Modul 0: Mengapa Kita Butuh OOP?**
* **Analogi**: Resep Masakan di Kertas Panjang (Prosedural) vs Stasiun Dapur Restoran Modern (OOP).
* **Masalah Nyata**: Mengapa kode non-OOP mudah kusut ("kode spageti") ketika aplikasi bertambah besar.
* **Inti Konsep**:
  * Cara membedah dunia menjadi kumpulan objek.
  * Elemen dasar objek: **Atribut** (Data/Ciri-ciri) dan **Method** (Perilaku/Aksi).
* **Latihan Awam**: Membedah benda nyata di sekitar (Kucing, Kopi, Smartphone, Akun Instagram).

#### **Modul 1: Melahirkan Objek Pertama (Class, Object, & Constructor)**
* **Analogi**: Cetakan Martabak (Class) vs Martabak yang Siap Dimakan (Object).
* **Inti Konsep**:
  * Sintaks kata kunci `class` dan cara instansiasi objek.
  * Momen kelahiran objek: Fungsi `__init__()` (Constructor).
  * Menguak rahasia `self`: Mengapa objek butuh mengenali dirinya sendiri?
* **Jebakan Pemula**: Lupa menulis `self` dan error `TypeError: takes 0 positional arguments but 1 was given`.
* **Mini Latihan**: Membuat class `Kucing` dan melahirkan beberapa kucing dengan warna serta suara berbeda.

#### **Modul 2: Variabel Milik Siapa? (Instance vs Class Attributes)**
* **Analogi**: Warna Baju Tiap Individu (Instance) vs Gravitasi Bumi yang Berlaku untuk Semua Orang (Class).
* **Inti Konsep**:
  * Kapan variabel menempel pada *satu objek khusus* vs menempel pada *seluruh cetakan class*.
  * Menghitung total objek yang pernah dibuat secara otomatis.
* **Jebakan Fatal**: Bahaya meletakkan tipe data `list` di class level (data satu user bisa bocor ke user lain).
* **Mini Latihan**: Sistem absensi siswa sederhana.

---

### 🟡 FASE 2: 4 PILAR SAKTI OOP DALAM PYTHON (LEVEL 1 - CORE)
*Tujuan: Membuat kode aman, terstruktur, rapi, dan mudah dikembangkan.*

#### **Modul 3: Pilar 1 – Encapsulation & Gaya Elegan `@property`**
* **Analogi**: Kap Mesin Mobil & Saklar Lampu (Cukup tekan saklar tanpa menyentuh kabel listrik telanjang).
* **Inti Konsep**:
  * Konvensi hak akses Python: Public (`nama`), Protected (`_nama`), Private (`__nama`).
  * Memahami *Name Mangling* di Python.
  * Menolak cara kuno `get_nama()` & `set_nama()`.
  * Menggunakan `@property` dan `@nama.setter` untuk validasi otomatis (contoh: saldo tidak boleh negatif).
* **Mini Latihan**: Membuat rekening bank digital yang aman dari manipulasi saldo liar.

#### **Modul 4: Pilar 2 – Inheritance (Pewarisan & Prinsip DRY)**
* **Analogi**: DNA Keluarga (Kendaraan $\rightarrow$ Mobil $\rightarrow$ Mobil Listrik Tesla).
* **Inti Konsep**:
  * Prinsip DRY (*Don't Repeat Yourself*): Menghemat kode dengan mewarisi sifat umum.
  * Memanggil kemampuan orang tua dengan `super().__init__()`.
  * Khas Python: *Multiple Inheritance* (Punya dua orang tua) & sekilas MRO (*Method Resolution Order*).
* **Jebakan Pemula**: Terlalu dalam membuat rantai warisan (anak, cucu, cicit) hingga kode sulit diubah.
* **Mini Latihan**: Sistem karyawan kantor (Manager, Programmer, Desainer mewarisi class `Karyawan`).

#### **Modul 5: Pilar 3 – Polymorphism & Filosofi *Duck Typing***
* **Analogi**: Colokan USB (Mau dicolok mouse, flashdisk, keyboard, port-nya merespons dengan cara masing-masing).
* **Inti Konsep**:
  * *Method Overriding*: Menimpa aksi orang tua dengan aksi baru yang lebih spesifik.
  * *Duck Typing* khas Python: *"Jika dia berjalan seperti bebek dan bersuara seperti bebek, maka dia adalah bebek!"*.
* **Mini Latihan**: Sistem pembayaran toko (Metode Tunai, QRIS, dan Transfer merespons perintah `proses_bayar()`).

#### **Modul 6: Pilar 4 – Abstraction (Menyembunyikan Kerumitan)**
* **Analogi**: Remote TV Universal (Tombol `Power` ada di semua remote, tapi tiap merek TV punya cara kerja berbeda di dalamnya).
* **Inti Konsep**:
  * Modul bawaan Python: `from abc import ABC, abstractmethod`.
  * Membuat "kontrak wajib": Mengharuskan class anak memiliki fungsi tertentu.
* **Jebakan Pemula**: Berusaha melahirkan objek langsung dari class abstrak (`TypeError`).
* **Mini Latihan**: Desain driver database (MySQL, PostgreSQL) yang wajib tunduk pada standar perintah baku.

---

### 🟠 FASE 3: PYTHON SUPERPOWERS (LEVEL 2 - INTERMEDIATE)
*Tujuan: Menguasai fitur-fitur ajaib Python yang membedakan pemula dari programmer berpengalaman.*

#### **Modul 7: Magic / Dunder Methods & Object Serialization**
* **Inti Konsep**:
  * Mempercantik tampilan objek: `__str__` (untuk user) vs `__repr__` (untuk programmer/debug).
  * Menghitung isi objek: `__len__`.
  * Membandingkan dua objek: Mengapa `a == b` butuh `__eq__`.
  * Operator Overloading: `__add__` (Membuat objek bisa dijumlahkan dengan tanda `+`).
  * **Object Serialization (Menyimpan Objek)**: Mengubah objek menjadi Dictionary & JSON (`to_dict()` / `from_dict()`) agar data tidak hilang saat program ditutup.
* **Mini Latihan**: Membuat objek `Dompet` yang bisa digabungkan isinya dengan `dompet1 + dompet2` dan disimpan ke file JSON.

#### **Modul 8: Metode Spesial (`@classmethod` vs `@staticmethod`)**
* **Inti Konsep**:
  * *Instance Method* (parameter `self`): Bekerja pada satu objek individu.
  * *Class Method* (parameter `cls`): Bekerja pada tingkat cetakan class (digunakan sebagai *Alternative Constructor*, misal: membuat objek dari format String atau JSON).
  * *Static Method* (tanpa `self`/`cls`): Fungsi pembantu yang relevan berada di dalam class.
* **Mini Latihan**: Membuat class `User` yang bisa dibuat langsung dari format teks `"Budi, budi@email.com, 25"`.

#### **Modul 9: Custom Exception & Error Handling Berbasis Objek**
* **Analogi**: Kartu Kuning & Kartu Merah Wasit Sepak Bola.
* **Inti Konsep**:
  * Mengapa `print("Error!")` adalah cara yang buruk untuk menangani kesalahan program.
  * Membuat class error sendiri dengan mewarisi `Exception` (misal: `SaldoKurangError`, `AkunTerkunciError`).
  * Menggunakan `raise` dan menangkapnya dengan blok `try...except`.
* **Mini Latihan**: Simulasi mesin ATM yang menolak transaksi berbahaya secara tertib.

#### **Modul 10: Modern Python Shortcut (`@dataclass`) & Type Hinting**
* **Inti Konsep**:
  * Memperkenalkan modul bawaan `dataclasses` (Python 3.7+).
  * Menulis **Type Hinting Modern** pada atribut & fungsi objek (membantu IDE mendeteksi typo dan salah tipe data).
  * Mengapa developer modern menyukai `@dataclass` untuk kelas penyimpan data murni.
  * Mengurangi boilerplate kode hingga 70% tanpa kehilangan fitur OOP.
* **Mini Latihan**: Membuat katalog produk e-commerce dalam hitungan detik lengkap dengan petunjuk tipe data.

---

### 🔴 FASE 4: ARSITEKTUR KELAS INDUSTRI (LEVEL 3 - HERO)
*Tujuan: Menulis kode skala profesional yang mudah dirawat, mudah diperluas, dan tidak rapuh.*

#### **Modul 11: Hubungan Antar Objek (Relasi Dunia Nyata)**
* **Inti Konsep**:
  * **Association**: Hubungan saling kenal (Dokter & Pasien).
  * **Aggregation**: Hubungan tim yang lepas (Perpustakaan & Buku).
  * **Composition**: Hubungan hidup-mati (Manusia & Jantung).
  * **Golden Rule**: *"Pilihlah Composition daripada Inheritance"*.
* **Mini Latihan**: Membangun model `Komputer` yang terdiri dari `Processor`, `RAM`, dan `Storage`.

#### **Modul 12: Prinsip S.O.L.I.D untuk Pemula**
* **S - Single Responsibility Principle**: Satu class hanya boleh punya satu alasan untuk berubah.
* **O - Open/Closed Principle**: Terbuka untuk penambahan fitur baru, tertutup dari mengubah kode lama yang sudah stabil.
* **L - Liskov Substitution Principle**: Objek anak harus bisa menggantikan induk tanpa merusak program.
* **I - Interface Segregation Principle**: Jangan paksa class memiliki fungsi yang tidak dibutuhkannya.
* **D - Dependency Inversion Principle**: Bergantunglah pada standar/abstraksi, bukan pada detail implementasi konkret.
* **Studi Kasus**: Membedah kode "buruk" dan mengubahnya menjadi kode bersih (Clean Code) berbasis SOLID.

#### **Modul 13: Design Patterns Terpopuler di Python**
* **Singleton Pattern**: Memastikan hanya ada 1 instance di memori (misal: Konfigurasi / Logger aplikasi).
* **Factory Pattern**: Pabrik pembuat objek yang fleksibel sesuai kebutuhan.
* **Strategy Pattern**: Mengganti strategi/algoritma secara dinamis saat program berjalan (misal: algoritma diskon musiman).

---

### 🏆 FASE 5: PROYEK AKHIR / CAPSTONE PROJECT (HERO LEVEL)
*Tujuan: Mempraktikkan seluruh ilmu dari Modul 0 sampai 13 dalam satu aplikasi utuh dan fungsional.*

#### **Modul 14: Membangun Aplikasi Nyata dari Nol**
Pilihan Proyek yang akan kita kerjakan bersama:
1. **Pilihan A: SmartPOS (Sistem Kasir & Loyalitas Pelanggan)**
   * Fitur: Manajemen Katalog Produk (`@dataclass`), Diskon Member (`Strategy Pattern`), Keamanan Saldo Kasir (`Encapsulation` & `@property`), Log Transaksi (`Singleton Logger`), Multi-metode Pembayaran (`Polymorphism`), Custom Error Transaksi.
2. **Pilihan B: HeroQuest (Text-Based RPG Adventure)**
   * Fitur: Karakter & Hero Class (`Inheritance`), Sistem Senjata & Armor (`Composition`), Serangan & Efek Skill (`Polymorphism` & `Abstract Class`), Battle Turn Engine, Custom Game Exceptions.

---

## 📁 Rencana Struktur Direktori Pembelajaran
Materi dan kode latihan akan disimpan dalam struktur folder yang rapi seperti berikut:

```text
OOP/
├── SILABUS.md                  <-- File panduan & pemantau progres utama (File Ini)
├── 01_zero_level/
│   ├── modul_00_mengapa_oop/
│   ├── modul_01_class_object/
│   └── modul_02_instance_vs_class_attr/
├── 02_core_level/
│   ├── modul_03_encapsulation/
│   ├── modul_04_inheritance/
│   ├── modul_05_polymorphism/
│   └── modul_06_abstraction/
├── 03_intermediate_level/
│   ├── modul_07_dunder_methods/
│   ├── modul_08_special_methods/
│   ├── modul_09_custom_exceptions/
│   └── modul_10_dataclasses/
├── 04_hero_level/
│   ├── modul_11_object_relationships/
│   ├── modul_12_solid_principles/
│   └── modul_13_design_patterns/
└── 05_capstone_project/
    └── smart_pos_system/       <-- Atau hero_quest_rpg
```

---
*Catatan: Dokumen ini bersifat hidup (living document) dan kotak centang `[ ]` akan diperbarui menjadi `[x]` setiap kali kita menyelesaikan satu modul.*
