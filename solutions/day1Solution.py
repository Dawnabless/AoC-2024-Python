import os
import numpy as np

def part_one(file_path):
    """
    We need to separate the 1st and second columns and sort them smallest -> biggest
    Then, we must compare each list together to find distance between each value
    add each distance up at the end.

    :param file_path: data for problem
    :return: total distance between left and right columns added up
    """

    with open(file_path) as file:
        lines = file.readlines()

    col1 = []
    col2 = []
    for line in lines:
        left, right = line.split()
        col1.append(int(left))
        col2.append(int(right))

    col1.sort()
    col2.sort()

    return sum(np.abs((np.array(col1) - np.array(col2))))


print(part_one(os.path.join('data', 'day1.txt')))