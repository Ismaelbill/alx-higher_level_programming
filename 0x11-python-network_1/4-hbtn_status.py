#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status """

if __name__ == "__main__":
    import requests

    var = "https://alx-intranet.hbtn.io/status"
    r = requests.get(var)
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- type: {}".format(r.text))
