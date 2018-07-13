"""
Return the lowest index at which a value (second argument) 
should be inserted into an array (first argument) once it 
has been sorted. The returned value should be a number.
"""

def find_index(lyst, num):
    for i in range(len(lyst)):
        if lyst[i] < num:
            continue
        else:
            return i 
