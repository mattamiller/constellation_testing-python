

import requests
import pprint
import json

pp = pprint.PrettyPrinter(indent=4)
base_url = ('https://run.appstax.io/rest/369b58a7-bc4e-4fde-b1cb-c0b5023d48ce/master')
# email_response = requests.get(base_url +'/Customer/byEmailWithAddressAndOrders?email=delaphnie%40spacefleet.gov')


while True:
    email_address = input("Login:").replace('@','%40')
    email_response = requests.get(base_url +'/Customer/byEmailWithAddressAndOrders?email='+email_address)
    data = email_response.json()
    pp.pprint(data)


    # Account Details
    print('First Name: '+data["data"]["customerByEmail"]["firstName"])
    print('Last Name: '+data["data"]["customerByEmail"]["lastName"])
    print('Contact Email: '+data["data"]['customerByEmail']['email'])
    # print('Contact Email: '+ data["data"]['customerByEmail'][{'orders'}])



    print('---------------------------------')