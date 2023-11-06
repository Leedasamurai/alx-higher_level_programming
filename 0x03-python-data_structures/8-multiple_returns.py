#!/usr/bin/python3
def multiple_returns(sentence):
    leng = len(sentence)
    if leng == 0:
        f_char = None
    else:
        f_char = sentence[0]
    return leng, f_char
