# ✨ MODUL 7: PYTHON SUPERPOWERS – DUNDER METHODS & SERIALISASI JSON
> **Tingkat**: Intermediate Level (Kekuatan Rahasia Python)  
> **Tujuan**: Memahami **Dunder / Magic Methods** (`__str__`, `__repr__`, `__len__`, `__eq__`, `__add__`), menguasai *Operator Overloading*, serta menjawab pertanyaan awam: *"Bagaimana cara menyimpan objek ke file JSON agar tidak hilang saat program ditutup?"*.

---

## 1. Cerita Pembuka: Kartu Nama Ramah vs KTP Resmi Programmer

Pernahkah Anda mencoba mencetak objek buatan Anda sendiri dengan perintah `print()`?

```python
class Kucing:
    def __init__(self, nama: str):
        self.nama = nama

kucing = Kucing("Mimi")
print(kucing)
# 💥 OUTPUT ASLI PYTHON:
# <__main__.Kucing object at 0x0000019F45FF74D0>
```

Bagi orang awam, melihat teks `<__main__.Kucing object at 0x000...>` terasa sangat aneh dan tidak berguna. Itu adalah **alamat fisik memori RAM komputer**.

Di sinilah **Dunder Methods (Magic Methods)** datang sebagai penyelamat!  
Dunder adalah singkatan dari **Double Underscore** (dua garis bawah di depan dan belakang). Mereka adalah fungsi-fungsi rahasia bawaan Python yang bertindak sebagai **"Penerjemah Bahasa Alami"** bagi objek Anda.

---

## 2. Duo Penerjemah Tampilan: `__str__` vs `__repr__`

Python menyediakan dua metode berbeda untuk mengubah objek menjadi teks:

| Pembeda | `__str__()` | `__repr__()` |
| :--- | :--- | :--- |
| **Audiens Utama** | **Pengguna Akhir (User)** | **Programmer / Debugger** |
| **Karakter Teks** | Ramah manusia, mudah dibaca, informatif | Lengkap, presisi, mencerminkan kode Python asli pembuatnya |
| **Kapan Dipanggil?** | Saat kita memanggil `print(objek)` atau `str(objek)` | Saat mengetik `objek` di terminal interaktif atau `repr(objek)` |
| **Aturan Emas** | Menggambarkan *apa artinya* bagi user | Menggambarkan *apa isinya* bagi developer |

### Contoh Kode:
```python
class Produk:
    def __init__(self, nama: str, harga: int):
        self.nama = nama
        self.harga = harga

    # 1. UNTUK USER: Cantik dan rapi di layar aplikasi
    def __str__(self) -> str:
        return f"{self.nama} (Harga: Rp {self.harga:,})"

    # 2. UNTUK PROGRAMMER: Cetak biru kode asli untuk keperluan debug
    def __repr__(self) -> str:
        return f"Produk(nama='{self.nama}', harga={self.harga})"

kopi = Produk("Kopi Arabika", 25_000)

print(str(kopi))   # Output: Kopi Arabika (Harga: Rp 25,000)
print(repr(kopi))  # Output: Produk(nama='Kopi Arabika', harga=25000)
```

> 💡 **Tips Python**: Jika Anda hanya menulis `__repr__`, Python otomatis menggunakannya juga untuk `__str__`. Jadi minimal buatlah selalu `__repr__`!

---

## 3. Menghitung Isi Objek dengan `__len__` 📏

Secara bawaan, kita tidak bisa menjalankan `len(objek_kita)`. Python akan memprotes: `TypeError: object of type '...' has no len()`.  
Agar objek kita bisa dihitung panjangnya seperti list biasa, cukup pasang `__len__`:

```python
class RakBuku:
    def __init__(self):
        self.buku = []

    def tambah_buku(self, judul: str):
        self.buku.append(judul)

    def __len__(self) -> int:
        return len(self.buku)

rak = RakBuku()
rak.tambah_buku("Laskar Pelangi")
rak.tambah_buku("Bumi Manusia")

print(len(rak))  # Output: 2 (Bisa dihitung dengan len() bawaan Python!)
```

---

## 4. Membandingkan Objek Sejati dengan `__eq__` ⚖️

Pernahkah Anda heran mengapa dua objek yang isinya sama persis dianggap berbeda oleh Python?

```python
class KTP:
    def __init__(self, nik: str):
        self.nik = nik

ktp1 = KTP("3201019901")
ktp2 = KTP("3201019901")

print(ktp1 == ktp2)  # 💥 HASILNYA: False! (Loh, kok beda?)
```
*Mengapa `False`?*  
Karena secara default, simbol `==` di Python membandingkan **alamat memori (`id`)**, bukan isi datanya! Karena `ktp1` dan `ktp2` adalah dua wadah terpisah di RAM, Python menganggap keduanya berbeda.

### Solusi: Ajari Python Cara Membandingkan dengan `__eq__`:
```python
class KTP:
    def __init__(self, nik: str):
        self.nik = nik

    def __eq__(self, objek_lain) -> bool:
        if isinstance(objek_lain, KTP):
            return self.nik == objek_lain.nik
        return False

# Sekarang:
print(ktp1 == ktp2)  # Output: True! ✅
```

