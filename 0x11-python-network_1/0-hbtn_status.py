#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status status """

import urllib.request

var = 'https://alx-intranet.hbtn.io/status'
with urllib.request.urlopen(var) as resp:
    html = resp.read()
    print('Body response:')
    print('\t- type: {}'.format(type(html)))
    print('\t- content: {}'.format(html))
    print('\t- utf8 content: {}'.format(html.decode('utf-8')))
