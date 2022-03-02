import csv
 with open('iris.data','RB')as csv file:
lines=csv.reader(csv file)
for row in lines:
    print(','.join(row))