---

## 5. Operator Overloading: Menjumlahkan Objek dengan `__add__` ➕

Bagaimana jika kita ingin menggabungkan dua objek secara alami menggunakan tanda tambah (`+`)?

```python
class Dompet:
    def __init__(self, saldo: int):
        self.saldo = saldo

    def __add__(self, objek_lain):
        if isinstance(objek_lain, Dompet):
            return Dompet(self.saldo + objek_lain.saldo)
        elif isinstance(objek_lain, int):
            return Dompet(self.saldo + objek_lain)
        return NotImplemented

dompet_a = Dompet(50_000)
dompet_b = Dompet(70_000)

dompet_total = dompet_a + dompet_b
print(dompet_total.saldo)  # Output: 120000 (Sangat elegan!)
```

---

## 6. Menyimpan Objek ke JSON (Object Serialization) 💾

Orang awam sering bertanya:  
*"Ketika program dimatikan, semua objek yang dibuat di RAM hilang. Bagaimana cara menyimpannya ke file harddisk agar datanya abadi?"*

Proses mengubah objek hidup di memori menjadi format teks yang bisa disimpan disebut **Serialization (Serialisasi)**. Format paling populer di dunia adalah **JSON**.

```mermaid
flowchart LR
    A["Objek Python di RAM\n(budi = User('Budi', 25))"] -->|to_dict() + json.dump()| B["File JSON di Harddisk\n{'nama': 'Budi', 'umur': 25}"]
    B -->|json.load() + from_dict()| C["Lahir Kembali Jadi Objek\n(User Aktif di Memori)"]
```

### Pola Industri: Metode `to_dict()` dan `from_dict()`
```python
import json

class Nasabah:
    def __init__(self, nama: str, saldo: int):
        self.nama = nama
        self.saldo = saldo

    # 1. SERIALISASI: Ubah Objek -> Dictionary
    def to_dict(self) -> dict:
        return {"nama": self.nama, "saldo": self.saldo}

    # 2. DESERIALISASI: Ubah Dictionary -> Objek Baru
    @classmethod
    def from_dict(cls, data: dict):
        return cls(nama=data["nama"], saldo=data["saldo"])
```

### Menyimpan dan Membuka Kembali:
```python
# SIMPAN KE FILE:
user = Nasabah("Anton", 750_000)
with open("nasabah.json", "w") as f:
    json.dump(user.to_dict(), f, indent=4)

# BACA KEMBALI SETELAH PROGRAM DIMATIKAN:
with open("nasabah.json", "r") as f:
    data_mentah = json.load(f)
    user_pulih = Nasabah.from_dict(data_mentah)

print(user_pulih.nama)   # Output: Anton (Data pulih sempurna!)
print(user_pulih.saldo)  # Output: 750000
```

---

## 7. 🎯 Kuis Kilat Cek Pemahaman Mandiri

#### Soal 1:
> Jika sebuah class tidak memiliki fungsi `__str__`, tetapi memiliki fungsi `__repr__`, apa yang terjadi saat kita menjalankan `print(objek)`?  
> A. Python akan error karena `__str__` wajib ada.  
> B. Python akan secara otomatis memanggil `__repr__` sebagai pengganti.  
> C. Layar terminal akan tetap kosong.  

<details>
<summary>👉 Klik untuk melihat Jawaban Soal 1</summary>

**Jawaban: B**  
*Penjelasan*: Python memiliki mekanisme *fallback*: jika `__str__` tidak ditemukan, Python akan memanggil `__repr__`. Oleh karena itu, *best practice* di industri adalah selalu mendefinisikan minimal `__repr__`.
</details>

---

#### Soal 2:
> Dunder method apa yang dipanggil saat kita mengeksekusi ekspresi `len(keranjang_belanja)`?  
> A. `__count__()`  
> B. `__size__()`  
> C. `__len__()`  

<details>
<summary>👉 Klik untuk melihat Jawaban Soal 2</summary>

**Jawaban: C (`__len__()`)**  
*Penjelasan*: Fungsi bawaan `len(x)` di Python sebenarnya adalah jembatan yang memanggil `x.__len__()` di balik layar.
</details>

---

## 8. 🛠️ Berkas Latihan di Modul Ini
Silakan buka dan jalankan file berikut di terminal:
1. `01_str_repr_len.py` $\rightarrow$ Praktik `__str__`, `__repr__`, dan `__len__` pada katalog buku.
2. `02_operator_overloading.py` $\rightarrow$ Praktik perbandingan `__eq__` dan penjumlahan `__add__` pada saldo dompet.
3. `03_object_serialization_json.py` $\rightarrow$ Praktik menyimpan objek ke file JSON dan memulihkannya kembali.
4. `04_latihan_mandiri.py` $\rightarrow$ Tantangan membuat Objek `PlaylistLagu` lengkap dengan dunder & serialisasi JSON.
5. `04_solusi_latihan.py` $\rightarrow$ Kunci jawaban lengkap latihan.
