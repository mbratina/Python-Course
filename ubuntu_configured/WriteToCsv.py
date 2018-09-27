import csv
DeviceData=[['router4', 'Lou', 'Passw0rd1!']]
File = open('newfile', 'w')
with File:
	writer = csv.writer(File)
	writer.writerows(DeviceData)
print('The file has been created')