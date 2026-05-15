import os
from misc import print_style
from Identifier import identify_file_type, load_signatures

def main_menu():
    sig_database = load_signatures("signatures.txt")
    
    while True:
        # Using the typewriter style for the menu
        print_style("\n--- Cyber File Identifier ---")
        print_style("1. Identify File Type")
        print_style("2. Exit")
        
        choice = input("\nSelect an option: ")
        
        if choice == '1':
            path = input("Enter file path: ").strip('"')
            if os.path.exists(path):
                print_style(f"Analyzing {os.path.basename(path)}...")

                file_type, mime = identify_file_type(path, sig_database)
                file_extension = os.path.splitext(path)[1].lower()



                print_style(f"""[+]File Type: {file_type}
[+]MIME Type: {mime}
[+] File Extension: {file_extension}""")
                
                if file_type == "Unknown File Type":
                    print_style("\n[!] Caution: No matching signature found in database.")
                elif file_extension.strip('.') in mime:
                    print_style("\n[V] Verification complete. Signature matches extension.")

                elif "application/x-msdownload" in mime and file_extension != ".exe":
                    print_style("\n!!! WARNING: CRITICAL MASQUERADING DETECTED !!!")
                    print_style("!!! This is an EXECUTABLE hiding as another file type !!!")
                else:
                    print_style("\n[!] Warning: File extension mismatch detected!")

            else:
                print_style("Error: File not found!")

        elif choice == '2':
            print_style("Exiting...")
            break


if __name__ == "__main__":
    main_menu()