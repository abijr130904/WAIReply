from playwright.sync_api import sync_playwright
from ai_module import ai_response
import time

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            user_data_dir="C:/temp/chrome-profile",
            channel="chrome",
            headless=False
        )
        page = browser.new_page()
        page.goto("https://web.whatsapp.com", timeout=60000, wait_until="domcontentloaded")

        print("✅ WhatsApp Web berhasil dibuka.")

        try:
            page.wait_for_selector("canvas[aria-label='Scan me!']", timeout=15000)
            print("Silakan scan QR Code WhatsApp...")
        except:
            print("✅ Sudah login, langsung masuk ke WhatsApp.")

        last_seen_msg = ""

        while True:
            try:
                messages = page.query_selector_all("div.message-in span.selectable-text")

                if messages:
                    last_msg = messages[-1].inner_text()

                    # hanya proses jika beda dari terakhir
                    if last_msg != last_seen_msg:
                        print("Pesan masuk:", last_msg)

                        # Balasan AI
                        reply = ai_response(last_msg)
                        print("Balasan:", reply)

                        input_box = page.query_selector("div[contenteditable='true'][data-tab='10']")
                        input_box.click()
                        input_box.fill(reply)
                        input_box.press("Enter")

                        last_seen_msg = last_msg  # simpan pesan terakhir

            except Exception as e:
                print("⚠️ Error:", e)

            time.sleep(3)  # cek tiap 3 detik

if __name__ == "__main__":
    main()
