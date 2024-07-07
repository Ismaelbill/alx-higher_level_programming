#!/usr/bin/python3
""" listing 10 commits from a giving repo"""

if __name__ == "__main__":
    import requests
    import sys

    var = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[2], sys.argv[1])

    r = requests.get(var)

    for i in r.json()[:10]:
        print('{}: {}'.format(i.get('sha'), i.get('commit').get('author').get('name')))
