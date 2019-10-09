import requests
import json

base_url = ('https://run.appstax.io/rest/369b58a7-bc4e-4fde-b1cb-c0b5023d48ce/master')


order_response = requests.get(base_url +'/order/byOrderID?id=00000000-4f1d-f03a-0000-000000000065')
data = order_response.json()
print(data)