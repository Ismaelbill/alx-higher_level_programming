#!/usr/bin/python3
""" listing 10 commits """

if __name__ == "__main__":
    import requests
    import sys

    var = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[1], sys.argv[2])

    r = requests.get(var)

    j = 0
    for i in list(r.json()):
        print('{}:'.format(i['sha']), i['commit']['author']['name'])
        j += 1
        if j == 10:
            exit(0)
