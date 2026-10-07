# ==============================================================================
# SMARTPOS SYSTEM - CUSTOM EXCEPTIONS (MODUL 9)
# ==============================================================================
# File: exceptions.py
# Deskripsi: Hirarki error kustom berbasis OOP untuk menangani kegagalan
#            transaksi, keamanan inventaris, dan hak akses kasir.
# ==============================================================================

class POSError(Exception):
    """Kelas induk seluruh error khusus di aplikasi SmartPOS."""
    def __init__(self, pesan: str, kode_error: str = "ERR-GENERIC"):
        super().__init__(pesan)
        self.pesan = pesan
        self.kode_error = kode_error

    def __str__(self):
        return f"[{self.kode_error}] {self.pesan}"


class ProdukTidakDitemukanError(POSError):
    """Dilempar saat SKU produk yang dicari kasir tidak ada di inventaris."""
    def __init__(self, sku: str):
        super().__init__(f"Produk dengan SKU '{sku}' tidak ditemukan di katalog toko!", "ERR-PRODUCT-404")
        self.sku = sku


class StokHabisError(POSError):
    """Dilempar saat stok fisik tidak mencukupi permintaan kasir."""
    def __init__(self, nama_produk: str, stok_tersedia: int, diminta: int):
        super().__init__(
            f"Stok '{nama_produk}' tidak cukup! Tersedia: {stok_tersedia}, Diminta: {diminta}",
            "ERR-STOCK-INSUFFICIENT"
        )
        self.nama_produk = nama_produk
        self.stok_tersedia = stok_tersedia
        self.diminta = diminta


class PembayaranGagalError(POSError):
    """Dilempar saat pembayaran gagal (uang tunai kurang atau kartu ditolak)."""
    def __init__(self, alasan: str):
        super().__init__(f"Proses pembayaran gagal diproses: {alasan}", "ERR-PAYMENT-FAILED")


class SaldoKasirKurangError(POSError):
    """Dilempar saat penarikan kas laci kasir melebihi saldo yang ada."""
    def __init__(self, saldo_tersedia: int, diminta: int):
        super().__init__(
            f"Penarikan kas ditolak! Saldo laci Rp {saldo_tersedia:,}, diminta tarik Rp {diminta:,}",
            "ERR-CASH-DRAWER"
        )


class AksesDitolakError(POSError):
    """Dilempar saat staf mencoba melakukan aksi di luar wewenang rolenya."""
    def __init__(self, role: str, aksi: str):
        super().__init__(
            f"Akses ditolak! Role '{role}' tidak diizinkan melakukan tindakan '{aksi}'",
            "ERR-UNAUTHORIZED"
        )
