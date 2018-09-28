import requests

url = "https://192.168.10.100/api/interfaces/physical"

headers = {'Authorization': 'Basic ZW5hYmxlXzE6Y2lzY28='}

response = requests.request("GET", url, verify=False,  headers=headers)

print(response.text)
