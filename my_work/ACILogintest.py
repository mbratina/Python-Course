#  This script logs onto ACI. But HTTP must be turned on the APIC first.

import requests

url = "https://apic/api/aaaLogin.json"

payload = "{\n \"aaaUser\":{\n\t\"attributes\":{\n\t\t\"name\":\"admin\",\n\t\t\"pwd\":\"cisco123\"\n\t}\n  }\n}"
headers = {
    'cache-control': "no-cache",
    'postman-token': "68f4acae-0950-10e4-5c8a-7687bc2c3c1d"
    }
try:
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
except (requests.exceptions.ConnectionError) as err_msg:
    print "Cisco  ACI Authentication Failed.  Ensure your controller is provisioned"
    print "The Python error message is", err_msg
