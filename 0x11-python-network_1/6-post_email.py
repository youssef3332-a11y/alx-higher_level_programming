#!/usr/bin/python3
""" alot"""
import requests
import sys


def post_email(url, email):
    # The payload containing the email address, sent in the POST request
    payload = {'email': email}

    # Sending the POST request with the payload
    response = requests.post(url, data=payload)

    # Displaying the body of the response
    # print(response.status_code)
    print(response.text)


if __name__ == "__main__":
    # The URL and email address are passed as command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]
    # Calling the function to send the POST request and display the response
    post_email(url, email)
