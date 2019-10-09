

import requests
import json


base_url = ('https://run.appstax.io/rest/369b58a7-bc4e-4fde-b1cb-c0b5023d48ce/master')
email_response = requests.get(base_url +'/Customer/byEmailWithAddressAndOrders?email=delaphnie%40spacefleet.gov')
data = email_response.json()
print(data)
last_name = data["data"]["customerByEmail"]["lastName"]
print(last_name)
