import csv
with open('device.csv') as csvfile:
    testreader = csv.reader(csvfile, delimiter = ' ', quotechar= '|')
#    for row in testreader:
#        print ''.join(row)
#        print row[1]
#        print row[2]
    for line_number, row in zip(range(2), csvfile):
    	print row