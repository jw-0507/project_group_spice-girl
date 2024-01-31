import csv
from pathlib import Path

# create a file path to the CSV file.
file_paths = [Path.cwd() / "csv_reports"/ "Profit_and_Loss.csv"]

# create an empty list for overhead records
profit_and_loss_record = []

# iterate through each file path in the list
for fp in file_paths:
    # read the CSV file.
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # skip header

        # append profit and loss records into the list
        profit_and_loss_record.extend([[int(row[0]), float(row[1]), float(row[2]), float(row[3]), float(row[4])] for row in reader])

# Scenario 1
# Initialize variables for profit surplus
highest_net_profit_surplus_day = None
highest_net_profit_surplus_amount = float('-inf')

# Iterate through each row to check for profit surplus
for i in range(1, len(profit_and_loss_record)):
    current_day, current_amount = profit_and_loss_record[i][0], profit_and_loss_record[i][4]
    previous_day, previous_amount = profit_and_loss_record[i-1][0], profit_and_loss_record[i-1][4]

    # net_profit_surplus_amount = current_amount - previous_amount
    # if current_amount > previous_amount:
    net_profit_surplus_amount = current_amount - previous_amount
    if net_profit_surplus_amount > highest_net_profit_surplus_amount:
        highest_net_profit_surplus_amount = net_profit_surplus_amount
        highest_net_profit_surplus_day = current_day

# Print the result
print("[PROFIT SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY:")
print(f"[HIGHEST PROFIT SURPLUS] DAY: {highest_net_profit_surplus_day}, AMOUNT: SGD {highest_net_profit_surplus_amount}")


# Scenario 2
# Initialize variables for profit deficit
lowest_net_profit_deficit_day = None
lowest_net_profit_deficit_amount = float('inf')

# Iterate through each row to check for profit deficit
for i in range(1, len(profit_and_loss_record)):
    current_day, current_amount = profit_and_loss_record[i][0], profit_and_loss_record[i][4]
    previous_day, previous_amount = profit_and_loss_record[i-1][0], profit_and_loss_record[i-1][4]

    # Calculate the net profit deficit amount
    net_profit_deficit_amount = current_amount - previous_amount
    if net_profit_deficit_amount < lowest_net_profit_deficit_amount:
        lowest_net_profit_deficit_amount = net_profit_deficit_amount
        lowest_net_profit_deficit_day = current_day

# Print the result
#abs to absoluting the amount (removing negative sign)
print("[PROFIT DEFICIT] CASH ON EACH DAY IS LOWER THAN THE PREVIOUS DAY:")
print(f"[HIGHEST PROFIT DEFICIT] DAY: {lowest_net_profit_deficit_day}, AMOUNT: SGD {abs(lowest_net_profit_deficit_amount)}") 

# Scenario 3 
# Calculate net profit deficits and print the top 5
profit_deficits = sorted([(record[0], record[4] - profit_and_loss_record[i - 1][4]) for i, record in enumerate(profit_and_loss_record) if i != 0 and record[4] < profit_and_loss_record[i - 1][4]], key=lambda x: x[1])
for i in range(5):  # Print top 5 deficits
    print(f"[NET PROFIT DEFICIT] DAY: {profit_deficits[i][0]}, AMOUNT: SGD {abs(profit_deficits[i][1])}")


for i in range(5):  # Print top 5 deficits
    print(f"[NET PROFIT DEFICIT] DAY: {profit_deficits[i][0]}, AMOUNT: SGD {abs(profit_deficits[i][1])}")

# Print the highest, 2nd, and 3rd net profit deficit
print(f"[HIGHEST NET PROFIT DEFICIT] DAY: {profit_deficits[0][0]}, AMOUNT: SGD {abs(profit_deficits[0][1])}")
print(f"[2ND HIGHEST NET PROFIT DEFICIT] DAY: {profit_deficits[1][0]}, AMOUNT: SGD {abs(profit_deficits[1][1])}")
print(f"[3RD HIGHEST NET PROFIT DEFICIT] DAY: {profit_deficits[2][0]}, AMOUNT: SGD {abs(profit_deficits[2][1])}")