#!/usr/bin/python3
"""
This module Takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the response
(decoded in utf-8)
"""
from sys import argv
import requests


if __name__ == '__main__':
    response = requests.post(argv[1], {'email': argv[2]})
    print(response.text)
