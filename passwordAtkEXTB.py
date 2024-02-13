import argparse
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
    parser = argparse.ArgumentParser(description="Password cracking tool for ZIP files")
    parser.add_argument("-f", "--zipfile", help="Path to the ZIP file", required=True)
    parser.add_argument("-d", "--dictionary", help="Path to the dictionary file", required=True)
    args = parser.parse_args()

    zip_file = args.zipfile
    dictionary_file = args.dictionary

    with open(dictionary_file, 'r') as f:
        dictionary = [line.strip() for line in f]

    if extract_zip(zip_file, dictionary):
        print("Password successfully cracked!")
    else:
        print("Failed to crack the password.")

if __name__ == "__main__":
    main()
