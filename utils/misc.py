import os


def init(filename, day):
    print(f'----------- Day {day} -----------')
    os.chdir(os.path.dirname(os.path.abspath(filename)))
