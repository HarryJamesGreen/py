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
    zip_file = input("Enter the path to the ZIP file: ")
    dictionary_file = input("Enter the path to the dictionary file: ")

    with open(dictionary_file, 'r') as f:
        dictionary = [line.strip() for line in f]

    if extract_zip(zip_file, dictionary):
        print("Password successfully cracked!")
    else:
        print("Failed to crack the password.")

if __name__ == "__main__":
    main()
