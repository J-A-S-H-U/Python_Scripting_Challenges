import sys
import os
import re


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


def count_Verilog(content):
    Verilog = 0
    for line in content:
        split_line = line.split()
        count = split_line.count("Verilog")
        Verilog = Verilog + count
    print(f'No of Verilog(Exact match): {Verilog}')

def count_verilog_not_exact(content):
    verilog = 0
    verilog = sum(len(re.findall(r"verilog", line, re.IGNORECASE)) for line in content)
    print(f'No of Verilog(Not Exact match): {verilog}')




def main(source):
    path = os.getcwd()
    file_path = os.path.join(path,source)
    with open(file_path,'r') as file:
        content = file.readlines()
        count_lines(content)
        count_words(content)
        count_Verilog(content)
        count_verilog_not_exact(content)



if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        raise Exception("Enter Source File")
    source = args[1]
    main(source)

