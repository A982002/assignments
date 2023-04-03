def sum_of_squares(numbers):
    """Returns the sum of the squares of all the numbers in the list."""
    result = 0
    for num in numbers:
        result += num ** 2
    return result
