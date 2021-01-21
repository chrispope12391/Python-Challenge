# This will allow us to create a file path across operating systems
import os

# creates a module for reading csv files
import csv

#create variables to store values
months = []
total_amount = 0
previous_value = 0
total_months = 0
monthly_change = 0
total_change = 0
average_change = 0
new_months = 0
store_change = []


#creates the path to pull the csv file
csvpath = os.path.join("..", "Resources", "PyBank_data.csv")

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
        total_months += 1

        #calculates the month by month change in the profit/losses column
        if (total_months == 1):
                previous_value = int(row[1])

        else:
                monthly_change = int(row[1]) - previous_value
                previous_value = int(row[1])

        #sums all of the monthly changes
        total_change = monthly_change + total_change

        #stores the monthly changes into a list
        store_change.append(int(monthly_change))
        months.append(row[0])

        #sums the profits/losses over the entire period
        total_amount = total_amount + (int(row[1]))

        
#calculates the average change over the entire period
new_months = int(total_months) - 1
average_change = total_change / new_months

# locates the greatest monthly increase
greatest_increase = max(store_change)
# print(greatest_increase)

#locates the month when the greatest positive change in value occured
store_position = store_change.index(greatest_increase)
greatest_position = (months[store_position])

# locates the greatest monthly decrease
greatest_decrease = min(store_change)
# print(greatest_decrease)

# locates the month when the greatest decrease in value occurred
store_decrease = store_change.index(greatest_decrease)
least_position = (months[store_decrease])
# print(least_position)

#prints a header for our analysis
print("-------------------------------")
print("Financial Analysis")
print("-------------------------------")

# prints out all of the values that were calculated above
print(f"Total Months: {total_months}")
print(f"Total: ${total_amount}")
change_amount = (str(round(average_change, 2)))
print(f"Average Change: ${change_amount}")
print(f"Greatest Increase in Profits: {greatest_position} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {least_position} (${greatest_decrease})")

#creates a variable to write the new csv file to
output_file = os.path.join("bank_output.csv")

with open(output_file, 'w') as datafile:

        writer = csv.writer(datafile, delimiter=' ')
        
        # writes the financial analysis results above to a new csv file
        #[3]
        datafile.write('---------------------------\n')
        datafile.write('Financial Analysis\n')
        datafile.write('---------------------------\n')
        datafile.write(f"Total Months: {total_months}\n")
        datafile.write(f"Total: ${total_amount}\n")
        datafile.write(f"Average Change: ${change_amount}\n")
        datafile.write(f"Greatest Increase in Profits: {greatest_position} (${greatest_increase})\n")
        datafile.write(f"Greatest Decrease in Profits: {least_position} (${greatest_decrease})\n")

     


    
