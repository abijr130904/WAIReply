from playwright.sync_api import sync_playwright
import requests, json, time, re, sys

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:1b-instruct-q4_K_M"

# Warna terminal
WHITE = "\033[97m"
GREEN = "\033[92m"
RESET = "\033[0m"

def ai_response_stream_to_whatsapp(prompt, page):
    """
    Ambil response AI streaming lalu kirim ke WhatsApp per kalimat,
    sambil stream ke terminal (hijau).
    """
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    try:
        with requests.post(OLLAMA_URL, json=payload, stream=True, timeout=120) as r:
            r.raise_for_status()
            buffer = ""
            print(f"{GREEN}Balasan AI: ", end="", flush=True)  # mulai baris baru
            for line in r.iter_lines():
                if line:
                    data = json.loads(line.decode("utf-8"))
                    token = data.get("response", "")
                    if token:
                        # tampilkan langsung di terminal
                        sys.stdout.write(token)
                        sys.stdout.flush()
                        buffer += token
                        # cek jika ada kalimat lengkap
                        sentences = re.split(r'([.!?])', buffer)
                        if len(sentences) > 1:
                            kalimat = "".join(sentences[:-1]).strip()
                            end = sentences[-2] if len(sentences) >= 2 else ""
                            if kalimat:
                                send_to_whatsapp(kalimat + end, page)
                            buffer = sentences[-1]  # sisa
                    if data.get("done", False):
                        # kirim sisa terakhir
                        if buffer.strip():
                            send_to_whatsapp(buffer.strip(), page)
                        break
            print(RESET)  # reset warna setelah selesai
    except Exception as e:
        print("Error streaming:", e)
        send_to_whatsapp("Error AI Lokal: tidak bisa balas.", page)

def send_to_whatsapp(text, page):
    """Kirim teks ke input box WhatsApp dan tekan Enter"""
    input_box = page.query_selector("div[contenteditable='true'][data-tab='10']")
    input_box.click()
    input_box.fill(text.strip())
    input_box.press("Enter")
    print(f"\n{GREEN}Terkirim: {text.strip()}{RESET}")

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            user_data_dir="C:/temp/chrome-profile",
            channel="chrome",
            headless=False
        )
        page = browser.new_page()
        page.goto("https://web.whatsapp.com", timeout=60000, wait_until="domcontentloaded")
        print("WhatsApp Web berhasil dibuka.")

        try:
            page.wait_for_selector("canvas[aria-label='Scan me!']", timeout=15000)
            print("Silakan scan QR Code WhatsApp...")
        except:
            print("Sudah login, langsung masuk ke WhatsApp.")
        last_seen_msg = ""
        while True:
            try:
                messages = page.query_selector_all("div.message-in span.selectable-text")

                if messages:
                    last_msg = messages[-1].inner_text()
                    if last_msg != last_seen_msg:
                        print(f"\n{WHITE}Pesan masuk: {last_msg}{RESET}")
                        # Balas dengan streaming per kalimat
                        ai_response_stream_to_whatsapp(last_msg, page)
                        last_seen_msg = last_msg
            except Exception as e:
                print("Error:", e)
            time.sleep(2)
if __name__ == "__main__":
    main()
