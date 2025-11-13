# fixed_file_reader.py

def read_file(path):
    """Read a file safely with basic error handling."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"[ERROR] File not found: {path}"
    except OSError as e:
        return f"[ERROR] OS error while reading {path}: {e}"

if __name__ == "__main__":
    print(read_file("missing_file.txt"))
