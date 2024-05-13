# THINGS TO BE DONE:
# Calculate: 
# total # of months in dataset;
# net total amount of profit/losses over entire period;
# changes in profit/losses over entire period, then average those changes
# greatest increase in profits (date and amount) over entire period
# greatest decrease in profits (date and amount) over entire period

# Modules
import csv

# Set path for file
csvpath = "hw/HW3/03-Python/Starter_Code/PyBank/Resources/budget_data.csv"

# A defining moment in a variable's life
months = 0
total_profit = 0
	# changes
last_month_profit = 0
changes = [] 
month_changes = []

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")

	# Read the header row first (skip this step if there is no header)
	csv_header = next(csvreader)
	print(f"CSV Header:{csv_header}")

# Read each row of data after the header
	for row in csvreader:
		print(row)
		
		# Step 1: count total number of months in dataset
		months = months + 1

		# Step 2: total sun of profit and loss
		total_profit = total_profit + int(row[1])

		# Step 3: Changes in "Profit/Losses" over entire period, then average changes
		# per prof: Need last month's profit; subtract this month's profit  -  last month's profit; append change to list
		# STEP 3 reminder: if first row, no change (b/c there is no previous month)
			# STEP 3 sub-reminder: per prof: If month count == 1, by definition, we're in first row
   
		if (months == 1):
			# in first row --- so no change
			last_month_profit = int(row[1])
		else:
			change = int(row[1]) - last_month_profit
			changes.append(change)
			month_changes.append(row[0])

			# reset last month's profit to be the current row we're in
			last_month_profit = int(row[1])
            
	print(months)
	print (total_profit)
	print(len(changes))

	ave_change = sum(changes) / len(changes)
	print(ave_change)

	max_change = max(changes)
	max_month_index = changes.index(max_change)
	max_month = month_changes[max_month_index]

	print(max_change )
	print(max_month)

	min_change = min(changes)
	min_month_index = changes.index(min_change)
	min_month = month_changes[min_month_index]
	# still need: keep track of the monoth's of the changes as an empty list; in our "else" we need to append the month as well, then grab the max of "changes", then call months.index to grab the month of the change (which we need to do for max and min) 