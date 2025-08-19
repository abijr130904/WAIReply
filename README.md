'''
## WA Auto-Reply dengan AI Lokal

Proyek ini memungkinkan kamu membuat bot WhatsApp yang dapat membalas pesan secara otomatis menggunakan AI lokal berbasis model GPT-2 atau GPT-2 fine-tuned untuk bahasa Indonesia.

## 🚀 Fitur

Balas pesan WhatsApp otomatis.
Menggunakan AI lokal (via Ollama) → tanpa perlu OpenAI API.
Mendukung bahasa Indonesia dan bisa disesuaikan dengan model lain.
Bisa jalan di Windows, Linux, atau Mac.
Support Chrome.

## Persyaratan
Python ≥ 3.10
Sistem operasi: Windows / Linux / Mac


## Instalasi
Clone repository proyek

## Install semua dependensi
## bash
pip install -r requirements.txt
Siapkan virtual environment (opsional tapi disarankan)
## bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/Mac

Unduh dan jalankan Ollama sesuai OS: https://ollama.ai/download
Cek apakah Ollama sudah jalan: ollama --version
Pull Model AI : ollama pull llama3.1

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

'''
