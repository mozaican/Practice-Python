""" Return the largest numbers in lists.
    Return a list consisting of the largest number from each provided sub-list.
"""

def largest_numbers(lyst):
    largest_numbers = []
    for sublyst in range(len(lyst)):
        largest = 0
        for number in range(len(lyst[sublyst])):
            if lyst[sublyst][number] > largest:
                largest = lyst[sublyst][number]
        largest_numbers.append(largest)

    return largest_numbers
