import json

json_string = '{ "aaaUser": {"attributes": {    "name" : "admin",    "pwd" : "cisco123" } }    }'
parsed_json = json.loads(json_string)
print(parsed_json["aaaUser"]['attributes']['name'])
print(parsed_json["aaaUser"]['attributes']['pwd'])
