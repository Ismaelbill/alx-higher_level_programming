#!/usr/bin/python3
""" script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

if __name__ == "__main__":
    import sys
    import requests

    if len(sys.argv) == 2:
        data = {'q': sys.argv[1]}
    else:
        data = {'q': ''}

    r = requests.post('http://0.0.0.0:5000/search_user', data=data)
    try:
        jsonade = r.json()
        if jsonade:
            print('[{}]'.format(jsonade.get('id')), jsonade.get('name'))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
