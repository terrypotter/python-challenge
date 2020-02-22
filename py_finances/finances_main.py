# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
from statistics import mean
# Module for reading CSV files
import csv

csvpath = os.path.join('budget_data.csv')


# Method 2: Improved Reading using CSV module

with open(csvpath, newline='', encoding="utf-8") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is no header)
    #csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    fin_data = []
    for row in csvreader:
        fin_data.append(row[0:2])
        
       
    prof_loss = []
    site_limits = []
    for row in fin_data:
        prof_loss.append(row[0])
        #prof_loss = int(prof_loss)
    prof_loss.pop(0)
    #print(prof_loss)

    for i in range(len(prof_loss)):
        if i != 0:
            site_limits.append(
                int(prof_loss[i]) - int(prof_loss[i-1]))

    max_limit = max(site_limits)
    ind_max = site_limits.index(max_limit)
    min_limit = min(site_limits)
    ind_min = site_limits.index(min_limit)
    avg_site_limit = mean(site_limits)
    for i in range(0, len(prof_loss)):
        prof_loss[i] = int(prof_loss[i])
    sum_pl = sum(prof_loss)

# +2 is correction from pop used above and loop
x = (str(fin_data[ind_max +2])).split("'")
y = (str(fin_data[ind_min +2])).split("'")

Results = (
f" Financial Analysis \n"
f"-------------------------\n"
f"Total Months: {len(prof_loss)} \n"
f"Total: ${sum_pl} \n"
f"Average Change: ${round(avg_site_limit,2)} \n"
f"Greatest Increase in Profit: {x[3]} (${max_limit}) \n"
f"Greatest Decrease in Profit: {y[3]} (${min_limit}) \n")
print(Results)
#create path to publish results
publish_data = os.path.join('py_finances_results.txt')
#create the write file with results
with open(publish_data, 'w') as text_file:
    text_writer = text_file.write(Results)





