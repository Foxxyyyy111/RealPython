"""Module to demonstrate Pylint conventions."""
def count(sequence, item):
    """Count the number of times an item occurs in a sequence."""
    y = 0
    for n in sequence:
        if n == item:
            y += 1
    return y
