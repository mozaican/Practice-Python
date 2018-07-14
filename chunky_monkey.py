"""
Write a function that splits a list (first argument) 
into groups the length of size (second argument) and 
returns them as a two-dimensional list.
"""

def chunky_monkey(lyst, size):
    new_lyst = []
    for i in range(0, len(lyst), size):
        new_lyst.append(lyst[i:i+size])
    return new_lyst


