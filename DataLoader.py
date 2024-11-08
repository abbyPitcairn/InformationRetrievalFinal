import os
import csv

# Load in data from .csv and store in a dictionary of dictionaries.
# Key at level 1: category name
# Value at level 1: another dictionary
# Key at level 2: query text
# Value at level 2: query value: "Scoring is on a relative scale where a value of 100
# is the most commonly searched query, 50 is a query searched half as often as
# the most popular query, and so on" (Google Trends).

def load_top_data(directory):
    data_structure = {}

    # Traverse each CSV file in the specified directory
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            filepath = os.path.join(directory, filename)

            # Create a dictionary for each file based on its cleaned filename
            category = filename[3:].split(".")[0]  # Remove first 3 chars and '.csv'
            file_data = {}

            with open(filepath, mode='r', encoding='utf-8') as file:
                csv_reader = list(csv.reader(file))

                # Extract rows 2-27 (index 1 to 26 in zero-indexed lists)
                for row in csv_reader[2:27]:
                    try:
                        name = row[0].strip()  # Query name from column 0
                        value = int(row[1].replace(",", "").replace("%", ""))  # Integer value from column 1
                        file_data[name] = value
                    except (IndexError, ValueError):
                        print(f"Skipping invalid row in {filename}: {row}")

            # Store the file's data under the cleaned filename key
            data_structure[category] = file_data

    return data_structure
