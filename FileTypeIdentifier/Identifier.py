import os 

# Basic file signature checks (magic numbers)
def load_signatures(filename="signatures.txt"):
    sig_dict = {}
    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                # Skip empty lines or headers starting with #
                if not line or line.startswith("#"):
                    continue
                
                # Split the line by commas: Hex, Description, MIME
                parts = line.split(",")
                if len(parts) == 3:
                    hex_sig, description, mime = parts
                    # Store in dictionary: { "89504E47": ("PNG Image", "image/png") }
                    sig_dict[hex_sig.upper()] = (description, mime)
        return sig_dict
    
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return {}

def identify_file_type(file_path, sig_database):
    try:
        with open(file_path, "rb") as f:
            # Read the first 16 bytes for matching
            file_header = f.read(16)
            hex_header = file_header.hex().upper()
            
            # Now we use the database you passed in
            for hex_sig, (name, mime) in sig_database.items():
                if hex_header.startswith(hex_sig): 
                    return name, mime
            
            return "Unknown File Type", "Unknown MIME"
    except Exception as e:
        return f"Error: {str(e)}", "Error"