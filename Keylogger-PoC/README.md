# Python Keylogger PoC (Educational)

A modular, stealth-oriented keylogger proof-of-concept built with Python. This project demonstrates how background processes can be used to capture system input and exfiltrate data to a remote server using Discord Webhooks.

## 🚀 Features
- **Silent Execution:** Designed to run via `.pyw` to hide terminal windows from the user.
- **Automated Exfiltration:** Monitors a local buffer and automatically sends data to a Discord Webhook every 100 characters.
- **Modular Architecture:** Logic is separated into an engine (`Keylogger.py`) and a launcher (`main.pyw`) for cleaner code management.
- **Secure Configuration:** Uses `python-dotenv` to keep sensitive Webhook URLs out of the source code and GitHub history.

## 🛠️ Project Structure
- `Keylogger.py`: The core engine that handles keystroke listening and network requests.
- `main.pyw`: The entry point that launches the logger as a background process.
- `.env`: (Local only) Stores your Discord Webhook URL.
- `requirements.txt`: List of necessary Python libraries for easy installation.

## 📥 Installation & Setup
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/Keylogger-PoC.git](https://github.com/YOUR_USERNAME/Keylogger-PoC.git)
   cd Keylogger-PoC
   ```

2. **Install dependencies:**
   ```pip install -r requirements.txt```

3. **Configure Environment:**
   Create a .env file in the root directory and add your webhook link:
   ```Webhook_URL=your_discord_webhook_url_here```

## 🧪 Usage
- **standard mode:** To run the keylogger in standard mode (visible terminal for testing):
   ```bash
   python Keylogger.py
   ```

- To run the keylogger in stealth mod (visible terminal for testing):
Run *main.pyw* or use:
   ```bash 
   pythonw main.pyw
   ```

## ⚠️ Disclaimer
This project was created for educational purposes and security research only.
The goal is to understand how malware functions to build better defensive systems.
NEVER use this software on a computer you do not own or have explicit permission to test.