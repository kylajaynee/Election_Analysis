# The data we need to retrieve.
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Percentage of votes each candidate won
# 4. Total number of votes each candidate won
# 5. The winner of the election based on popular vote. 
# Import dependencies
import csv
import os
# Assign a variable for file and load path
file_to_load = os.path.join(".", "Resources", "election_results.csv")
# file_to_load = "Resources\election_results.csv"

# Create and assign variable and path to file
file_to_save = os.path.join(".", "analysis", "election_analysis.txt")


# Open election results and read file
with open(file_to_load) as election_data:
    # Read file with reader function 
    file_reader = csv.reader(election_data)

    # Print Header row
    headers = next(file_reader)
    print(headers)
