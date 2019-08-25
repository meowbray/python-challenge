import os
import csv

#function juction
def count(csvfile):
    total_votes = 0
    percent = 0
    name = {}
    winner = ''
    
    
    for row in csvfile:
        total_votes += 1
        voteid = row[0]
        vote = row[2]

        if vote in name:

    return[total_votes]

with open(os.path.join('Resources', 'election_data.csv')) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    results = count(csvreader)
print()
 = open("results.text",'w')