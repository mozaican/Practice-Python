"""Return the factorial of the provided integer"""

def factorial(number):
    if number == 0:
        return 1
    elif number == 1:
        return 1
    else:
        return factorial(number-1) * number