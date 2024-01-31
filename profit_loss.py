import csv
from pathlib import Path

# create a file path to the CSV file.
file_paths = [ 
    Path.cwd() / "profit-and-loss-sgd (11-30).csv",
    Path.cwd() / "profit-and-loss-sgd (31-60).csv",
    Path.cwd() / "profit-and-loss-sgd (61-90).csv"
]

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
# Calculate net profit deficits
profit_deficits =[(record[0], record[4] - profit_and_loss_record[i - 1][4]) for i, record in enumerate(profit_and_loss_record) if i != 0 and record[4] < profit_and_loss_record[i - 1][4]]

# Define a function to extract the deficit amount for sorting
def profit_deficit_amount(item):
    return item[1]

# Sort the profit deficits in reverse order based on the deficit amount
profit_deficits_sorted = sorted(profit_deficits, key=profit_deficit_amount, reverse = False)

# Print top 20 deficits
for i in range(min(20, len(profit_deficits_sorted))):  
    print(f"[NET PROFIT DEFICIT] DAY: {profit_deficits_sorted[i][0]}, AMOUNT: SGD {abs(profit_deficits_sorted[i][1])}")

# Print the highest, 2nd, and 3rd net profit deficit
print(f"[HIGHEST NET PROFIT DEFICIT] DAY: {profit_deficits_sorted[0][0]}, AMOUNT: SGD {abs(profit_deficits_sorted[0][1])}")
print(f"[2ND HIGHEST NET PROFIT DEFICIT] DAY: {profit_deficits_sorted[1][0]}, AMOUNT: SGD {abs(profit_deficits_sorted[1][1])}")
print(f"[3RD HIGHEST NET PROFIT DEFICIT] DAY: {profit_deficits_sorted[2][0]}, AMOUNT: SGD {abs(profit_deficits_sorted[2][1])}")