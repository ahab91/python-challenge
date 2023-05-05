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
        
        # Extract candidate name
        candidate = row[2]
        
winning_count = 0
winner = ""
        
# Variable for total count of votes
total_count = len(id)

# List for unique candidate names
cand_names = []
cand_votes = {}
for candidate in cand:
    if candidate not in cand_names:
        cand_names.append(candidate)
        cand_votes[candidate] = 0
    cand_votes[candidate] = cand_votes[candidate] + 1


print("Election Results")
print("------------------------")
print("Total Votes: " + str(total_count))
print("------------------------")
output_file = os.path.join("Analysis", "election_results.txt")

with open(output_file, 'w') as f:
    f.write("Election Results"'\n')
    f.write("------------------------"'\n')
    f.write("Total Votes: " + str(total_count))
    f.write('\n'"------------------------"'\n')
    for cand_opt in cand_votes:
        votes = cand_votes.get(cand_opt)
        pct = round((((votes) / total_count) * 100), 3)
        if (votes > winning_count):
            winning_count = votes
            winner = cand_opt
        print(str(cand_opt) + ": ", str(pct) + "% ", "(" + str(votes) + ")")
        f.write('\n'"" + str(cand_opt) + ": ")
        f.write(str(pct) + "% ")
        f.write("(" + str(votes) + ")"'\n')
    f.write('\n'"------------------------"'\n')
    f.write('\n'"Winner: " + winner)

print("------------------------")
print("Winner: " + str(winner))
print("------------------------")
    

