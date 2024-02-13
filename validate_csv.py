import pandas as pd

def validate_csv(file_path):
    # Load the CSV file
    df = pd.read_csv(file_path)

    # Display the file name in console
    print(f"Validating: {file_path.split('/')[-1]}")
    print("-" * 50)

    # Check for null/missing values
    missing_values = df.isnull().sum()
    if missing_values.any():
        print("Missing Values:")
        for column, count in missing_values[missing_values > 0].items():
            print(f"  - {column}: {count}")
        print()
    else:
        print("No missing values detected.\n")

    # Checking for duplicate rows
    duplicate_rows = df[df.duplicated()]
    if not duplicate_rows.empty:
        print(f"Found {len(duplicate_rows)} duplicate rows.")
        print()
    else:
        print("No duplicate rows detected.\n")

    print("=" * 50)
    print()

# List of CSV files to validate (Declaring csv_files var)
csv_files = [
    "Database enhancement/csv_sample_data/customer.csv",
    "Database enhancement/csv_sample_data/developer.csv",
    "Database enhancement/csv_sample_data/order.csv",
    "Database enhancement/csv_sample_data/products.csv"
]

for file in csv_files:
    validate_csv(file)
