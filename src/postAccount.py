import requests

base_url = 'https://run.appstax.io/rest/369b58a7-bc4e-4fde-b1cb-c0b5023d48ce/master'
body = {
  "addresses": [
    {
      "city": "Alexey",
      "id": "00000000-37ed-5893-0000-000000000066",
      "name": "Alexey",
      "state": "Fiona",
      "street": "Fiona",
      "zipcode": "Robert"
    },
    {
      "city": "Bob",
      "id": "00000000-7408-dcf8-0000-000000000066",
      "name": "Robert",
      "state": "Fiona",
      "street": "Stacey",
      "zipcode": "Josephine"
    }
  ],
  "email": "matt@spacefleet.gov",
  "firstName": "Matt",
  "id": "00000000-0347-4bdc-0000-000000000066",
  "lastName": "Miller"
}
headers = {'Content-type': 'application/json'}
email_response = requests.post(base_url + '/Customer/update', json=body, headers=headers)
print(email_response.text)
