#!/usr/bin/python3
""" script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter
"""

if __name__ == "__main__":
    import sys
    import requests

    data = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], data=data)
    print(r.text)
