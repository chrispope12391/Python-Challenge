# This will allow us to create a file path across operating systems
import os

# creates a module for reading csv files
import csv

candidates_list = []
winner = 0
winner_list = []
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
o_tooley_votes = 0

#creates the path to pull the csv file
csvpath = os.path.join("..", "Resources", "PyPoll_data.csv")

# print(csvpath)


#Create CSV module for reading file
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)
    
    #skips the header row
    csv_header = next(csvreader)
    # print(f"csv header: {csv_header}")


        #reads the rows of data past the header row
    for row in csvreader:
        total_votes += 1

        if row[2] == "Khan":
            khan_votes += 1

        if row[2] == "Correy":
            correy_votes += 1

        if row[2] == "Li":
            li_votes += 1

        if row[2] == "O'Tooley":
            o_tooley_votes += 1

        # stores the unique values from the candidates list
        #[1]
        if row [2] not in candidates_list:
            candidates_list.append(row[2])

# print(total_votes)
# print(khan_votes)
# print(correy_votes)
# print(li_votes)
# print(o_tooley_votes)

#finds the percentages for each candidate
#[2]
khan_percentage = ("{:.3%}".format(khan_votes  / total_votes))
# print(khan_percentage)

correy_percentage = ("{:.3%}".format(correy_votes / total_votes))
# print(correy_percentage)

li_percentage = ("{:.3%}".format(li_votes / total_votes))
# print(li_percentage)

o_tooley_percentage = ("{:.3%}".format(o_tooley_votes / total_votes))
# print(o_tooley_percentage)

winner_list = max(khan_votes, correy_votes, li_votes, o_tooley_votes)

winner = winner_list


#prints a header for our election results
print("-------------------------------")
print("Election Results")
print("-------------------------------")

#print the total amount of votes in the spreadsheet
print(f"Total Votes: {total_votes}")
print("-------------------------------")

#print election results
print(F"{candidates_list[0]}: {khan_percentage} ({khan_votes})")
print(F"{candidates_list[1]}: {correy_percentage} ({correy_votes})")
print(F"{candidates_list[2]}: {li_percentage} ({li_votes})")
print(F"{candidates_list[3]}: {o_tooley_percentage} ({o_tooley_votes})")
print("-------------------------------")

# calculates what candidate has the most votes and prints which candidate won
if (winner == khan_votes):
   print("Winner: Khan")

elif (winner == correy_votes):
    print("Winner: Correy")

elif (winner == li_votes):
    print("Winner: Li")

elif (winner == o_tooley_votes):
    print("Winner: O'Tooley")
print("-------------------------------")

# print(winner_list)
# print(candidates_list)

#creates a variable to write the csv to
output_file = os.path.join("election_output.csv")

with open(output_file, 'w') as datafile:

        writer = csv.writer(datafile, delimiter=' ')
        
        # prints out the results above to a new csv file titles election_output.csv
        #[3]
        datafile.write('---------------------------\n')
        datafile.write('Election Results\n')
        datafile.write('---------------------------\n')
        datafile.write(f"Total Votes: {total_votes}\n")
        datafile.write('---------------------------\n')
        datafile.write(F"{candidates_list[0]}: {khan_percentage} ({khan_votes})\n")
        datafile.write(F"{candidates_list[1]}: {correy_percentage} ({correy_votes})\n")
        datafile.write(F"{candidates_list[2]}: {li_percentage} ({li_votes})\n")
        datafile.write(F"{candidates_list[3]}: {o_tooley_percentage} ({o_tooley_votes})\n")
        datafile.write('---------------------------\n')
        if (winner == khan_votes):
            datafile.write(F"Winner: Khan\n")

        elif (winner == correy_votes):
            datafile.write(F"Winner: Correy\n")

        elif (winner == li_votes):
            datafile.write(F"Winner: Li\n")

        elif (winner == o_tooley_votes):
            datafile.write(F"Winner: O'Tooley\n")
        datafile.write('---------------------------\n')

