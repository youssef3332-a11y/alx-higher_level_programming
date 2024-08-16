#!/usr/bin/python3
""" there is"""
import requests
import sys


def fetch(url):
    response = requests.get(url)
    var = response.headers.get('X-Request-Id')
    if var:
        print(var)


if __name__ == "__main__":
    url = sys.argv[1]
    fetch(url)
