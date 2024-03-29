from pathlib import Path
import csv

# create a file path to the CSV file.
file_paths = [ Path.cwd() / "csv_reports"/"Cash_on_Hand.csv"]

cash_on_hand_records = []

# iterate through each file path in the list
for fp in file_paths:
    # read the CSV file.
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # skip header

        # append cash on hand records into the list
        cash_on_hand_records.extend([[int(row[0]), float(row[1])] for row in reader])

# Initialize variables for cash surplus
highest_surplus_day = None
highest_surplus_amount = float('-inf')

# Iterate through each row to check for cash surplus
for i in range(1, len(cash_on_hand_records)):
    current_day, current_amount = cash_on_hand_records[i]
    previous_day, previous_amount = cash_on_hand_records[i - 1]

    # Calculate the cash surplus amount
    surplus_amount = current_amount - previous_amount
    if surplus_amount > highest_surplus_amount:
        highest_surplus_amount = surplus_amount
        highest_surplus_day = current_day

# Print the cash surplus result
print(f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY:")
print(f"[HIGHEST CASH SURPLUS] DAY: {highest_surplus_day}, AMOUNT: SGD {highest_surplus_amount}")

#  Scenario 2 
# Initialize variables for cash deficit
lowest_deficit_day = None
lowest_deficit_amount = float('inf')

# Iterate through each row to check for cash deficit
for i in range(1, len(cash_on_hand_records)):
    current_day, current_amount = cash_on_hand_records[i]
    previous_day, previous_amount = cash_on_hand_records[i-1]

    # Calculate the cash deficit amount
    deficit_amount = current_amount - previous_amount
    if deficit_amount < lowest_deficit_amount:
        lowest_deficit_amount = deficit_amount
        lowest_deficit_day = current_day

# Print the result
print(f"[CASH DEFICIT] CASH ON EACH DAY IS LOWER THAN THE PREVIOUS DAY:")
print(f"[HIGHEST CASH DEFICIT] DAY: {lowest_deficit_day}, AMOUNT: SGD {abs (lowest_deficit_amount)}")

#  Scenario 3
# Calculate cash deficits 
cash_deficits = [(record[0], record[1] - cash_on_hand_records[i - 1][1]) for i, record in enumerate(cash_on_hand_records) if i != 0 and record[1] < cash_on_hand_records[i - 1][1]]

# Define a function to extract the deficit amount for sorting
def cash_deficits_amount(item):
    return item[1]

# Sort the cash deficits in reverse order based on the deficit amount
cash_deficits_sorted = sorted(cash_deficits, key=cash_deficits_amount, reverse=False)

for cash_deficit in cash_deficits_sorted[:20]:  # Print top 20 deficits
    print(f"[CASH DEFICIT] DAY: {cash_deficit[0]}, AMOUNT: SGD {abs(cash_deficit[1])}")
    
# Print the highest, 2nd, and 3rd cash deficit
print(f"[HIGHEST CASH DEFICIT] DAY: {cash_deficits_sorted[0][0]}, AMOUNT: SGD {abs(cash_deficits_sorted[0][1])}")
print(f"[2ND HIGHEST CASH DEFICIT] DAY: {cash_deficits_sorted[1][0]}, AMOUNT: SGD {abs(cash_deficits_sorted[1][1])}")
print(f"[3RD HIGHEST CASH DEFICIT] DAY: {cash_deficits_sorted[2][0]}, AMOUNT: SGD {abs(cash_deficits_sorted[2][1])}")