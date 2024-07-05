#!/usr/bin/python3
""" ends a POST request to the passed URL with the email
as a parameter, and displays the body of the response """

if __name__ == "__main__":
    import urllib.parse
    import urllib.request
    import sys

    data = urllib.parse.urlencode({'email': sys.argv[2]})
    data = data.encode('ascii')
    with urllib.request.urlopen(sys.argv[1], data) as f:
        print(f.read().decode('utf-8'))
