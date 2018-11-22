# Requirements

Python Version - 3.6.6

# Installation

Make a virtual enviornment, and then install the requirements using the command, `pip install -r requirements.txt`.

# Executing the Application

Once done installing the dependencies you can run the application with the command `flask run`, it will automatically start listening on port 5000.

# Testing the Application

You can open up your favorite browser and then make a request to endpoint or simply use curl.

To find branch detail with IFSC code - http://127.0.0.1:5000/branch?ifsc=SBIN0030377
To find branch detail with city and bank name - http://127.0.0.1:5000/branchInCity?name=State%20bank%20of%20india&city=jaipur