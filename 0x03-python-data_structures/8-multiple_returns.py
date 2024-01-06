#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) > 0:
        a = len(sentence)
        b = sentence[0]
    else:
        a = 0
        b = None
    return a, b
