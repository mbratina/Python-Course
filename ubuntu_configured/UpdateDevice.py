import csv
with open('device.csv', 'w') as csvfile:
	fieldnames = ['hostname', 'user', 'password']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	writer.writerow({'hostname':'router1', 'user':'Joe', 'password':'Passw0rd1#'})
	writer.writerow({'hostname':'router2', 'user':'Fred', 'password':'Passw0rd1#'})
	writer.writerow({'hostname':'router3', 'user':'Sam', 'password':'Passw0rd1#'})
	writer.writerow({'hostname':'router4', 'user':'Lou', 'password':'Passw0rd1#'})