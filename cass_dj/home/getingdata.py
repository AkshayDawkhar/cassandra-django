import requests
import json
# response_API = requests.get('https://api.covid19india.org/state_district_wise.json')
# #print(response_API.status_code)
# data = response_API.text
# parse_json = json.loads(data)
# active_case = parse_json['Andaman and Nicobar Islands']['districtData']['South Andaman']['active']
# print("Active cases in South Andaman:", active_case)

response_API2 = requests.get('http://127.0.0.1:8000/a')
data2 = response_API2.text
parse_json2 = json.loads(data2)
print(type(parse_json2))
print(len(parse_json2))
for p in parse_json2:
    print(p)
