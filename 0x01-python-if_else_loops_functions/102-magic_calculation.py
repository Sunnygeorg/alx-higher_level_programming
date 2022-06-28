#!/usr/bin/python3
def magic_calculations(a, b, c):
    if a < b:
        return c
    else:
        if c > b:
            return a + b
    return (a * b) - c
