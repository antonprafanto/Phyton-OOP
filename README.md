# 🐍 Python OOP: From Zero to Hero
> **Panduan Lengkap Pemrograman Berorientasi Objek (OOP) Menggunakan Python untuk Pemula & Orang Awam**

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Active%20Learning-success.svg)]()
[![Target](https://img.shields.io/badge/Level-Zero%20to%20Hero-orange.svg)]()
[![License](https://img.shields.io/badge/license-MIT-green.svg)]()

Selamat datang di repositori belajar **Python Object-Oriented Programming (OOP) — From Zero to Hero!**  
Repositori ini dirancang khusus bagi siapa saja yang ingin memahami konsep OOP secara mendalam tanpa harus pusing dengan jargon teknis yang rumit. 

Materi disusun dengan prinsip:
1. **Analogi Kehidupan Sehari-hari** (Mobil, Restoran, Smartphone, Rekening Bank) sebelum masuk ke istilah koding.
2. **Problem-Driven Learning** (Memahami *kenapa* suatu fitur diciptakan, bukan sekadar menghafal sintaks).
3. **Hands-on & Bertahap** (Kode pendek $\rightarrow$ Eksplorasi $\rightarrow$ Mini Latihan).
4. **"Awas Jebakan!"** (Mengupas tuntas pesan error yang sering membingungkan pemula).

---

## 🗺️ Roadmap & Silabus Singkat

Untuk melihat silabus super lengkap dan memantau status belajar secara detail, silakan baca:  
👉 **[SILABUS & PROGRESS TRACKER LENGKAP (SILABUS.md)](SILABUS.md)**

| Level | Modul | Topik Bahasan | Fokus Utama |
| :---: | :--- | :--- | :--- |
| **Fase 1** | [**Modul 0**](01_zero_level/modul_00_mengapa_oop/MATERI.md) | Mengapa Butuh OOP? | Mental Model, Perbedaan Prosedural vs OOP, Atribut & Method |
| *(Zero)* | [**Modul 1**](01_zero_level/modul_01_class_object/MATERI.md) | Melahirkan Objek Pertama | `class`, Object/Instance, Constructor `__init__`, dan Rahasia `self` |
| | [**Modul 2**](01_zero_level/modul_02_instance_vs_class_attr/MATERI.md) | Variabel Milik Siapa? | Instance Attribute vs Class Attribute (Awas kebocoran data!) |
| **Fase 2** | [**Modul 3**](02_core_level/modul_03_encapsulation/MATERI.md) | Pilar 1: Encapsulation | Proteksi Data, Public/Private, dan Gaya Elegan `@property` |
| *(Core)* | **Modul 4** | Pilar 2: Inheritance | Pewarisan Sifat, DRY, `super()`, & Multiple Inheritance |
| | **Modul 5** | Pilar 3: Polymorphism | Overriding Method, Portabilitas Aksi, dan Filosofi *Duck Typing* |
| | **Modul 6** | Pilar 4: Abstraction | Menyembunyikan Kerumitan dengan `abc.ABC` & `@abstractmethod` |
| **Fase 3** | **Modul 7** | Python Superpowers (Dunder) | Magic Methods (`__str__`, `__repr__`, `__len__`, `__eq__`) & JSON Serialization |
| *(Intermediate)*| **Modul 8** | Metode Spesial | `@classmethod` (Alternative Constructor) vs `@staticmethod` |
| | **Modul 9** | Custom Exception | Membuat Error Sendiri yang Mewarisi `Exception` |
| | **Modul 10** | Modern Python Shortcut | Modul `@dataclass` & Penulisan Type Hinting Modern |
| **Fase 4** | **Modul 11** | Hubungan Antar Objek | Association, Aggregation, & Komposisi (*Composition over Inheritance*) |
| *(Hero)* | **Modul 12** | Prinsip S.O.L.I.D | Clean Architecture (S-O-L-I-D) Dijelaskan Ramah Awam |
| | **Modul 13** | Design Patterns Populer | Singleton, Factory Method, dan Strategy Pattern di Python |
| **Fase 5** | **Modul 14** | Proyek Akhir (Capstone) | Aplikasi Nyata Utuh: SmartPOS System / Text-RPG Adventure |

---

## 📁 Struktur Direktori Repositori

```text
OOP/
├── README.md                   <-- Halaman utama repositori ini
├── SILABUS.md                  <-- Rincian lengkap kurikulum & tracker belajar
├── 01_zero_level/              <-- Fondasi dasar (Modul 0 s.d. 2)
│   ├── modul_00_mengapa_oop/
│   ├── modul_01_class_object/
│   └── modul_02_instance_vs_class_attr/
├── 02_core_level/              <-- 4 Pilar OOP (Modul 3 s.d. 6)
│   ├── modul_03_encapsulation/
│   ├── modul_04_inheritance/
│   ├── modul_05_polymorphism/
│   └── modul_06_abstraction/
├── 03_intermediate_level/      <-- Fitur Lanjutan Python (Modul 7 s.d. 10)
│   ├── modul_07_dunder_methods/
│   ├── modul_08_special_methods/
│   ├── modul_09_custom_exceptions/
│   └── modul_10_dataclasses/
├── 04_hero_level/              <-- Arsitektur & Best Practices (Modul 11 s.d. 13)
│   ├── modul_11_object_relationships/
│   ├── modul_12_solid_principles/
│   └── modul_13_design_patterns/
└── 05_capstone_project/        <-- Proyek Akhir Utuh (Modul 14)
    └── smart_pos_system/
```

---

## 🚀 Cara Menjalankan Kode

1. **Clone Repositori**:
   ```bash
   git clone https://github.com/antonprafanto/Phyton-OOP.git
   cd Phyton-OOP
   ```
2. **Pastikan Python 3 Terinstall**:
   ```bash
   python --version
   ```
3. **Jalankan Contoh Kode (Misal Modul 1)**:
   ```bash
   python 01_zero_level/modul_01_class_object/contoh_kucing.py
   ```

---

## 👨‍💻 Penulis & Kontribusi
Dibuat dengan ❤️ untuk komunitas pembelajar pemrograman pemula di Indonesia.  
Jika Anda menemukan kesalahan ketik atau ingin menyumbangkan ide latihan, jangan ragu untuk membuat *Pull Request* atau membuka *Issue*!
