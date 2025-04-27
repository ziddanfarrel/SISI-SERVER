# 📦 BACKEND SISTEM MANAJEMEN INVENTORY (UTS)

---

## 📝 Deskripsi
Aplikasi backend untuk mengelola persediaan barang pada toko, termasuk kategori, supplier, item barang, dan laporan data stok.

---

## 🚀 Teknologi dan Tools
- **Django 5.2** - Backend Framework
- **Django REST Framework** - Membuat API CRUD
- **PostgreSQL** - Database Relasional
- **Docker & Docker Compose** - Containerization

---

## ✅ Fitur yang Sudah Dibuat
- CRUD Data Items
- CRUD Data Kategori
- CRUD Data Supplier
- Ringkasan Stok Barang (Total, Nilai, Rata-rata)
- Daftar Barang Stok Rendah (<5 unit)
- Laporan Barang per Kategori
- Laporan Barang per Supplier
- Ringkasan Keseluruhan Sistem

---

## ⚙️ Cara Menjalankan Project
1. Clone repository:
    ```bash
    git clone https://github.com/ziddanfarrel/SISI-SERVER.git
    ```
2. Masuk ke project folder:
    ```bash
    cd SISI-SERVER
    ```
3. Jalankan Docker Compose:
    ```bash
    docker-compose up --build
    ```
4. Akses melalui browser:
    - Admin Panel: `http://localhost:8000/admin/`
    - API Endpoints: `http://localhost:8000/api/items/`
    - API Reports: `/api/items/stock_summary/`, dll.

---

## 📄 Catatan
- Dokumentasi Swagger **tidak digunakan** karena ketidakcocokan dengan Django 5.2. 
- API dapat diuji menggunakan browser atau Postman.

---

## 🔗 Link Repository
[Klik di sini untuk melihat Repository GitHub](https://github.com/ziddanfarrel/SISI-SERVER)

---

## 📋 Checklist Project
- [x] Kode aplikasi lengkap
- [x] File migrasi database tersedia
- [x] docker-compose.yml tersedia
- [x] README.md tersedia
- [x] Repository sudah dipush ke GitHub

---

# ✨ Penutup
> Proyek ini diselesaikan sebagai tugas UTS Backend Development dengan menggunakan Django, PostgreSQL, dan Docker.

---

