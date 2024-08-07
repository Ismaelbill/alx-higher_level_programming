#!/usr/bin/python3
""" sends a request to the URL and displays the body of the response """

if __name__ == "__main__":
    import urllib.request
    import urllib.error
    import sys

    try:
        with urllib.request.urlopen(sys.argv[1]) as f:
            print(f.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
