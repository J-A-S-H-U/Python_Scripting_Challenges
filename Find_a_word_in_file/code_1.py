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

def count_first_word(content):
    first = 0
    for line in content:
        match = re.match(r'\AVerilog',line)
        if match:
            first = first+1
    print(f'No of first occurences:{first}')

def Replace_VHDL(content):
    with open("sample_vhdl.txt","w") as efile:
        for line in content:
            new_line = line.replace("Verilog","VHDL")
            efile.write(new_line)
    efile.close()

def remove_empty_line(content):
    with open("sample_ver.txt", "w") as file:
        for line in content:
            if line.split():
                file.write(line)
    file.close()



def main(source):
    path = os.getcwd()
    file_path = os.path.join(path,source)
    with open(file_path,'r') as file:
        content = file.readlines()
        count_lines(content)
        count_words(content)
        count_Verilog(content)
        count_verilog_not_exact(content)
        count_first_word(content)
        Replace_VHDL(content)
        remove_empty_line(content)


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        raise Exception("Enter Source File")
    source = args[1]
    main(source)

