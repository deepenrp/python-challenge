
import os
import sys
import csv

cwd = os.getcwd()

#print(cwd)


csvpath = os.path.join('election_data.csv')


with open(csvpath, newline='') as election_data_file:
    csvreader = csv.reader(election_data_file, delimiter=',')

    #print(csvreader)


    output_file = open("election_results.txt", "w")
    
    csv_header = next(csvreader)
    
    #print(f"CSV Header: {csv_header}")

 # Read each row of data after the header

    print("Election Results")
    print("---------------------------------------------------")
    output_file.write("Election Results")
    output_file.write("---")

    candids = ["Khan", "Correy", "Li", "O'Tooley"]

    votes = 0
    khan = 0
    correy = 0
    li = 0
    otooley = 0

    for row in csvreader:
        votes = votes + 1
        if str(row[2]) == str("Khan"):
            khan = khan + 1
        elif str(row[2]) == str("Correy"):
            correy = correy + 1
        elif str(row[2]) == str("Li"):
            li = li + 1
        elif str(row[2]) == str("O'Tooley"):
            otooley = otooley +1

    khan_percent = round((khan / votes) * 100, 2)
    correy_percent = round((correy / votes) * 100, 2)
    li_percent = round((li / votes) * 100, 2)
    otooley_percent = round((otooley / votes) * 100, 2)
    
    candidates = {
            khan: "Khan",
            correy: "Correy",
            li: "Li",
            otooley: "O'Tooley"
            }
    
    most_votes = max(khan, correy, li, otooley)
    
 

print(f"Total Votes: {votes}")
print("---------------------------------------------------")
print(f"Khan: {khan_percent}% ({khan})")
print(f"Correy: {correy_percent}% ({correy})")
print(f"Li: {li_percent}% ({li})")
print(f"O'Tooley: {otooley_percent}% ({otooley})")
print("------------------------------------------------")
print("Winner: " + f'{candidates[most_votes]}')
print("------------------------------------------------")


output_file.write(f"Total Votes: {votes}")
output_file.write("---")
output_file.write(f"Khan: {khan_percent}% ({khan})")
output_file.write(f"Correy: {correy_percent}% ({correy})")
output_file.write(f"Li: {li_percent}% ({li})")
output_file.write(f"O'Tooley: {otooley_percent}% ({otooley})")
output_file.write("---")
output_file.write("Winner: " + f'{candidates[most_votes]}')
output_file.write("---")




# Below is a simple script to print results to a text file with print outputs line by line
# However, I am unable to print results in text file and display on terminal at the same time

#>>> sys.stdout = open("election_results.txt", "w")
#>>> print(sys.stdout)
#>>> sys.stdout.close()