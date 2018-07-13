"""
Repeat a given string str (first argument) for num times (second argument). 
Return an empty string if num is not a positive number.
"""

def repeat_string(string, num):
    if num > 0:
        return string * num
    else:
        return ""