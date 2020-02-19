import csv
import os

budget_path= ('Resources/budget_data.csv')
with open (budget_path, newline='') as file:
    csvreader=csv.reader(file, delimiter=',')
    next(csvreader)

    total_months=0
    total=0
    average_change=0
    greatest_decrease=0
    greatest_increase=0
    months=[]
    values=[]
    changes=[]
    for row in csvreader:
        months.append(row[0])
        total_months+=1
        total+=int(row[1])
        values.append(int(row[1]))

    for idx, val in enumerate(values):
        changes.append((values[idx])-values[idx-1])
    average_change=round(sum(changes[1:])/(len(changes)-1),2)

    greatest_decrease=min(changes)
    greatest_increase=max(changes)

    key_list=['Total Months', 'Total', 'Average Change', 'Greatest Increase in Profits', 'Greatest Decrease in Profits']
    value_list=[total_months, total, average_change, greatest_increase, greatest_decrease]
    cleaned_report=zip(key_list,value_list)

    print("Financial Analysis \n ___________________________")
    print("Total Months: " + str(total_months))
    print("Total: " + str(total))
    print("Average Change: " + str(average_change))
    print("Greatest Increase in Profits: " + str(greatest_increase))
    print("Greatest Decrease in Profits: " + str(greatest_decrease))

output_file = os.path.join("pybank.txt")
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Metric", "Value"])
    writer.writerows(cleaned_report)
