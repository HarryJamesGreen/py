import sys
import zipfile

def extract_zip(zip_file, dictionary):
    with zipfile.ZipFile(zip_file) as zf:
        for password in dictionary:
            try:
                zf.extractall(pwd=password.encode())
                print(f"Password cracked: {password}")
                return True
            except Exception as e:
                # Incorrect password, continue trying
                pass
    return False

def main():
    # Check if enough arguments are provided
    if len(sys.argv) < 3:
        print("Usage: python passwordCrackZipExtA.py -zipfile- -dictionary-")
        return
    
    zip_file = sys.argv[1]
    dictionary_file = sys.argv[2]

    with open(dictionary_file, 'r') as f:
        dictionary = [line.strip() for line in f]

    if extract_zip(zip_file, dictionary):
        print("Password successfully cracked!")
    else:
        print("Failed to crack the password.")

if __name__ == "__main__":
    main()
