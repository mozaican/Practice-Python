"""
    Check if a string (first argument, string) ends with 
    the given target string (second argument, target).
"""

def confirm_ending(string, target):
    if string[-len(target):] == target:
        return True
    else:
        return False