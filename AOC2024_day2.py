import numpy as np

# Test data
# rows = [[7, 6, 4, 2, 1],
# [1, 2, 7, 8, 9],
# [9, 7, 6, 2, 1],
# [1, 3, 2, 4, 5],
# [8, 6, 4, 4, 1],
# [1, 3, 6, 7, 9]]
with open('day2input.txt', 'r', encoding = 'utf-8') as file:
    rows = [[int(num) for num in line.split()] for line in file]

def riseorfall(x):
    """
    Checks if the input list is in ascending or descending order.

    """
    return np.all(np.diff(x) > 0) or np.all(np.diff(x) < 0)

def differ(a, b):
    """
    Checks if the difference between two numbers is between 1 and 3.
    """
    difference = abs(a - b)
    return 1 <= difference <= 3

def safe(row):
    """
    Checks if a row is safe using conditions from differ and riseorfall functions.

    """
    return (all(differ(row[i], row[i + 1]) for i in range(len(row) - 1))
            and riseorfall(row))

def checkinittwice(x):
    """
    Checks the safety of each row in the input list and counts the 
    number of safe rows and tolerated rows.
    A row is considered safe if the `safe` function returns True for that row. 
    If a row is not safe, it is checked if it can be made safe by removing one element. 
    If so, it is counted as tolerated.
    Args:
        x (list): A list of rows to be checked. Each row is a list or string.
    Returns:
        tuple: A tuple containing two integers:
            - safe_count (int): The number of rows that are safe.
            - tolerated (int): The number of rows that are tolerated 
              (can be made safe by removing one element).
    """
    safe_count = 0
    tolerated = 0
    for row in x:
        if safe(row):
            safe_count += 1
            continue

        safety_tolerated = False
        for i in range(len(row)):
            tolerow = row[:i] + row[i + 1:]
            if safe(tolerow):
                tolerated += 1
                safety_tolerated = True
                break
        if not safety_tolerated:
            pass
    return safe_count, tolerated


naughty, nice = checkinittwice(rows) # Themed names for fun :)
print(f"Safe rows without removal: {nice}")
print(f"Safe rows after removing offending values: {naughty}")
