import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:1b-instruct-q4_K_M"

def ai_response_stream(text: str):
    """
    Kirim prompt ke Ollama dengan streaming.
    Mengembalikan teks hasil AI secara bertahap.
    """
    payload = {
        "model": MODEL_NAME,
        "prompt": text,
        "stream": True
    }

    try:
        with requests.post(OLLAMA_URL, json=payload, stream=True, timeout=120) as r:
            r.raise_for_status()
            full_response = ""
            for line in r.iter_lines():
                if line:
                    try:
                        data = line.decode("utf-8")
                        chunk = json.loads(data)
                        token = chunk.get("response", "")
                        if token:
                            print(token, end="", flush=True)  # tampil real-time di console
                            full_response += token
                        if chunk.get("done", False):
                            break
                    except Exception as e:
                        print("Error parsing chunk:", e)
            print()  # pindah baris setelah selesai
            return full_response if full_response else "AI tidak memberikan jawaban."
    except requests.exceptions.RequestException as e:
        return f"Error koneksi ke Ollama: {e}"
