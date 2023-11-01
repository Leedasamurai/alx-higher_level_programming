#!/usr/bin/python3

def remove_char_at(str, n):
    if 0 <= n < len(str):
        return str[:n] + str[n+1:]
    return str
# creates a copy of the string, removing the character at the position n
