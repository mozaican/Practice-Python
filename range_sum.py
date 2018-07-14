"""
You have a list of two numbers. Return the sum 
of those two numbers plus the sum of all the 
numbers between them.
The lowest number will not always come first.
"""

def sum_all(lyst):
    sum_all = lyst[0] + lyst[1]
    if lyst[0] < lyst[1]:
        for num in range(lyst[0]+1, lyst[1]):
            sum_all += num
    else:
        for num in range(lyst[1]+1, lyst[0]+1-1):
            sum_all += num
    return sum_all
