import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

# Lists storing variables
date = []
profit_loss = []

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
        
    #Remove header
    header = next(csvreader)
    
    for row in csvreader:
        # Add months
        date.append(row[0])
            
        # Add up net profit/loss total
        profit_loss.append(int(row[1]))
            
# Month total variable
month_count = len(date)
            
# Net profit/loss total variable
total_profit = sum(profit_loss)

# Profit/loss change list
pl_change = []

# Calculating profit/loss change
for month in range(1, month_count):
    pl_change.append(profit_loss[month] - (profit_loss[month - 1]))

# Calculate average change in profit/loss total
avg_prof_change = round(sum(pl_change) / (month_count - 1), 2)

# Calculate minimum change in p/l total for lowest increase
min_pl_diff = min(pl_change)

# Same calc for max for greatest increase
max_pl_diff = max(pl_change)

# Create output file
output_file = os.path.join("budget_data_final.txt")

# Variable for date of greatest pl increase
max_date = date[pl_change.index(max_pl_diff) + 1]

# Same as above for min
min_date = date[pl_change.index(min_pl_diff) + 1]

# Create list with text for txt file
lines = ["Financial Analysis", "", "------------------------", "", "Total Months: " + str(month_count), "Total: $" + str(total_profit), "Average Change: $" + str(avg_prof_change), "Greatest Increase in Profits: " + str(max_date) + " ($" + str(max_pl_diff) + ")", "Greatest Decrease in Profits: " + str(min_date) + " ($" + str(min_pl_diff) + ")"]

# Open the output file
with open(output_file, "w") as f:
    # Create loop to add line break after each comma in list above
    for line in lines:
        f.write(line)
        f.write('\n')

# Print to terminal
print("Financial Analysis")
print("---------------------")
print("Total Months: " + str(month_count))
print("Total: $" + str(total_profit))
print("Average Change: $" + str(avg_prof_change))
print("Greatest Increase in Profits: " + str(max_date) + " ($" + str(max_pl_diff) + ")")
print("Greatest Decrease in Profits: " + str(min_date) + " ($" + str(min_pl_diff) + ")")
