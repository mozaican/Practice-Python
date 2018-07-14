"""
Compare two lists and return a new list with any items 
only found in one of the two given lists, but not both. 
In other words, return the symmetric difference of the two lists.
"""

def differences(lyst1, lyst2):
    set1 = set(lyst1)
    set2 = set(lyst2)
    new_lyst = []
    diff1 = set1.difference(set2) 
    diff2 = set2.difference(set1)
    new_lyst.extend(list(diff1))
    new_lyst.extend(list(diff2))
    return new_lyst
