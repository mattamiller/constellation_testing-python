import requests
import pprint


# define functions
def getAccountInfo(email, endpoint):
    account_response = requests.get(endpoint + '/Customer/byEmailWithAddressAndOrders?email=' + email).json()
    full_name = account_response["data"]["customerByEmail"]["firstName"] + ' ' + \
                account_response["data"]["customerByEmail"]["lastName"]
    return full_name


def getOrderById(order_id, endpoint):
    order = requests.get(endpoint + '/Order/byID?id=' + order_id).json()
    return order


#  main
def main():
    endpoint = ('https://run.appstax.io/rest/369b58a7-bc4e-4fde-b1cb-c0b5023d48ce/master')
    pp = pprint.PrettyPrinter(indent=4)

    while True:
        order_id = input("Order ID:")
        data = getOrderById(order_id, endpoint)
        cust_email = data["data"]["order"]["customer"]["email"]
        cust_name = getAccountInfo(cust_email, endpoint)


        pp.pprint(data)
        print('Customer Name: ' + cust_name)
        print('Customer Email: ' + cust_email)
        print('\n------------------')

    # print(getAccountInfo("foo@spacefleet.gov",endpoint))

if __name__ == '__main__':
    main()
