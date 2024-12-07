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
    with open(file_path) as file:
        lines = [[int(num) for num in line.split()] for line in file.readlines()]
    # im just gonna redo the whole thing even worse now

    # check if numbers are right dist
    # check removing 1 bad level
    # check if increasing or decreasing
    good_count = 0
    for line in lines[:]:
        bad_count = 0

        # check for too many dupes
        for num in set(line):
            if line.count(num) > 1:
                bad_count += 1
                if bad_count > 1:
                    continue

        bad_count = 0
        # check if next are good
        for i, curr_num in enumerate(line):
            if i != len(line) - 1:
                if abs(curr_num - line[i + 1]) > 3 or abs(curr_num - line[i + 1]) < 1:
                    bad_count += 1
                    if i != len(line) - 2:
                        if abs(curr_num - line[i + 2]) > 3 or abs(curr_num - line[i + 2]) < 1:
                            bad_count += 1
                        else:
                            print(f'index: {i}, curr_num: {curr_num}, {line}')
                            line.pop(i + 1)
                            print(f'after:{line}')

        if bad_count > 1:
            print(line)
            continue

        # check if it follows direction fully
        # determine direction
        direction = 0
        for i, num in enumerate(line):
            if i == 0:
                last_num = num
            if num > last_num:
                direction += 1
            elif num < last_num:
                direction -= 1
            else:
                direction += 0
            last_num = num

            if abs(direction) != i:
                print("SORTING ERROR:", line, num)
                line.pop(i)
                break



        good_count += 1




    return good_count






if __name__ == "__main__":
    data_path = os.path.join('data', 'day2.txt')
    # print(part_one(data_path))
    print('part two:', part_two(data_path))
