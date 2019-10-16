# Constellation Testing
 
This repo is dedicated to testing the Constellation toolset with python

Here is a list of the programs, what they demonstrate, and how to run them:

connect_cassandra.py & connect_dse.py
--
For now this is just the code snippet from the DSE documentation for how to connect via the python driver.  Docs Here: 
https://helpdocs.datastax.com/aws/dscloud/apollo/dscloudPythonDriver.html#dscloudPythonDriver
  
  For the python setup, it is recommended to use 'pyenv' to manage the different versions of python on your machine without changing the system level python.  Docs here: 
  
  https://realpython.com/intro-to-pyenv/#why-use-pyenv
  
writingAppstaxEcommerce.py 
--
This program is based on AppStax and the generated endpoints provided by AppStax.  So no driver necessary because all DSE calls are via REST.  Two functions in the program plus a main function.  "addAccount" function adds a new user to the system, and "addOrder" does exactly what the name implies.  The order ID is a randomly generated UUID.  Once the order is added, the order ID is printed so that you can go look up your new order via the "readingAppstaxEcommerce.py".  Initially the data generation is very static and manual, but eventually it will more dynamic and require less manual data entry.  Depending on what operation you want to run, comment and uncomment sections of main()


readingAppstaxEcommerce.py
--
The readAppstaxEcommerce program loops through either an account lookup by email or an order lookup via orderID.