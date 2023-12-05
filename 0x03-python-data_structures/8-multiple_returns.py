#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first = sentence[0]
    tup1 = length, first
    tup2 = length, None
    if len(sentence) != 0:
        return tup1
    else:
        return tup2
