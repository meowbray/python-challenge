import os 
import csv

#csv


#Function Junction
def bank(hw):

#total months
    month = 0   
#total Profit/losses
    total = 0
#Average Change Profit/loss
    avg_chng = 0
#greatest increase (date/Amount)
    max_rev = 0
    max_month = ""
#greatest decrease (date/amount)
    min_rev = 0
    min_month = ""
    #loop
    for row in csvfile:
        current_month = row[0]
        pal = row[1]
        month += 1
        total += row[1]
        avg_chng = (total/month)
        if pal > max_rev:
            max_rev = pal
            max_month = current_month
        elif pal < min_rev:
            min_rev = pal
            min_month = current_month
    return [month, total, avg_chng, max_month, max_rev, min_month, min_rev]

#call
#print
#write

with open(os.path.join('Resources', 'budget_data.csv')) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    analysis = bank(csvreader)
print(analysis[0, 1, 2, 3, 5, 4, 7, 6])

analysis = open("results.text",'w')




#print
#write