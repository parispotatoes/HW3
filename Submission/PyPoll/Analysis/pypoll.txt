import csv

csvpath = "Resources/election_data.csv"

# Variables
votect = 0
can_dict = {}

with open(csvpath, encoding='UTF-8') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")

	# Read header row first (skip if no header)
	csv_header = next(csvreader)
	print(f"CSV Header: {csv_header}")

	# Read each row of data after header
	for row in csvreader:
		# count votes
		votect += 1

		# add to dictionary
		row_candidate = row[2]
		if row_candidate in can_dict.keys():
			can_dict[row_candidate] += 1
		else:
			can_dict[row_candidate] = 1

print(votect)
print(can_dict)

# output
output = f"""Election Results
-------------------------
Total Votes: 369711
-------------------------\n"""

max_can = ""
max_votect = 0

for candidates in can_dict.keys():
	# get votes
	votes = can_dict[candidates]
	perc = 100 * (votes / votect)

	line = f"{candidates}: (round(perc, 3))% ({votes})\n"
	output += line

	# get max of dictionary
	if votes > max_votect:
		max_can = candidates
		max_votect = votes

last_line = f"""-------------------------
Winner: {max_can}
-------------------------"""
output += last_line

print(output)

with(open("output_pypoll.txt", 'w') as f):
	f.write(output)