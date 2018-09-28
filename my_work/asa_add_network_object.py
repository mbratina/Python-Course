import requests

url = "https://192.168.10.100/api/objects/networkobjects"

payload = "{\r\n  \"host\": {\r\n    \"kind\": \"IPv4Address\",\r\n    \"value\": \"1.10.8.10\"\r\n  },\r\n  \"kind\": \"object#NetworkObj\",\r\n  \"name\": \"ASA_Demo_NObj_1190\",\r\n  \"objectId\": \"ASA_Demo_NObj_1190\"\r\n}"
headers = {
    'Content-Type': "application/json",
    'Authorization': "Basic ZW5hYmxlXzE6Y2lzY28="
    }

response = requests.request("POST", url, verify=False, data=payload, headers=headers)

print(response.text)
