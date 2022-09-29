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

# 1. Initialize a total vote counter 
total_votes = 0

# Candidate Options and 1. candidate votes.
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning count tracker
winning_candidate = ""
winning_count = 0 
winning_percentage = 0

# Open election results and read file
with open(file_to_load) as election_data:
    # Read file with reader function 
    file_reader = csv.reader(election_data)

    # Read Header row
    headers = next(file_reader)
    
    # Print each row in CSV file
    for row in file_reader:
        #2. Add to the total vote count
        total_votes += 1

        # Get candidate names
        candidate_name = row[2]
        # Add candidate name to candidate list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            # 2. Begin tracking candidate's vote count
            candidate_votes[candidate_name] = 0
        # Add votes to candidate's count
        candidate_votes[candidate_name] += 1

        #Determine percent of votes for each candidate by looping through 
        #1. Iterate through Cadidate list
    for candidate_name in candidate_votes:
        #2. Retreive vote count for candidate
        votes = candidate_votes[candidate_name]
        #3. calculate percent
        vote_percentage = float(votes) / float(total_votes) * 100
        #4. print candidate name and percentage of votes
        # print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Determine winning vote count and candidate
        # Determine if votes is greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #if true then set winning count and percent
            winning_count = votes
            winning_percentage = vote_percentage
            # Set winning candiates name
            winning_candidate = candidate_name
        
    # Print winning candidate summary
    winning_candidate_summary = (
        f"-------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------\n")
    print(winning_candidate_summary)

    #3. Print total votes
    # print(total_votes)
    # print(candidate_votes)
