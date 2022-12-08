"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for val in items:
        if checkItem(val, frequencies):
            frequencies[str(val)] = 1
        else:
            frequencies[str(val)] = frequencies[str(val)] + 1
    return frequencies

def checkItem(item, frequencies):
    if str(item) not in frequencies.keys():
        return True
    return False