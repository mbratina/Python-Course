import requests

url = "http://192.168.10.80/restconf/api/config/native/interface/Loopback/500"

payload = "{\r\n\t\"ned:Loopback\": {\r\n\t\t\"name\": 500,\r\n\t\t\"ip\": {\r\n\t\t\t\"address\": {\r\n\t\t\t\t\"primary\": {\r\n\t\t\t\t\t\"address\": \"170.99.1.1\",\r\n\t\t\t\t\t\"mask\": \"255.255.255.0\"\r\n\t\t\t\t}\r\n\t\t\t}\r\n\t\t}\r\n\t}\r\n}"
headers = {
    'Content-Type': "application/vnd.yang.data+json",
    'Accept': "application/vnd.yang.data+json",
    'Authorization': "Basic YWRtaW46Y2lzY28="
    }

response = requests.request("PUT", url, data=payload, headers=headers)

print(response.text)
