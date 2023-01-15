import pandas as pd
csv_path = 'Instructions/PyPoll/Resources/election_data.csv'
pypoll = pd.read_csv(csv_path, encoding = "ISO-8859-1")

votes = pypoll["Ballot ID"].value_counts()
 
print("Total Votes:" + str(len(votes)))

new_df = pypoll.loc[pypoll["Candidate"] == "Charles Casper Stockham"]
print(new_df.head())
CSSvotes = new_df["Ballot ID"].value_counts()
print(len(new_df))
CSSvote = (len(new_df))
vote = (len(votes))

dosnew_df = pypoll.loc[pypoll["Candidate"] == "Diana DeGette"]
DDvotes = dosnew_df["Ballot ID"].value_counts()
print(len(dosnew_df))
DDvote = (len(dosnew_df))

tresnew_df = pypoll.loc[pypoll["Candidate"] == "Raymon Anthony Doane"]
RADvotes = tresnew_df["Ballot ID"].value_counts()
print(len(tresnew_df))
RADvote = (len(tresnew_df))



perc = (int(CSSvote) / int(vote)) * 100
print("Charles Casper Stockham: " + str(perc) + "%  " + str(len(new_df)))

perc2 = (int(DDvote) / int(vote)) * 100
print("Diana DeGette: " + str(perc2) + "%  " + str(len(dosnew_df)))

perc3 = (int(RADvote) / int(vote)) * 100
print("Raymon Anthony Doane: " + str(perc3) + "%  " + str(len(tresnew_df)))

print("Winner: Diana DeGette")
