import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")

# Lists for storing variables
id = []
county = []
cand = []

with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Remove header for data analysis
    header = next(csvreader)
    
    # Set up loop to add contents to lists
    for row in csvreader:
    
        # Add ballot id
        id.append(int(row[0]))
        
        # Add county
        county.append(row[1])
        
        # Add candidate
        cand.append(row[2])
        
# Variable for total count of votes
total_count = len(id)

# List for unique candidate names
cand_names = []
for name in cand:
    if name not in cand_names:
        cand_names.append(name)

stockham_vote = 0
degette_vote = 0
doane_vote = 0
winner_name = []

for vote in cand:
    if vote == cand_names[0]:
        stockham_vote = stockham_vote + 1
    if vote == cand_names[1]:
        degette_vote = degette_vote + 1
    if vote == cand_names[2]:
        doane_vote = doane_vote + 1

for winner in cand_names:
    if stockham_vote > degette_vote and doane_vote:
        winner = cand_names[0]
    if degette_vote > stockham_vote and doane_vote:
        winner = cand_names[1]
    if doane_vote > stockham_vote and degette_vote:
        winner = cand_names[2]
    

ccs_percent = round((stockham_vote) / (total_count) * 100, 3)
dd_percent = round((degette_vote) / (total_count) * 100, 3)
rad_percent = round((doane_vote) / (total_count) * 100, 3)

win_count = max(stockham_vote, degette_vote, doane_vote)
winner_percent = max(ccs_percent, dd_percent, rad_percent)

output_file = os.path.join("Analysis", "election_results.txt")

lines = ["Election Results", "", "------------------------", "", "Total Votes: " + str(total_count), "------------------------", str(cand_names[0]) + ": " + str(ccs_percent)+'%' + " (" + str(stockham_vote) + ")", str(cand_names[1]) + ": " + str(dd_percent)+'%' + " (" + str(degette_vote) + ")", str(cand_names[2]) + ": " + str(rad_percent)+'%' + " (" + str(doane_vote) + ")", "", "------------------------", "", "Winner: " + str(winner), "", "------------------------"]

with open(output_file, "w") as f:
    for line in lines:
        f.write(line)
        f.write('\n')

# Print to terminal
print("Election Results")
print("------------------------")
print("Total Votes: " + str(total_count))
print("------------------------")
print(str(cand_names[0]) + ": " + str(ccs_percent)+'%' + " (" + str(stockham_vote) + ")")
print(str(cand_names[1]) + ": " + str(dd_percent)+'%' + " (" + str(degette_vote) + ")")
print(str(cand_names[2]) + ": " + str(rad_percent)+'%' + " (" + str(doane_vote) + ")")
print("------------------------")
print("Winner: " + str(winner))
print("------------------------")
