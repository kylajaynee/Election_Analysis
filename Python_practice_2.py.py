counties = ["Arapahoe", "Denver", "Jefferson"]
print(counties)
counties_dict = {}
counties_dict ["Arapahoe"] = 422829
counties_dict ["Denver"] = 463353
counties_dict ["Jefferson"] = 432438
print(counties_dict.keys())
print(len(counties_dict))
voting_data = []
voting_data.append({"county": "Arapahoe", "registered_voters":422829})
voting_data.append({"county":"Denver", "registered_voters":463353})
voting_data.append({"county":"Jefferson", "registered_voters":432438})
print(voting_data)
voting_data.insert(1,{"county":"El Paso", "registered_voters":461149})
voting_data.pop(0)
voting_data.remove({"county":"Denver", "registered_voters":463353})
voting_data.append({"county":"Denver", "registered_voters":463353})
voting_data.append({"county": "Arapahoe", "registered_voters":422829})
print(voting_data)
# How many votes did you get?
my_votes = int(input("how many votes did you get in the election?"))
#Total votes in election
total_votes = int(input("What is the total votes in the election?"))
# Calculate the percentage of votes you got 
percentage_votes = int((my_votes / total_votes) * 100)
print(f"I received", percentage_votes, " percent of the total votes.")