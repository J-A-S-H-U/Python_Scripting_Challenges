import re


def main(lines):
    with open("TOP_MODULES.txt","w") as doc:
        pattern = re.compile(r'#\sTop\slevel\smodules:')
        for i, line in enumerate(lines):
            if pattern.match(line):  
                for j in range(i, min(i + 4, len(lines))): 
                    doc.write(lines[j].strip()+"\n")
                    if j==min(i + 4, len(lines))-1:
                        doc.write("\n")
                        break



lines = []
if __name__ == "__main__":
    with open("UVM.txt","r") as file:
        lines = file.readlines()
        main(lines)