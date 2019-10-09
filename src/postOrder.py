import requests

base_url = 'https://run.appstax.io/rest/369b58a7-bc4e-4fde-b1cb-c0b5023d48ce/master'
body = {
  "customer": {
    "id": "00000000-4f1d-f03a-0000-000000000065"
  },
  "deliveryAddress": {
    "id": "00000000-554d-cd2b-0000-000000000065"
  },
  "id": "00000000-6310-16b3-0000-000000000065",
  "products": [
    {
      "description": "Alexey",
      "id": "00000000-20ff-6758-0000-000000000065",
      "name": "Bob",
      "price": 1946737912,
      "variants": [
        {
          "variant": "Fiona"
        },
        {
          "variant": "Stacey"
        },
        {
          "variant": "Simona"
        },
        {
          "variant": "Bob"
        },
        {
          "variant": "Stacey"
        },
        {
          "variant": "John"
        }
      ]
    },
    {
      "description": "Simona",
      "id": "00000000-4e8f-1ba9-0000-000000000065",
      "name": "Alex",
      "price": 1542603436,
      "variants": [
        {
          "variant": "Robert"
        }
      ]
    },
    {
      "description": "Stacey",
      "id": "00000000-0748-b259-0000-000000000065",
      "name": "Stacey",
      "price": 768747578,
      "variants": [
        {
          "variant": "Alex"
        },
        {
          "variant": "Robert"
        },
        {
          "variant": "Alexey"
        },
        {
          "variant": "Alex"
        }
      ]
    }
  ],
  "subtotal": 1638496702,
  "tax": 627963836,
  "timestamp": "2017-09-01T03:55:30",
  "total": 502062723
}


headers = {'Content-type': 'application/json'}
email_response = requests.post(base_url + '/Order/record', json=body, headers=headers)
print(email_response.text)
