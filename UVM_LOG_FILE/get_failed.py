import re


def main(lines):
    with open("FAILED.txt","w") as doc:
        pattern = re.compile(r'#\s\|\sDATA\sFAILED\s\|.*')
        for line in lines:
            if pattern.match(line):
                doc.write(line)



lines = []
if __name__ == "__main__":
    with open("UVM.txt","r") as file:
        lines = file.readlines()
        main(lines)