import pandas as pd

def extract_sheets_as_csv(excel_file_path, output_folder):
    # Load the Excel file
    xls = pd.ExcelFile(excel_file_path)

    # Loop through all the sheets in the Excel file
    for sheet_name in xls.sheet_names:
        # Read the sheet into a DataFrame
        df = pd.read_excel(xls, sheet_name)

        # Define the CSV file name with the output folder
        csv_file_name = f"{output_folder}\\{sheet_name}.csv"

        # Save the DataFrame as a CSV file
        df.to_csv(csv_file_name, index=False)
        print(f"Sheet {sheet_name} saved as {csv_file_name}")

# Path to  Excel file
excel_file_path = 'C:\\Users\\coolb\\Desktop\\Mainski\\uni\\Database Enhancement\\DB_enchantment_git\\database_enchancement\\Database enhancement\\csv_sample_data\\SampleData (2).xlsx'

# Folder where CSV files will be saved
output_folder = 'C:\\Users\\coolb\\Desktop\\Mainski\\uni\\Database Enhancement\\DB_enchantment_git\\database_enchancement\\Database enhancement\\csv_sample_data'

extract_sheets_as_csv(excel_file_path, output_folder)
