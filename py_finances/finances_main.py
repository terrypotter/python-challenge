# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
from statistics import mean
# Module for reading CSV files
import csv

# Path for csv file
csvpath = os.path.join('budget_data.csv')


# Reading using CSV module

with open(csvpath, newline='', encoding="utf-8") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Create list and read each row of data after the header
    fin_data = []
    for row in csvreader:
        fin_data.append(row[0:2])
        
    # Create a list for profits and loss data   
    prof_loss = []
    # Create a list containing net month to month profit and loss
    site_limits = []
    # Read profit and loss data from fin_data into prof_loss
    for row in fin_data:
        prof_loss.append(row[0])
    # Delete header info
    prof_loss.pop(0)
    # Read net month to month profit and loss data 
    for i in range(len(prof_loss)):
        if i != 0:
            site_limits.append(
                int(prof_loss[i]) - int(prof_loss[i-1]))
    # Find max profit/loss
    max_limit = max(site_limits)
    # Find index of corresponding max profit/loss
    ind_max = site_limits.index(max_limit)
    # Find min profit/loss
    min_limit = min(site_limits)
    # Find index corresponding to min profit/loss
    ind_min = site_limits.index(min_limit)
    # Find average profit/loss
    avg_site_limit = mean(site_limits)
    # Find total profit/loss
    for i in range(0, len(prof_loss)):
        prof_loss[i] = int(prof_loss[i])
    sum_pl = sum(prof_loss)

# Create string containing MM YY corresponding to max and min profit/loss
# +2 is correction from pop and loop used above
x = (str(fin_data[ind_max +2])).split("'")
y = (str(fin_data[ind_min +2])).split("'")

# Create string containing output
Results = (
f" Financial Analysis \n"
f"-------------------------\n"
f"Total Months: {len(prof_loss)} \n"
f"Total: ${sum_pl} \n"
f"Average Change: ${round(avg_site_limit,2)} \n"
f"Greatest Increase in Profit: {x[3]} (${max_limit}) \n"
f"Greatest Decrease in Profit: {y[3]} (${min_limit}) \n")
# Print output to cmd screen
print(Results)
# Create path to publish results and name file
publish_data = os.path.join('py_finances_results.txt')
# Create the write file with results
with open(publish_data, 'w') as text_file:
    text_writer = text_file.write(Results)





