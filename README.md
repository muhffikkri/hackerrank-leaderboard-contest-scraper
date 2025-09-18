# Hackerrank Leaderboard Contest Scraper

Aplikasi ini digunakan untuk mengambil data leaderboard dari kontes Hackerrank secara otomatis dan menyimpannya dalam format CSV. Tersedia antarmuka GUI agar lebih mudah digunakan.

## Fitur

- Scraping leaderboard kontes Hackerrank dengan pagination (semua peserta diambil)
- Menyimpan hasil ke file CSV di folder `results`
- Konfigurasi login dan link kontes melalui file `.env` atau GUI
- GUI dengan tab Home, Settings, Results, dan Help
- Log progress scraping langsung di GUI
- Melihat hasil file dan info durasi scraping di tab Results
- Setup otomatis dengan `setup.bat` (membuat venv, install dependencies, jalankan GUI)

## Cara Penggunaan

### 1. Manual (tanpa GUI)

- Edit file `.env` dan isi dengan email, password, dan link kontes Hackerrank
- Jalankan `main.py` dengan Python:
  ```
  python main.py
  ```
- File hasil akan tersimpan di folder `results`

### 2. Otomatis (GUI & setup)

- Jalankan `setup.bat` (klik dua kali atau lewat terminal):
  ```
  setup.bat
  ```
- Ikuti instruksi di GUI:
  - Isi email, password, dan link kontes di tab Settings
  - Klik "Start Scraping" di tab Home
  - Lihat log progress dan hasil di tab Results

## Hasil

- File CSV berisi leaderboard kontes Hackerrank, tersimpan di folder `results`
- Info file: jumlah peserta, waktu mulai, waktu selesai, durasi scraping

## Persiapan

- Pastikan sudah memiliki akun Hackerrank dengan akses ke kontes yang ingin diambil
- Pastikan Python sudah terinstall (disarankan versi 3.8+)
- Koneksi internet aktif

## Update Potensial

- Export hasil ke format lain (Excel, JSON)
- Filter peserta berdasarkan skor atau kriteria lain
- Scraping data tambahan (submission, challenge detail)
- Integrasi login OAuth atau token
- Penambahan fitur analisis data leaderboard

---

Kontribusi dan saran pengembangan sangat terbuka!
