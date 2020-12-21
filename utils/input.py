def get_file_contents(filename):
    with open(filename) as file:
        return file.read().rstrip('\n')


def get_file_lines(filename):
    with open(filename) as f:
        lines = f.readlines()
    return [line.strip() for line in lines]


def get_file_lines_with_no_blanks(filename):
    return [line for line in get_file_lines(filename) if line != '']


def get_file_numbers(filename):
    return [int(line) for line in get_file_lines(filename)]
