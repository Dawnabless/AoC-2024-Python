import os
import re
def part_one(file_path):
    with open(file_path) as file:
        lines = file.readlines()

    total = 0
    for line in lines:
        # i dont know regex, i just typed things til it worked, so this can probably be done a lot nicer
        total += sum([(int(nums[0]) * int(nums[1])) for nums in re.findall(r'mul\((\d*),(\d*)\)', line)])

    return total

def part_two(file_path):
    with open(file_path) as file:
        lines = file.readlines()

    # dont know enough regex to figure this one out sorry
    print('🐄🐄')









if __name__ == "__main__":
    data_path = os.path.join('data', 'day3.txt')
    print(part_one(data_path))
    print('part two:', part_two(data_path))