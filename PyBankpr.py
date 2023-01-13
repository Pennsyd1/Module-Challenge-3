import os
import csv

PyBank_csv = os.path.join("..", "Instructions", "PyBank", "Resources", "budget_data.csv")

with open (PyBank_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    monthcount = []
    total_profit = []
    for col in csv_reader:
        monthcount.append(col[0])
        total_profit.append(col[1])
print(f"Total Months: {int(len(monthcount))}")

profit = 0        
for num in range(0, len(total_profit)):
    profit = int(profit) + int(total_profit[num])
print(f"Total: ${int(profit)}")

