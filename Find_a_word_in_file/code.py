import re
import sys
import os



def count_lines(content):
    lines = len(content)
    print(f'No of lines: {lines}')

def count_words(content):
    words = 0
    for line in content:
        split_line = line.split()
        word_count = len(split_line)
        words = words +word_count
    print(f'No of words:{words}')

PATTERN = 'Verilog'
def count_Verilog(content):
    Verilog = 0
    for line in content:
        split_line = line.split()
        if PATTERN in split_line:
            Verilog = Verilog+1
    print(f'No of Verilog(Exact match):{Verilog}')


def main(source):
    path = os.getcwd()
    file_path = os.path.join(path,source)
    with open(file_path,'r') as file:
        content = file.readlines()
        count_lines(content)
        count_words(content)
        count_Verilog(content)




if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        raise Exception("Enter Source File")
    source = args[1]
    main(source)

