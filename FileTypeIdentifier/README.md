# 🛡️ File Identifier

A Python-based forensics tool designed to identify the true nature of files by analyzing their **Magic Bytes** (internal hex signatures) rather than relying on file extensions. This project demonstrates core cybersecurity concepts like binary data analysis, MIME type mapping, and the detection of **Masquerading** (files hiding their true identity).

## 🚀 Key Features
- **Binary Signature Analysis**: Reads the first 16 bytes of any file to find its "Magic Number."
- **MIME Type Mapping**: Correctly identifies files using industry-standard types (e.g., `image/png`).
- **Security Validation**: Flags high-priority mismatches, specifically alerting if executables (.exe) are hiding as other formats.
- **Stylized CLI**: Features a typewriter-effect interface for a classic cybersecurity aesthetic.
- **Modular Database**: All signatures are stored in an external `signatures.txt` file for easy updates without changing the code.

## 📂 Project Structure
- `main.py`: The primary user interface and main execution loop.
- `Identifier.py`: The logic engine that handles file reading and signature comparison.
- `misc.py`: Contains helper functions for the typewriter effect and styling.
- `signatures.txt`: The signature database (supports comments and category headers).
- `.gitignore`: Configured to keep the repository clean of temporary Python and system junk.

## 🛠️ Installation & Usage
1. **Clone the Repo**:
   ```bash
   git clone [https://github.com/Daniel7Shuai/CyberProjects.git](https://github.com/Daniel7Shuai/CyberProjects.git)
   cd FileTypeIdentifier