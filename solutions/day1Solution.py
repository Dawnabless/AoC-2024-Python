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


def part_two(file_path):
    """
    For every unique value in the left column, check how often it appears in right column and multiply itself by that
    sum up the resulting values

    :param file_path: data for problem
    :return: sum of times left items appear in right, multiplied by original value
    """

    with open(file_path) as file:
        lines = file.readlines()

    col1 = set()
    col2 = []
    for line in lines:
        left, right = line.split()
        col1.add(int(left))
        col2.append(int(right))

    sim_count = 0
    for number in col1:
        sim_count += number * col2.count(number)

    return sim_count


if __name__ == "__main__":
    data_path = os.path.join('data', 'day1.txt')
    print(part_one(data_path))
    print(part_two(data_path))
