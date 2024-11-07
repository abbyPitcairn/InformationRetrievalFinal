import os
import csv


def load_nested_data_structure(directory):
    data_structure = {}

    # Traverse each CSV file in the specified directory
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            filepath = os.path.join(directory, filename)

            # Initialize the dictionaries for each file
            file_data = {"top": {}, "rising": {}}

            with open(filepath, mode='r', encoding='utf-8') as file:
                csv_reader = csv.reader(file)

                # Track which section we’re in
                current_section = None

                for row in csv_reader:
                    if not row:
                        continue

                    # Check for section headers
                    if row[0].strip() == "TOP":
                        current_section = "top"
                    elif row[0].strip() == "RISING":
                        current_section = "rising"

                    # Extract data for the current section
                    elif current_section in ["top", "rising"]:
                        # Parse string and integer value
                        try:
                            name = row[0].strip()
                            value = int(row[1].replace(",", "").replace("%", ""))
                            file_data[current_section][name] = value
                        except (IndexError, ValueError):
                            print(f"Skipping invalid row in {filename}: {row}")

            # Add the structured data for this file to the main dictionary
            data_structure[filename] = file_data

    return data_structure


# Usage example
me_top_data = load_nested_data_structure("Data/ME-TOP")
us_top_data = load_nested_data_structure("Data/US-TOP")
ww_top_data = load_nested_data_structure("Data/WW-TOP")

# Print a sample to verify
print("ME-TOP Sample:", list(me_top_data.items())[:1])  # Show the structure for the first file