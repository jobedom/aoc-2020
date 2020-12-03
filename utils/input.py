def get_file_lines(filename):
    with open(filename) as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    lines = [line for line in lines if line != '']
    return lines


def get_file_numbers(filename):
    return [int(line) for line in get_file_lines(filename)]
