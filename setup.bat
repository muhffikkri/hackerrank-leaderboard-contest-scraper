@echo off
setlocal

REM 1. Cek dan buat venv jika belum ada
if not exist venv (
    echo Membuat virtual environment...
    python -m venv venv
)

REM 2. Aktifkan venv dan install requirements
call venv\Scripts\activate
if exist requirements.txt (
    echo Menginstall dependencies dari requirements.txt...
    pip install --upgrade pip
    pip install -r requirements.txt
) else (
    echo Tidak ditemukan requirements.txt
)

REM 3. Jalankan GUI
python gui.py
endlocal
