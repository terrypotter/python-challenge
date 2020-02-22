# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Import module operator
import operator

# Path to CSV file
csvpath = os.path.join('houston_election_data.csv')

# Reading using CSV module

with open(csvpath, newline='', encoding="utf-8") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

# Create dictionary using data from csvreader   
    cand_data = {}
    for row in csvreader:
        if row[0] not in cand_data.keys():
            cand_data[row[0]] = 1
            
        else:
            cand_data[row[0]] += 1

# Delete header            
    cand_data.pop("Candidate")
# Calculate total votes
    total_votes = (sum(cand_data.values())) 
# Sort dictionary in descending order
    sorted_cand_data = dict( sorted(cand_data.items(), key=operator.itemgetter(1),reverse=True))
# Create a list of dictionary keys (candidate names)
    adv_cand = list(sorted_cand_data.keys())

# Write first part of output to a text file
    f = open("py_elections_results.txt", "w")
    f.write(
    f" Houston Mayoral Election Results \n"
    f"----------------------------------\n"
    f"Total Cast Votes: {total_votes} \n"
    f"----------------------------------\n")
    f.close()
# Append previously created text file (candidate names and voting info)    
    for x, y in sorted_cand_data.items():
        z = round(((y/total_votes)*100),2)
        f = open("py_elections_results.txt", "a")
        f.write(f"{x}:  {z}%  ({y}) \n")
        f.close()
# Final append to previously created text file
    f = open("py_elections_results.txt", "a")
    f.write(
    f"----------------------------------\n"
    f"1st Advancing Candidate: {adv_cand[0]} \n"
    f"2nd Advancing Candidate: {adv_cand[1]} \n"
    f"----------------------------------\n")  
    f.close()
# Open text file and print to cmd window
    f = open("py_elections_results.txt", "r")
    print(f.read())
    f.close()
        

    
    


    
