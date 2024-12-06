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


    for line in lines:
