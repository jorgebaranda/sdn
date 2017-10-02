import requests
from requests.auth import HTTPBasicAuth
import json
import sys

with open(sys.argv[1]) as data_file:    
	json_rule = json.dumps(json.load(data_file))

headers = {'Content-Type':'application/json' , 'Accept':'application/json'}
response = requests.post('http://localhost:8181/onos/v1/flows/of:5e3e486e73020629', data=json_rule, auth=('onos', 'rocks'), headers=headers)
print response.status_code

