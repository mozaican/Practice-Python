"""
Return true if the string in the first element of 
the list contains all of the letters of the string 
in the second element of the list.
"""

def mutations(lyst):
    for letter in range(len(lyst[1])):
        if lyst[1][letter].lower() in lyst[0].lower():
            return True
        else:
            return False