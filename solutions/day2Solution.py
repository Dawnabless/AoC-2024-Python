import os
import numpy as np


def part_one(file_path):

    with open(file_path) as file:
        lines = file.readlines()

    safe_count = 0
    for line in lines:
        # check for lines that arent continuous one direction (heehee, lazy)
        levels = [int(level) for level in line.split(' ')]
        if levels != sorted(levels) and levels != sorted(levels, reverse=True):
            print('bad line:', line)
            continue
        else:
            # check that numbers are not too far apart or too close
            for i, curr_num in enumerate(levels):
                if i == len(levels) - 1:
                    safe_count += 1
                elif abs(curr_num - levels[i + 1]) > 3 or abs(curr_num - levels[i + 1]) < 1:
                    print('Bad line:', line)
                    break

    return safe_count


def part_two(file_path):
    print("no... just no...")













if __name__ == "__main__":
    data_path = os.path.join('data', 'day2.txt')
    # print(part_one(data_path))
    print('part two:', part_two(data_path))
