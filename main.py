from pathlib import Path
import overheads
import profit_loss
import cash_on_hand

# Define file path for the summary report
file_path = Path.cwd() / "summary_report.txt"

# Open the file for writing
with file_path.open(mode="r", encoding="UTF-8", newline="") as f:
    # scenario 1
    # Write highest overhead
    f.write(f"\nHighest Overhead: {overheads.highest_overhead_category}, AMOUNT: SGD {overheads.highest_value}%\n")

    # write cash surplus
    f.write(f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY:\n")
    f.write(f"[HIGHEST CASH SURPLUS] DAY: {cash_on_hand.highest_surplus_day}, AMOUNT: SGD {cash_on_hand.highest_surplus_amount}\n")

    # write profit surplus
    f.write(f"[PROFIT SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY:\n")
    f.write(f"[HIGHEST PROFIT SURPLUS] DAY: {profit_loss.highest_net_profit_surplus_day}, AMOUNT: SGD {profit_loss.highest_net_profit_surplus_amount}\n")

# scenario 2 
    # Write highest overhead
    f.write(f"\nHighest Overhead: {overheads.highest_overhead_category}, AMOUNT: SGD {overheads.highest_value}%\n")

    # write cash deficit
    f.write(f"[CASH DEFICIT] CASH ON EACH DAY IS LOWER THAN THE PREVIOUS DAY:\n")
    f.write(f"[HIGHEST CASH DEFICIT] DAY: {cash_on_hand.lowest_deficit_day}, AMOUNT: SGD {abs (cash_on_hand.lowest_deficit_amount)}\n")
#abs to absoluting the amount (removing negative sign)
    
    # write profit surplus
    f.write(f"[PROFIT DEFICIT] CASH ON EACH DAY IS LOWER THAN THE PREVIOUS DAY:\n")
    f.write(f"[HIGHEST PROFIT DEFICIT] DAY: {profit_loss.lowest_net_profit_deficit_day}, AMOUNT: SGD {abs(profit_loss.lowest_net_profit_deficit_amount)}\n") 

# scenario 3
    # Write highest overhead
    f.write(f"\nHighest Overhead: {overheads.highest_overhead_category}, AMOUNT: SGD {overheads.highest_value}%\n")

    # Write top 20 cash deficits
    for cash_deficit in cash_on_hand.cash_deficits_sorted[:20]:
        f.write(f"[CASH DEFICIT] DAY: {cash_deficit[0]}, AMOUNT: SGD {abs(cash_deficit[1])}\n")

    # Write the highest, 2nd highest, and 3rd highest cash deficit
    f.write(f"[HIGHEST CASH DEFICIT] DAY: {cash_on_hand.cash_deficits_sorted[0][0]}, AMOUNT: SGD {abs(cash_on_hand.cash_deficits_sorted[0][1])}\n")
    f.write(f"[2ND HIGHEST CASH DEFICIT] DAY: {cash_on_hand.cash_deficits_sorted[1][0]}, AMOUNT: SGD {abs(cash_on_hand.cash_deficits_sorted[1][1])}\n")
    f.write(f"[3RD HIGHEST CASH DEFICIT] DAY: {cash_on_hand.cash_deficits_sorted[2][0]}, AMOUNT: SGD {abs(cash_on_hand.cash_deficits_sorted[2][1])}\n")

#write top 20 profit deficits
    for i in range(min(20, len(profit_loss.profit_deficits_sorted))):  
        f.write(f"[NET PROFIT DEFICIT] DAY: {profit_loss.profit_deficits_sorted[i][0]}, AMOUNT: SGD {abs(profit_loss.profit_deficits_sorted[i][1])}\n")

#.write the highest, 2nd, and 3rd net profit deficit
    f.write(f"[HIGHEST NET PROFIT DEFICIT] DAY: {profit_loss.profit_deficits_sorted[0][0]}, AMOUNT: SGD {abs(profit_loss.profit_deficits_sorted[0][1])}\n")
    f.write(f"[2ND HIGHEST NET PROFIT DEFICIT] DAY: {profit_loss.profit_deficits_sorted[1][0]}, AMOUNT: SGD {abs(profit_loss.profit_deficits_sorted[1][1])}\n")
    f.write(f"[3RD HIGHEST NET PROFIT DEFICIT] DAY: {profit_loss.profit_deficits_sorted[2][0]}, AMOUNT: SGD {abs(profit_loss.profit_deficits_sorted[2][1])}\n")
print("Summary report has been written to summary_report.txt")