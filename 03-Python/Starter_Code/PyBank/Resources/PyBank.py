# Modules
import csv

# Set path for file
csvpath = "hw/HW3/03-Python/Starter_Code/PyBank/Resources/budget_data.csv"

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

        # Read the header row first (skip this step if there is no header)
        csv_header = next(csvreader)
        print(f"CSV Header:{csv_header}")

# Read each row of data after the header
for row in csvreader:
    print(row)