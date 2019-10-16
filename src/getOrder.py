import requests
import pprint
import json

def getAccountInfo(email, endpoint) :
    account_response = requests.get(endpoint+'/Customer/byEmailWithAddressAndOrders?email='+email).json()
    full_name = account_response["data"]["customerByEmail"]["firstName"]+' '+account_response["data"]["customerByEmail"]["lastName"]
    return full_name

endpoint = ('https://run.appstax.io/rest/369b58a7-bc4e-4fde-b1cb-c0b5023d48ce/master')
pp = pprint.PrettyPrinter(indent=4)

while True:
    order_id = input("Order ID:")
    # order_id = '6bb828c3-9060-4994-a235-ae6a54537772'
    order_response = requests.get(endpoint+'/Order/byID?id='+order_id)
    # order_response = requests.get(base_url +'/order/byOrderID?id=6bb828c3-9060-4994-a235-ae6a54537772')
    data = order_response.json()
    pp.pprint(data)
    cust_email = data["data"]["order"]["customer"]["email"]
    cust_name = getAccountInfo(cust_email, endpoint)
    print(order_response)
    print('Customer Name: '+ cust_name)
    print('Customer Email: ' + cust_email)
    print('\n------------------')


