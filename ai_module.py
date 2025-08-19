import requests
import time

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.1"

def ai_response(text: str, retries: int = 3) -> str:
    """
    Kirim prompt ke Ollama dan ambil balasan AI.
    - retries: jumlah percobaan ulang kalau gagal/timeout
    """
    payload = {
        "model": MODEL_NAME,
        "prompt": text,
        "stream": False,   # bisa ubah ke True kalau mau streaming
        # "options": {
        #     "num_predict": 30  # batasi jawaban max ~80 token biar cepat
        # }
    }

    for attempt in range(1, retries + 1):
        try:
            response = requests.post(
                OLLAMA_URL,
                json=payload,
                timeout=90
            )

            if response.status_code == 200:
                data = response.json()
                return data.get("response", "AI tidak memberikan jawaban.")
            else:
                return f"Gagal (status {response.status_code}): {response.text}"

        except requests.exceptions.Timeout:
            print(f"Timeout di percobaan ke-{attempt}, coba lagi...")
        except requests.exceptions.ConnectionError:
            print("Tidak bisa konek ke Ollama. Pastikan server jalan (docker/ollama).")
            return "Gagal koneksi ke AI Lokal."
        except Exception as e:
            print(f"Error tak terduga: {e}")
            return f"Error AI Lokal: {e}"

        # kalau belum berhasil, tunggu sebentar lalu ulang
        time.sleep(2)

    return "AI Lokal tidak merespon setelah beberapa kali percobaan."
