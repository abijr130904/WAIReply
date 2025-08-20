```
## WA Auto-Reply dengan AI Lokal

Proyek ini memungkinkan kamu membuat membalas pesan WA secara otomatis
menggunakan berbasis AI

## 🚀 Fitur

Balas pesan WhatsApp otomatis.
Menggunakan AI lokal (via Ollama) → tanpa perlu OpenAI API.
Bisa jalan di Windows, Linux, atau Mac.
Support Chrome.

## Persyaratan
Python ≥ 3.10
Sistem operasi: Windows / Linux / Mac

## Instalasi
Clone repository proyek

## Install semua dependency
## bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt (instalasi semua dependency)

Instal Ollama lewat docker jika menggunakan windows (disarankan)
Jangan lupa jalankan container ollama yang sudah ditambahkan model contoh 
llama3.2:1b-instruct-q4_K_M

sesuaikan MODEL_NAME pada scrip ai_module.py dengan model yang sudah di pasang

## Jalankan file utama:
## bash
python main.py
Scan QR code WhatsApp Web di browser.
Mulai chat di WhatsApp, bot akan membalas pesan secara otomatis.

## Struktur Proyek
wa-auto-reply/
│
├─ main.py           # File utama menjalankan bot WA
├─ ai_module.py      # Modul untuk memanggil AI Lokal
├─ requirements.txt  # Daftar package yang dibutuhkan
├─ README.md         # Dokumentasi ini

```
