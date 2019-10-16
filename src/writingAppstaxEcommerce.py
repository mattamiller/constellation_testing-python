import requests
import uuid

def addAccount(first_name, last_name, email, endpoint ) :
    base_url = endpoint
    body = {
        "id": "55982a37-50b0-4b08-849a-28c6cbcf66be",
        "firstName": first_name,
        "lastName": last_name,
        "email": email,
        "addresses": [
            {
                "id": "cbcb36d4-d038-4e77-88df-84438f9513cd",
                "name": "Delaphanie Expulsivario",
                "street": "X-5+N33.5",
                "city": "Mongroves",
                "zipcode": "544357",
                "state": "Planet PY552"
            }
        ]
    }

    headers = {'Content-type': 'application/json'}
    email_response = requests.post(base_url + '/Customer/update', json=body, headers=headers)
    print(email_response)

    #Add if statement here to read out status of request based on return code (ie error or success)

def addOrder(endpoint) :
    rand_id = uuid.uuid1()
    base_url = endpoint
    body = {
        "customer": {
            "id": rand_id,
            "lastName": "Alexey",
            "email": "johndoe826034912@gmail.com",
            "id": "00000000-2b7a-0c5f-0000-000000000065",
            "firstName": "Bob"
        },
        "deliveryAddress": {
            "id": "00000000-554d-cd2b-0000-000000000065"
        },
        "id": str(rand_id),
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
    print(requests.post(base_url + '/Order/record', json=body, headers=headers))
    print("Order ID: "+str(rand_id))
    return rand_id

def main() :
    endpoint = ('https://run.appstax.io/rest/369b58a7-bc4e-4fde-b1cb-c0b5023d48ce/master')

    first_name = "Foo"
    last_name = "Barr"
    email = "foo@spacefleet.gov"


    addOrder(endpoint)
    # addAccount(first_name,last_name,email,endpoint)


if __name__ == '__main__':
    main()