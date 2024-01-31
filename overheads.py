from pathlib import Path
import csv

# create a file path to Csv file.
file_path = Path.cwd() / "csv_reports" /"Overhead.csv"

# create an empty list for overhead records
overhead_records = []

# iterate through each file path in the list
for fp in file_path:
    # read the CSV file.
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # skip header

        # append delivery records into the overhead records list
        for row in reader:
            # get the info for each record and append to the overhead records list
            overhead_records.append([row[0], row[1]])

# Scenario 1
# the highest overheads in “overheads.csv”
   # Initialize variables for finding the highest value
    highest_value = float('-inf')  # Set to negative infinity initially
    highest_overhead_category = None

    # Iterate through each row to find the highest value
    for row in overhead_records:
        current_value = float(row[1])
        if current_value > highest_value:
            highest_value = current_value
            highest_overhead_category = row[0]

# Print the result
print(f"[HIGHEST OVERHEAD] {highest_overhead_category}: {highest_value}%")
