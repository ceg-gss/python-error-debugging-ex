# buggy_file_reader.py

def read_file(path):
    f = open(path, "r")
    data = f.read()
    # forgot to close the file and no error handling
    return data

if __name__ == "__main__":
    print(read_file("missing_file.txt"))
