"""Return the length of the longest word in a string"""

def longest_word(string):
    words = string.split(" ")
    longest = 0
    for word in words:
        if len(word) > longest:
            longest = len(word)
    return longest