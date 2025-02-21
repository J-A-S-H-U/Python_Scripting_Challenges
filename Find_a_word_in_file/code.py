import re
import sys
import os


def main(source):
    path = os.getcwd()
    file_path = os.path.join(path,source)
    print(file_path)




if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        raise Exception("Enter Source File")
    source = args[1]
    main(source)

