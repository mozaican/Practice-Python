"""
Truncate a string (first argument) if it is longer than 
the given maximum string length (second argument). 
Return the truncated string with a ... ending.
"""

def truncate_string(string, num):
    if len(string) > num:
        return string[:num] + "..."