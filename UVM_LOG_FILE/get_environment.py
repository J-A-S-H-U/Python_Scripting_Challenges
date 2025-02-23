import re


def main(lines):
    with open("ENVIRONMENT.txt","w") as doc:
        pattern = re.compile(r'.*\senvironment.sv.*')
        for line in lines:
            if pattern.match(line):
                doc.write(line)



lines = []
if __name__ == "__main__":
    with open("UVM.txt","r") as file:
        lines = file.readlines()
        main(lines)