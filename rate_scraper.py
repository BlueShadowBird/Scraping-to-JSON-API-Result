import requests

idr_json_string = requests.get('http://www.floatrates.com/daily/idr.json')
idr_json = idr_json_string.json()

for data_key in idr_json.values():
    print(data_key)